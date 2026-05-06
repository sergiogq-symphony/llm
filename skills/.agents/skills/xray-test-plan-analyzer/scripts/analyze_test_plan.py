import os
import sys
import json
import re
import urllib.parse
import subprocess

def run_jira_search(jql, limit=1000):
    user = os.environ.get('JIRA_USER_EMAIL')
    token = os.environ.get('JIRA_API_TOKEN')
    encoded_jql = urllib.parse.quote(jql)
    url = f"https://perzoinc.atlassian.net/rest/api/2/search?jql={encoded_jql}&maxResults={limit}"
    
    cmd = ["curl", "-s", "-u", f"{user}:{token}", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return None
    try:
        return json.loads(result.stdout)
    except:
        return None

def analyze_plan(plan_id):
    print(f"### Analyzing Test Plan: {plan_id}")
    
    # 1. Get all Test Executions linked to the plan
    # Note: Xray provides JQL functions for this
    jql_executions = f'issue in testPlanTestExecutions("{plan_id}")'
    exec_data = run_jira_search(jql_executions)
    
    if not exec_data or 'issues' not in exec_data:
        print(f"Error: Could not find executions for {plan_id}")
        return

    executions = exec_data['issues']
    print(f"Found {len(executions)} Test Executions.\n")
    
    results = {} # Area -> {Manual: X, AutoPhx: Y, AutoExt: Z}
    
    for ex in executions:
        key = ex['key']
        summary = ex.get('fields', {}).get('summary', '').upper()
        
        # Determine Area
        area = "General / Other"
        if "C2" in summary or "XPOD" in summary: area = "Phoenix (C2 / XPOD / Core)"
        elif "FEDERATION" in summary: area = "Federation"
        elif "SDA" in summary: area = "SDA"
        elif "DIRECTORY" in summary: area = "Directory"
        elif "UWH" in summary: area = "UWH"
        elif "LOGIN" in summary or "SSO" in summary: area = "Login / SSO"
        
        # Determine Type
        is_auto = "AUTO" in summary or "AUTOMATION" in summary
        is_phx = "PHX" in summary or "PHOENIX" in summary or any(x in summary for x in ["C2", "AGENT", "XPOD"])
        
        # Count tests in this execution
        jql_tests = f'issue in testExecutionTests("{key}")'
        # We only need the total, so maxResults=0
        test_data = run_jira_search(jql_tests, limit=0)
        count = test_data.get('total', 0) if test_data else 0
        
        if area not in results:
            results[area] = {"Manual": 0, "AutoPhx": 0, "AutoExt": 0}
            
        if not is_auto:
            results[area]["Manual"] += count
        elif is_phx:
            results[area]["AutoPhx"] += count
        else:
            results[area]["AutoExt"] += count

    # Print Table
    print("| Functional Area | Manual Tests | Auto (Phoenix) | Auto (Outside) | Total |")
    print("| :--- | :---: | :---: | :---: | :---: |")
    
    grand_manual = 0
    grand_phx = 0
    grand_ext = 0
    
    for area, counts in sorted(results.items()):
        m = counts["Manual"]
        ap = counts["AutoPhx"]
        ae = counts["AutoExt"]
        row_total = m + ap + ae
        print(f"| **{area}** | {m} | {ap} | {ae} | **{row_total}** |")
        grand_manual += m
        grand_phx += ap
        grand_ext += ae
        
    print(f"| **TOTAL** | **{grand_manual}** | **{grand_phx}** | **{grand_ext}** | **{grand_manual + grand_phx + grand_ext}** |")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_test_plan.py <TEST-PLAN-ID>")
    else:
        analyze_plan(sys.argv[1])

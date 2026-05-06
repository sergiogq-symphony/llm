---
name: xray-test-plan-analyzer
description: Performs a comprehensive breakdown of Xray Test Plans, categorizing tests by functional area, testing type (manual/automation), and environment (Phoenix/External). Use when asked to analyze a Jira Test Plan ID (e.g., TEST-102954).
user-invocable: true
allowed-tools: [run_shell_command]
---

# Xray Test Plan Analyzer

This skill automates the extraction and categorization of Xray test cases linked to a specific Test Plan.

## Prerequisites

Ensure the following environment variables are set in your terminal:
- `JIRA_USER_EMAIL`: Your Jira account email.
- `JIRA_API_TOKEN`: Your Jira API token.

## Workflow

1.  **Identify the Test Plan ID**: Extract the `TEST-XXXXXX` key from the user request.
2.  **Run Analysis**: Execute the bundled Python script to perform JQL searches and aggregate results.
3.  **Display Report**: Present the generated markdown table and summary to the user.

## Usage

When triggered, run the following command:

```bash
python3 scripts/analyze_test_plan.py <TEST-PLAN-ID>
```

The script handles:
-   Finding all linked Test Executions using `testPlanTestExecutions()`.
-   Counting tests in each execution using `testExecutionTests()`.
-   Categorizing by Area (C2, Federation, SDA, etc.) based on execution summaries.
-   Splitting Automation between Phoenix and External environments.

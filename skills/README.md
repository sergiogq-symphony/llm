# Skills

This repository contains Agent Skills compatible with **Gemini CLI**, **Claude Code**, and other agents supporting the [Agent Skills](https://agentskills.io) standard.

## Available Skills

*   **`jira-xray-test-generator`**: Generates Jira XRay Test Cases from a source Jira issue (story, bug, or task). It analyzes the source ticket, linked tickets, Confluence pages, and Figma links to understand requirements, proposes draft test cases, and creates them in the `TEST` project in Jira linked to the original issue.
*   **`xray-test-plan-analyzer`**: Performs a comprehensive breakdown of Xray Test Plans, categorizing tests by functional area, testing type (manual/automation), and environment (Phoenix/External).
*   **`jbehave-to-xray-tests`**: Parses JBehave `.story` files to extract scenarios missing a Jira Test key, creates corresponding `Xray Test` issues in Jira (automatically mapping custom fields like Associated Project, Product(s) Name, Test Type, and QE Automation Status), transitions them to the `Automated` status, and updates the `.story` files with the generated test IDs and Meta tags.
*   **`gke-log-analyzer`**: Executing gcloud and kubectl commands to analyze GKE tenant logs (e.g. for sbe-s003 or tenant-10006), diagnosing service health (SBE, keymanager, search, ai, etc.) and gathering clean raw evidence for bug reports.
*   **`jbehave-scenario-generator`**: Translates a Jira Story or Task ticket into JBehave BDD scenarios. Instructs the agent to explore repository source code to understand requirements, propose scenarios for user review and approval, implement stories and Java step definitions, and defer Jira Xray Test ticket creation until confirmed by a human.
*   **`jenkins-log-analyzer`**: Analyzes Jenkins build logs from https://jenkins.gke-use4-tools-001.symphony.com/ using Jenkins MCP tools to diagnose pipeline failures, trace test or compilation tracebacks, and propose precise remediation plans for code, dependencies, or pod configurations.

## Structure
Skills are stored in the `.agents/skills/` directory for cross-agent compatibility.

## Prerequisites
- Install the `mcp-atlassian` (follow [this](https://perzoinc.atlassian.net/wiki/spaces/QE/pages/4180115752/Testing+with+AI+LLMs#Gemini-CLI-with-MCP) guideline)
- For `xray-test-plan-analyzer`, ensure `JIRA_USER_EMAIL` and `JIRA_API_TOKEN` are set in your environment.

## Install (Gemini CLI)
```bash
# To install globally (user level):
gemini skills install xray-test-plan-analyzer.skill --scope user

 # To install locally (this workspace):
gemini skills install xray-test-plan-analyzer.skill --scope workspace

# To delete a skill
gemini skills uninstall xray-test-plan-analyzer --scope user

/skills reload
```

## Claude Code Support

### Project-level (Automatic)
If you are working within this repository, Claude Code automatically discovers the skill in `.agents/skills/`. You can trigger it immediately:
```bash
/xray-test-plan-analyzer
```

### Global Installation (Available in any project)
To use this skill in any folder on your machine with Claude Code, copy the skill directory to your global agents directory:

```bash
# Create the global directory if it doesn't exist
mkdir -p ~/.agents/skills

# Copy the skill folder from this repo to your global directory
cp -r .agents/skills/xray-test-plan-analyzer ~/.agents/skills/
```

Once copied, the `/xray-test-plan-analyzer` command will be available in any Claude Code session, regardless of which folder you are in.

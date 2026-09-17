---
name: jbehave-xray-automation
description: Automate creation of Jira Xray Test tickets from JBehave story files, including custom field mapping (Associated Project, Product, Test Type, Automation Status) and updating the story files with the new test keys.
---

# JBehave to Xray Test Automation

This skill guides the agent to parse JBehave `.story` files, create Jira Xray Test tickets for untracked scenarios, populate required custom fields, and update the story files with the generated test IDs.

## Prerequisites
- Jira MCP Server (provides `mcp_Atlassian_jira_create_issue`, `mcp_Atlassian_jira_transition_issue`, `mcp_Atlassian_jira_get_field_options`, etc.)
- Access to the target repository with `.story` files.

## Workflow

### 1. Identify Scenarios Needing Tickets
Run a Python script (or manually parse) the `.story` files to find `Scenario:` blocks that do NOT have a `[TEST-...` prefix in their title. Extract their title, `Meta:` line, and the steps (which will become the description).

You can use a Python script to extract these scenarios reliably, checking for lines starting with `Scenario:` and ensuring they don't already start with `[TEST-`.

### 2. Verify Jira Custom Fields
Before creating tickets, you must retrieve the exact IDs and values for required Jira fields. Typical fields required for Xray Tests:
- **Associated Project**: (e.g., `customfield_15362`). Usually requires a project ID (e.g., `{"id": "14400"}`).
- **Test Type**: (e.g., `customfield_15712`). Usually requires a select value (e.g., `{"value": "Integration test"}`).
- **Product(s) Name**: (e.g., `customfield_17217`). Often a multi-select array (e.g., `[{"value": "SBE"}]`).
- **QE Automation Status** / **Status**: (e.g., `customfield_15708`). Usually a select value (e.g., `{"value": "A (Automation Test Exists)"}`).

*Note: Use `mcp_Atlassian_jira_search_fields` and `mcp_Atlassian_jira_get_field_options` if you are unsure of the field ID or the exact string value expected by Jira.*

### 3. Create Jira Xray Tests
For each untracked scenario, use `mcp_Atlassian_jira_create_issue` (can be delegated to a subagent like `generalist` for bulk processing):
- `project_key`: The target Jira project (e.g., `TEST`).
- `issue_type`: `Xray Test`
- `summary`: Contextualized title, e.g., `[MCP QA] <Original Scenario Title>`
- `description`: The full text of the JBehave steps.
- `additional_fields`: A JSON string mapping the custom fields identified in step 2.
  Example:
  ```json
  {
    "customfield_15362": {"id": "14400"}, 
    "customfield_15712": {"value": "Integration test"}, 
    "customfield_15708": {"value": "A (Automation Test Exists)"}
  }
  ```

### 4. Transition the Jira Issues
Xray Tests often need to be moved to an "Automated" or "In Progress" workflow stage.
- Use `mcp_Atlassian_jira_get_transitions` to find the correct transition ID (e.g., `111` for "Automated").
- Use `mcp_Atlassian_jira_transition_issue` to transition the newly created tickets.

### 5. Update the `.story` Files
Update the original story files with the new Jira IDs:
1. Prepend the scenario title with `[TEST-XXXXXX] ` (e.g., `Scenario: [TEST-12345] User logs in`).
2. Append the lowercased test key tag to the `Meta:` block (e.g., `Meta: @featureX @test12345`).

*Tip: You can use a Python string-replacement script to apply these updates robustly to the story files, or do it surgically via `replace` if there are only a few.*

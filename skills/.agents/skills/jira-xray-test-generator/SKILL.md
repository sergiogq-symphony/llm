---
name: jira-xray-test-generator
description: Generate Jira XRay Test Cases from a source Jira issue (story, bug, or task). Analyzes the source ticket, linked tickets, Confluence pages, and Figma links to understand requirements, proposes draft test cases, and creates them in Jira linked to the original issue.
---

# Jira XRay Test Generator

This skill enables the agent to comprehensively analyze a Jira issue (Story, Bug, Task) along with its linked resources to design, propose, and create Jira XRay Test Cases.

## Workflow

### 1. Information Gathering
When the user asks to generate test cases for a specific Jira issue:
1. **Analyze Source Issue:** Use `mcp_Atlassian_jira_get_issue` to retrieve the issue's details, including description, acceptance criteria, and links.
2. **Explore Linked Jira Issues:** If there are linked issues (e.g., Epic, dependencies, blockers), retrieve their details to gain a broader understanding of the requirements.
3. **Explore Confluence Pages:** Look for Confluence page links in the issue description or remote links. Use `mcp_Atlassian_confluence_get_page` or `mcp_Atlassian_confluence_search` to read the content of these pages to extract detailed specifications.
4. **Explore Figma Links:** If the issue or Confluence pages contain Figma links, use available Figma MCP tools (if installed) or `web_fetch` to extract design context, developer handoff notes, or component details.

### 2. Test Case Design & Proposal
1. Synthesize all gathered context (Jira, Confluence, Figma).
2. Draft a comprehensive set of test cases. For each test case, include:
   - **Summary:** A clear, concise title.
   - **Description / Steps:** High-level steps to execute.
   - **Expected Result:** What should happen if the test passes.
   - **Type:** e.g., Manual, Automated.
3. Present these draft test cases to the user for review and approval. **Do not create the test cases in Jira until the user explicitly approves them.**
4. Ask the user if they want any modifications before proceeding.

### 3. Creating Test Cases in Jira XRay
Once the user approves the test cases:
1. **Create Issues:** Use `mcp_Atlassian_jira_create_issue` or `mcp_Atlassian_jira_batch_create_issues` to create the test cases. 
   - Set the `issue_type` to "Xray Test" (or the appropriate XRay test type configured if specified by the user).
   - Populate the `summary` and `description` with the approved details.
   - Use the `project_key` "TEST" by default unless instructed otherwise by the user.
2. **Link Issues:** For each newly created Test issue, use `mcp_Atlassian_jira_create_issue_link` to link it back to the original source issue. 
   - Use the appropriate link type (e.g., "Tests", "Relates to", or the specific link type used for XRay in the project).
3. **Final Report:** Provide the user with a summary of the created test cases, including their new Jira issue keys and links.

---
name: jbehave-scenario-generator
description: Generate and implement JBehave BDD scenarios from a source Jira Story or Task ticket. Explores repository source code to understand requirements, proposes Gherkin scenarios for review, implements story and step definition files, and defers Jira Xray ticket creation until confirmed by the human.
---

# JBehave Scenario Generator & Implementer

This skill guides the agent to translate a Jira Story or Task ticket into fully-formed, proposed, and implemented JBehave BDD test scenarios. It emphasizes deep exploration of the repository's source code to ensure tests are semantically accurate, well-designed, and follow local conventions.

## Core Mandates
- **Explore Source Code First:** Always explore both the requirement ticket and the actual source code of the project (via local files or GitHub) to understand current behavior, API contracts, classes, and established test steps.
- **Propose Before Creating Jira Tickets:** Propose drafted scenarios to the human for review and feedback. **Do not create any Jira Xray Test tickets** until the human has explicitly reviewed and confirmed the proposed JBehave scenarios.

## Execution Steps

### 1. Analyze the Jira Ticket
Retrieve the details of the given Story or Task ticket to understand the functional requirements and any acceptance criteria:
- Use `mcp_Atlassian_jira_get_issue` to retrieve the ticket description, custom fields, and comments.

### 2. Explore the Codebase
Explore the project's codebase in your workspace (or via GitHub) to map how the feature is implemented:
- Identify target services, APIs, and components.
- Use `grep_search` and `glob` to locate existing step definitions (`@Given`, `@When`, `@Then` classes) and `.story` files to ensure reuse of existing test fixtures and compliance with writing style.

### 3. Propose JBehave Scenarios
Draft and propose JBehave story scenarios in clear, structured Gherkin syntax:
- Present the proposed story scenarios in markdown code blocks to the human user.
- Highlight any new steps that will require java step-definition implementation.
- **Stop and wait** for user review and explicit approval. Do NOT write any story files or make any Jira updates yet.

### 4. Implement Story Files
Upon receiving approval from the human, write the `.story` file under the appropriate resources path:
- Format the file correctly with `Meta:` tags (e.g., `@mcp_server`, `@since_sbe_X`).
- Ensure scenario names are descriptive. Do not add any `[TEST-XXXX]` prefixes or `@testXXXX` tags yet, as those are created during the Xray sync.

### 5. Implement Step Definitions (Java)
Implement any new steps proposed in the scenarios:
- Write or update Java step definition classes (e.g., `@Given`, `@When`, `@Then` methods) following the repository's architecture and libraries.
- Ensure proper type safety, assertion libraries, and helper classes are utilized.
- Compile and run a test build to verify syntactic correctness.

### 6. Sync with Jira Xray (Deferred)
Only after the human user confirms they are happy with the local test execution, use the `jbehave-xray-automation` skill to create the Xray Test tickets in Jira, link them to the original Story/Task, and update the `.story` files with the final issue keys.

## Constraints & Formatting
- **Draft Headings:** Present proposals with distinct "Scenario Drafts", "Proposed Step Modifications", and "Code Exploration Observations" headings.
- **Mocking & Integration:** Align the step implementations with actual APIs and services, utilizing robust connection-testing and error-logging diagnostics.

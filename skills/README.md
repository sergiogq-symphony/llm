# Skills

This repository contains Agent Skills compatible with **Gemini CLI**, **Claude Code**, and other agents supporting the [Agent Skills](https://agentskills.io) standard.

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

# Jira Agent

## Setup
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

mv .env.example .env
# Add your variables values

gcloud auth application-default login
```

## Run Jira MCP server
```
docker run -d -p 8081:8081 \
  -e JIRA_URL="https://perzoinc.atlassian.net" \
  -e JIRA_USERNAME="sergio.gonzalez@symphony.com" \
  -e JIRA_API_TOKEN="your-jira-api-token" \
  mcp/atlassian:latest --transport sse --port 8081
```

Note: You can get the jira token [here](https://id.atlassian.com/manage-profile/security/api-tokens)

## Run
```
# Dev UI
adk web
```


## References
- https://google.github.io/adk-docs/
- https://cloud.google.com/blog/topics/developers-practitioners/use-google-adk-and-mcp-with-an-external-server


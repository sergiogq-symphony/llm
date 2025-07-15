from google.adk.agents import LlmAgent
# from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams, StdioServerParameters
from google.adk.tools import google_search


"""
Initializes and runs an ADK agent connected to the mcp/atlassian server.
"""
#remote_imagen, _ = MCPToolset(
#    connection_params=SseServerParams(url="http://localhost:8081/sse"),
#)

root_agent = LlmAgent(
    name="atlassian_assistant",
    model="gemini-2.0-flash",
    description="Answers any user question about Jira issues.",
    instruction="You are an assistant that can interact with Jira Atlassian",
    # google_search is a pre-built tool which allows the agent to perform Google searches.
    tools=[google_search]
)

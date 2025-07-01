import os

from google.adk.agents import LlmAgent
from google.adk.tools.retrieval import VertexAiRagRetrieval
from vertexai import rag

cv_vertex_retrieval = VertexAiRagRetrieval(
    name='retrieve_rag_documentation',
    description=(
        'Use this tool to retrieve Jira issues documentation and reference materials for the question from the RAG corpus'
    ),
    rag_resources=[
        rag.RagResource(
            # please fill in your own rag corpus
            # here is a sample rag coprus for testing purpose
            # e.g. projects/123/locations/us-central1/ragCorpora/456
            rag_corpus=os.environ.get("RAG_CORPUS", "")
        )
    ],
    similarity_top_k=10,
    vector_distance_threshold=0.5,
)

root_agent = LlmAgent(
    name="jira_searcher",
    model="gemini-2.0-flash",
    description="Answers any user question about Jira issues.",
    instruction="You are a helpful agent who can answer user questions about Jira issues.",
    tools=[cv_vertex_retrieval]
)

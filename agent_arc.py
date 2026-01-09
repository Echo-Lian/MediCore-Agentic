from smolagents import CodeAgent, AzureOpenAIModel, E2BExecutor

# Configure the 'Brain' via Azure
model = AzureOpenAIModel(
    model_id="gpt-4o",
    azure_endpoint="your-endpoint",
    api_key="your-key",
    api_version="2024-05-01-preview"
)

# Configure the Agent with Security and Tools
agent = CodeAgent(
    tools=[medical_knowledge_retriever, clinical_calculator],
    model=model,
    sandbox=E2BExecutor(),  # Remote secure execution for GAIA tasks
    additional_authorized_imports=["pandas", "numpy", "scipy"],
    max_steps=10            # GAIA Level 1 usually needs ~5-10 steps
)

@tool
def medical_knowledge_retriever(query: str) -> str:
    """
    Searches clinical registers and knowledge bases for the query.
    Args:
        query: The medical term or symptom to research.
    """
    # In a real BCB Medical scenario, this would query a Vector DB
    # For GAIA, it might query a local file or web search
    return "Retrieved: Protocol for [query] suggests..."
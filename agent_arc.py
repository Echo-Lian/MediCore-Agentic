from smolagents import CodeAgent, AzureOpenAIModel, E2BExecutor, tool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- 1. DEFINE MEDICAL TOOLS ---
@tool
def medical_knowledge_retriever(query: str) -> str:
    """
    Searches clinical registers and knowledge bases for the query.
    Args:
        query: The medical term or symptom to research.
    """
    # In a real BCB Medical scenario, this would query a Vector DB
    # For GAIA, it might query a local file or web search
    return f"Retrieved: Protocol for {query} suggests first-line treatment with evidence-based guidelines."

@tool
def clinical_calculator(calculation_type: str, **params) -> str:
    """
    Performs medical calculations (GFR, BMI, etc.)
    Args:
        calculation_type: Type of calculation ('gfr', 'bmi', etc.)
        **params: Parameters needed for the calculation
    """
    if calculation_type.lower() == "gfr":
        creatinine = params.get("creatinine", 1.0)
        age = params.get("age", 65)
        gender = params.get("gender", "male")

        gfr = 175 * (creatinine**-1.154) * (age**-0.203)
        if gender.lower() == "female":
            gfr *= 0.742
        return f"Calculated GFR: {round(gfr, 2)} mL/min/1.73m²"

    return "Calculation type not supported"

# --- 2. CONFIGURE MODEL ---
model = AzureOpenAIModel(
    model_id="gpt-4o",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-05-01-preview")
)

# --- 3. CONFIGURE AGENT ---
agent = CodeAgent(
    tools=[medical_knowledge_retriever, clinical_calculator],
    model=model,
    sandbox=E2BExecutor(),  # Remote secure execution for GAIA tasks
    additional_authorized_imports=["pandas", "numpy", "scipy"],
    max_steps=10            # GAIA Level 1 usually needs ~5-10 steps
)

# --- 4. EXAMPLE USAGE ---
if __name__ == "__main__":
    # Example query
    response = agent.run("What is the treatment protocol for hypertension?")
    print(response)
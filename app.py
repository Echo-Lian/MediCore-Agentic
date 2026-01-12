import streamlit as st
from smolagents import CodeAgent, AzureOpenAIModel, E2BExecutor, tool
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- 1. PRO-GRADE MEDICAL TOOLS ---
@tool
def calculate_renal_function(creatinine: float, age: int, gender: str) -> str:
    """
    Calculates GFR (Glomerular Filtration Rate) to help with drug dosing.
    Args:
        creatinine: Serum creatinine in mg/dL.
        age: Patient age in years.
        gender: Patient gender ('male' or 'female').
    """
    # Example of complex logic an agent can call
    gfr = 175 * (creatinine**-1.154) * (age**-0.203)
    if gender.lower() == "female":
        gfr *= 0.742
    return f"Calculated GFR: {round(gfr, 2)} mL/min/1.73m². "

@tool
def get_clinical_guidelines(condition: str) -> str:
    """
    Retrieves official treatment protocols for a specific condition.
    Args:
        condition: The medical condition (e.g., 'Hypertension').
    """
    # In production, this would be a RAG query to a Vector Database
    return f"Protocol for {condition}: 1. Lifestyle changes, 2. First-line: ACE Inhibitors."

# --- 2. AGENT CONFIGURATION ---
model = AzureOpenAIModel(
    model_id="gpt-4o",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY")
)

agent = CodeAgent(
    tools=[calculate_renal_function, get_clinical_guidelines],
    model=model,
    sandbox=E2BExecutor(), # ESSENTIAL FOR SECURITY
    additional_authorized_imports=["pandas", "numpy"]
)

# --- 3. STREAMLIT INTERFACE ---
st.set_page_config(page_title="BCB Medical Assistant", page_icon="🩺")
st.title("🩺 Clinical Decision Support Agent")
st.markdown("---")

query = st.text_area("Enter Physician Request:", 
                    placeholder="e.g., 'A 65-year-old female has creatinine 1.2. Calculate her GFR and suggest hypertension protocol.'")

if st.button("Run Clinical Analysis"):
    with st.spinner("Agent is reasoning and executing secure code..."):
        # The agent performs multi-step reasoning:
        # 1. Calls calculate_renal_function
        # 2. Calls get_clinical_guidelines
        # 3. Synthesizes the final answer
        response = agent.run(query)
        
        st.subheader("Final Clinical Summary")
        st.success(response)
        
        with st.expander("View Agent's Reasoning Trace"):
            st.write(agent.logs) # Shows the exact steps taken
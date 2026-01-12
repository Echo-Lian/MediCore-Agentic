# MediCore-Agentic
Secure Decision Support System for Clinical Workflows

> **Quick Start**: New to this project? Check out [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide!

## Overview

**Objective**: Autonomous agent capable of solving complex clinical data tasks, achieving a 30%+ score on the GAIA Benchmark (General AI Assistants).

**Architecture**: Code-Action Agent using smolagents and Azure OpenAI (GPT-4o), enabling the agent to write and execute Python for medical calculations rather than relying on LLM intuition.

**Security**: Secure execution environment using E2B sandboxing, ensuring that generated code runs in an isolated VM to prevent data leakage - critical for healthcare IT.

**Tools**: Custom RAG tools for clinical guideline retrieval and automated form-filling logic using vector-based retrieval.

## Technical Stack

- **Brain**: Azure OpenAI (GPT-4o) for high-level reasoning
- **Framework**: smolagents for code-based tool use (critical for 30%+ GAIA scores)
- **Security**: E2BExecutor for remote, ephemeral sandboxing
- **Interface**: Streamlit for the user-facing web app
- **Data Processing**: pandas, numpy for medical calculations

## How the Agent Works

1. **Input**: Doctor enters a complex request (e.g., "Analyze these lab results and fill out the patient's discharge form")
2. **Reasoning**: GPT-4o analyzes the text and determines required actions (calculations, lookups, etc.)
3. **Action**: Agent writes Python code snippets and sends them to the E2B Sandbox for secure execution
4. **Observation**: Sandbox executes code and returns results (e.g., GFR: 55)
5. **Synthesis**: Agent combines calculated data with retrieved guidelines to provide structured answers

## Setup Instructions

### Prerequisites

- Python 3.8+
- Azure OpenAI account with GPT-4o access
- E2B API key (sign up at [https://e2b.dev](https://e2b.dev))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MediCore-Agentic
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv

   # On macOS/Linux:
   source .venv/bin/activate

   # On Windows:
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env

   # Edit .env with your actual credentials
   # Required values:
   # - AZURE_OPENAI_ENDPOINT: Your Azure OpenAI endpoint URL
   # - AZURE_OPENAI_KEY: Your Azure OpenAI API key
   # - E2B_API_KEY: Your E2B sandbox API key
   ```

### Getting API Keys

**Azure OpenAI**:
1. Go to [Azure Portal](https://portal.azure.com)
2. Create an Azure OpenAI resource
3. Deploy a GPT-4o model
4. Copy the endpoint and API key from "Keys and Endpoint" section

**E2B Sandbox**:
1. Visit [https://e2b.dev](https://e2b.dev)
2. Sign up for an account
3. Get your API key from the dashboard

## Usage

### Running the Streamlit Web App

Start the interactive medical assistant interface:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

**Example queries**:
- "A 65-year-old female has creatinine 1.2. Calculate her GFR and suggest hypertension protocol."
- "What are the treatment guidelines for Type 2 Diabetes?"
- "Calculate BMI for a patient who is 175cm tall and weighs 80kg"

### Running the CLI Agent

For direct agent interaction without the web interface:

```bash
python agent_arc.py
```

You can modify the query in [agent_arc.py:60](agent_arc.py#L60) to test different medical scenarios.

## Project Structure

```
MediCore-Agentic/
├── app.py                 # Streamlit web interface
├── agent_arc.py          # CLI agent implementation
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── .env                 # Your actual credentials (not in git)
└── README.md           # This file
```

## Key Features

### Medical Tools

1. **Renal Function Calculator**: Calculates GFR (Glomerular Filtration Rate) for drug dosing
2. **Clinical Guidelines Retriever**: Fetches treatment protocols for specific conditions
3. **Secure Code Execution**: All calculations run in isolated E2B sandbox

### Security Features

- **Sandboxed Execution**: Code runs in ephemeral VMs, not on host machine
- **No Data Leakage**: Isolated environment prevents access to local network
- **Healthcare Compliance**: Architecture designed for hospital IT requirements

## Why This Achieves 30%+ on GAIA

- **Code-Action**: CodeAgent can use pandas/numpy to handle large CSV/Excel files (GAIA Level 2/3)
- **Sandbox Isolation**: Agent can safely iterate, fail, and fix its own code
- **Multi-step Reasoning**: Combines calculations with knowledge retrieval

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'smolagents'`
- **Solution**: Make sure virtual environment is activated and run `pip install -r requirements.txt`

**Issue**: `Error: Azure OpenAI credentials not found`
- **Solution**: Check that `.env` file exists and contains valid credentials

**Issue**: `E2B API Error`
- **Solution**: Verify E2B API key is correct and account is active

## Development

To extend the agent with new medical tools:

1. Define a new tool function with `@tool` decorator
2. Add it to the `tools` list in agent initialization
3. Document the tool's purpose and parameters

Example:
```python
@tool
def calculate_bmi(weight_kg: float, height_m: float) -> str:
    """Calculates Body Mass Index"""
    bmi = weight_kg / (height_m ** 2)
    return f"BMI: {round(bmi, 2)}"
```

## License

This project is for educational and research purposes.
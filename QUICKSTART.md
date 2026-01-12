# Quick Start Guide

Get up and running with MediCore-Agentic in 5 minutes!

## Step 1: Clone and Setup

```bash
# Navigate to the project directory
cd MediCore-Agentic

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Configure API Keys

```bash
# Copy the example environment file
cp .env.example .env
```

Now edit the `.env` file with your actual credentials:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_KEY=your-actual-api-key-here
AZURE_OPENAI_API_VERSION=2024-05-01-preview
E2B_API_KEY=your-e2b-api-key-here
```

### Where to Get API Keys

**Azure OpenAI** (Required):
- Go to [Azure Portal](https://portal.azure.com)
- Create an Azure OpenAI resource
- Deploy GPT-4o model
- Copy endpoint and key from "Keys and Endpoint"

**E2B Sandbox** (Required):
- Visit [e2b.dev](https://e2b.dev)
- Sign up (free tier available)
- Copy API key from dashboard

## Step 3: Verify Setup

```bash
python verify_setup.py
```

You should see all checks pass:
```
✓ Dependencies: PASS
✓ Project Files: PASS
✓ Environment Configuration: PASS
```

## Step 4: Run the Application

### Option A: Web Interface (Recommended)

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

### Option B: CLI Agent

```bash
python agent_arc.py
```

Edit the query in `agent_arc.py` (line 60) to test different scenarios.

## Example Queries to Try

Once the app is running, try these medical queries:

1. **Renal Function**:
   ```
   A 65-year-old female has creatinine 1.2. Calculate her GFR and suggest hypertension protocol.
   ```

2. **Treatment Guidelines**:
   ```
   What are the first-line treatment options for Type 2 Diabetes?
   ```

3. **Complex Clinical Calculation**:
   ```
   Patient is 70 years old, male, creatinine 1.5 mg/dL.
   Calculate GFR and determine if dosage adjustment is needed for renal medications.
   ```

## Troubleshooting

### Issue: Dependencies won't install
```bash
# Make sure you're using Python 3.8+
python --version

# Upgrade pip
pip install --upgrade pip

# Try installing again
pip install -r requirements.txt
```

### Issue: "Module not found" error
```bash
# Make sure virtual environment is activated
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### Issue: API authentication errors
- Double-check your `.env` file exists and has correct values
- Make sure there are no spaces around the `=` signs
- Verify your Azure OpenAI deployment name matches "gpt-4o"

### Issue: E2B sandbox errors
- Verify your E2B API key is active
- Check your E2B account dashboard for any issues
- Ensure you have available sandbox credits

## Next Steps

- Read the full [README.md](README.md) for architecture details
- Explore [app.py](app.py) to understand the medical tools
- Customize tools in [agent_arc.py](agent_arc.py) for your use case
- Review the GAIA benchmark documentation to understand the agent's capabilities

## Need Help?

- Check the [README.md](README.md) troubleshooting section
- Review error messages carefully - they often indicate what's wrong
- Make sure all environment variables are correctly set
- Verify your API keys are active and have proper permissions

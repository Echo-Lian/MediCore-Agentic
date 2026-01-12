#!/usr/bin/env python3
"""
Verification script to check if the environment is properly set up.
Run this after installing dependencies to verify everything is configured.
"""
import sys
import os
from pathlib import Path

def check_dependencies():
    """Check if all required packages are installed."""
    print("Checking dependencies...")
    required_packages = [
        "smolagents",
        "openai",
        "e2b_code_interpreter",
        "streamlit",
        "pandas",
        "numpy",
        "dotenv"
    ]

    missing = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package} - MISSING")
            missing.append(package)

    return len(missing) == 0

def check_env_file():
    """Check if .env file exists and has required variables."""
    print("\nChecking environment configuration...")
    env_path = Path(".env")

    if not env_path.exists():
        print("  ✗ .env file not found")
        print("    → Run: cp .env.example .env")
        print("    → Then edit .env with your API keys")
        return False

    print("  ✓ .env file exists")

    # Load .env and check for required variables
    from dotenv import load_dotenv
    load_dotenv()

    required_vars = {
        "AZURE_OPENAI_ENDPOINT": os.getenv("AZURE_OPENAI_ENDPOINT"),
        "AZURE_OPENAI_KEY": os.getenv("AZURE_OPENAI_KEY"),
        "E2B_API_KEY": os.getenv("E2B_API_KEY")
    }

    all_set = True
    for var_name, var_value in required_vars.items():
        if not var_value or var_value.startswith("your-"):
            print(f"  ✗ {var_name} - NOT SET or using placeholder")
            all_set = False
        else:
            print(f"  ✓ {var_name} - configured")

    return all_set

def check_files():
    """Check if all required files exist."""
    print("\nChecking project files...")
    required_files = ["app.py", "agent_arc.py", "requirements.txt"]

    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} - MISSING")
            all_exist = False

    return all_exist

def main():
    print("=" * 60)
    print("MediCore-Agentic Setup Verification")
    print("=" * 60)

    checks = {
        "Dependencies": check_dependencies(),
        "Project Files": check_files(),
        "Environment Configuration": check_env_file()
    }

    print("\n" + "=" * 60)
    print("Summary:")
    print("=" * 60)

    all_passed = all(checks.values())

    for check_name, passed in checks.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{check_name}: {status}")

    if all_passed:
        print("\n✓ All checks passed! You're ready to run the application.")
        print("\nNext steps:")
        print("  1. Run the Streamlit app: streamlit run app.py")
        print("  2. Or run the CLI agent: python agent_arc.py")
    else:
        print("\n✗ Some checks failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()

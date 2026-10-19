
import subprocess
import sys
from pathlib import Path

# Locate the project folder
PROJECT_DIR = Path(__file__).resolve().parent
PYTHON = sys.executable

# Modules to run, in order
modules = [
    "src/sales_analytics.py",
    "src/business_insights.py",
]

print("\n===================================")
print("       VISIONMIND AI")
print("     RETAIL BUSINESS CO-PILOT")
print("===================================")

for module in modules:
    print(f"\nRunning {module}...\n")

    result = subprocess.run(
        [PYTHON, str(PROJECT_DIR / module)],
        cwd=PROJECT_DIR
    )

    if result.returncode != 0:
        print(f"\nError while running {module}.")
        sys.exit(result.returncode)

print("\n===================================")
print("VISIONMIND AI RUN COMPLETED!")
print("===================================")

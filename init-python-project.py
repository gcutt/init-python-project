import os
from pathlib import Path

# Common project folders
FOLDERS = ["data", "notebooks", "scripts", "src", "tests"]

# Requirements template
REQUIREMENTS = """# Project dependencies
#pathlib
#numpy
#pandas
#python-dateutil
#pytz
#scipy
"""

# Gitignore template (common Python ignores)
GITIGNORE = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*.pyo
*.pyd

# Virtual environments
.venv/
env/
venv/

# Distribution / packaging
build/
dist/
*.egg-info/

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Logs
*.log

# OS files
.DS_Store
Thumbs.db
"""

# Bash script for venv setup
BASH_SCRIPT = """#!/bin/bash
# Create local virtual environment in .venv
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
"""

# Windows batch script for venv setup
BAT_SCRIPT = """@echo off
REM Create local virtual environment in .venv
python3.12 -m venv .venv
call .venv\\Scripts\\activate
pip install --upgrade pip
pip install -r requirements.txt
"""

# Template for scripts/main.py
MAIN_SCRIPT = """def hello_world():
    \"\"\"Example function to demonstrate project structure.\"\"\"
    return "Hello, world!"

def main():
    message = hello_world()
    print(message)

if __name__ == "__main__":
    main()
"""

# Template for tests/test_main.py (using unittest)
TEST_SCRIPT = """import unittest
from src.main import hello_world

class TestMain(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
"""

def main():
    project_path_input = input("Enter the full path where you want to create the new project: ").strip()
    project_root = Path(project_path_input)

    project_root.mkdir(parents=True, exist_ok=False)
    print(f"Initializing project in: {project_root.resolve()}")

    # Create folders
    for folder in FOLDERS:
        path = project_root / folder
        path.mkdir(exist_ok=True)
        print(f"Created folder: {path}")

    # Create starter files
    (project_root / "scripts" / "main.py").write_text(MAIN_SCRIPT)
    print("Created scripts/main.py")

    (project_root / "tests" / "test_main.py").write_text(TEST_SCRIPT)
    print("Created tests/test_main.py")

    # Create requirements.txt
    (project_root / "requirements.txt").write_text(REQUIREMENTS)
    print("Created requirements.txt")

    # Create .gitignore
    (project_root / ".gitignore").write_text(GITIGNORE)
    print("Created .gitignore")

    # Create setup scripts
    (project_root / "setup_env.sh").write_text(BASH_SCRIPT)
    os.chmod(project_root / "setup_env.sh", 0o755)

    (project_root / "setup_env.bat").write_text(BAT_SCRIPT)
    print("Created setup_env.sh and setup_env.bat")

    print("✅ Project initialized successfully!")

if __name__ == "__main__":
    main()
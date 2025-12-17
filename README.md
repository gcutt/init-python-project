# init-python-project

A simple utility to **initialize a Python project folder** with a ready-to-use structure and virtual environment setup.

---

## 🚀 Features
- Creates a clean directory structure for new Python projects.
- Provides a starter template for organizing code and resources.
- Includes scripts to quickly set up a virtual environment (`venv`).
- Works across platforms (Windows `.bat` and Linux/macOS `.sh`).

---

## 📦 Getting Started

### 1. Run the Initialization Script
Execute the main script to start the setup:
```bash
python init-python-project.py
```

You will be prompted to enter the **full path** where the new project directory should be created.  
The script will generate a standard Python project template at that location.

---

### 2. Set Up the Virtual Environment
After the project folder is created, run the environment setup script:

- **Windows**
  ```bash
  setup_env.bat
  ```

- **Linux/macOS**
  ```bash
  ./setup_env.sh
  ```

This will create a `venv` named '.venv' inside your project directory.

---

### 3. Open in Your IDE
Once the environment is ready, you can create a new project in your preferred IDE (e.g., **PyCharm**, **VS Code**), set the interpreter to `my_project/.venv` and start coding right away.

---

## 📂 Example Project Structure
```
my_project/
├── .venv/                [created after running setup_env.*]
├── scripts/
│   └── main.py           [starter script]
├── src/
│   └── main.py           [optional, move main.py here if you want src logic, or place helpers here]
├── tests/
│   └── test_main.py      [starter test]
├── setup_env.bat
├── setup_env.sh
├── requirements.txt
└── README.md
```

> Note: The `.venv/` directory is automatically created when you run `setup_env.bat` (Windows) or `setup_env.sh` (Linux/macOS).

---

## License
```
This project is licensed under the GNU General Public License v3.0 (GPLv3).  
You are free to use, modify, and distribute this code, including for commercial purposes, provided that any derivative work is also licensed under GPLv3.  
See the license file for the full text.
```



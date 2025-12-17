@echo off
REM Create local virtual environment in .venv
python3.12 -m venv .venv
call .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

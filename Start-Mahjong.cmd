@echo off
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" p16mj.py
) else (
    py -3 p16mj.py
)
if errorlevel 1 pause

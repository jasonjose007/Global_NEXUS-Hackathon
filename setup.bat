@echo off
REM Setup Virtual Environment for Global NEXUS
echo Setting up Virtual Environment for Global NEXUS...

REM Check if .venv exists
if exist ".venv" (
    echo .venv already exists
) else (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -q flask

echo Setup complete! Virtual environment is ready.
echo To activate manually, run: .venv\Scripts\activate.bat
pause

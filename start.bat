@echo off
REM Start Flask Application
echo Starting Global NEXUS Medical Portal...

REM Check if .venv exists
if not exist ".venv" (
    echo Virtual environment not found. Please run setup.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Start Flask app
echo Flask app running at http://127.0.0.1:5000
echo Press Ctrl+C to stop the server
python app.py
pause

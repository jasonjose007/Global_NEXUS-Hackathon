# Start Flask Application
Write-Host "Starting Global NEXUS Medical Portal..." -ForegroundColor Green

# Check if .venv exists
if (-not (Test-Path ".venv")) {
    Write-Host "Virtual environment not found. Please run setup.ps1 first." -ForegroundColor Red
    exit 1
}

# Activate virtual environment
& ".\.venv\Scripts\Activate.ps1"

# Start Flask app
Write-Host "Flask app running at http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
python app.py

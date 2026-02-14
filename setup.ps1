# Setup Virtual Environment
Write-Host "Setting up Virtual Environment for Global NEXUS..." -ForegroundColor Green

# Check if .venv exists
if (Test-Path ".venv") {
    Write-Host ".venv already exists" -ForegroundColor Yellow
} else {
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv .venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
& ".\.venv\Scripts\Activate.ps1"

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Cyan
pip install -q flask

Write-Host "Setup complete! Virtual environment is ready." -ForegroundColor Green
Write-Host "To activate manually, run: .\.venv\Scripts\Activate.ps1" -ForegroundColor Gray

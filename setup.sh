#!/bin/bash
# Setup Virtual Environment for Global NEXUS

echo "Setting up Virtual Environment for Global NEXUS..."

# Check if venv exists
if [ -d "venv" ]; then
    echo "venv already exists"
else
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q flask

echo "Setup complete! Virtual environment is ready."
echo "To activate manually, run: source venv/bin/activate"

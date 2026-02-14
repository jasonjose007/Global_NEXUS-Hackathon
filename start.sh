#!/bin/bash
# Start Flask Application for Global NEXUS

echo "Starting Global NEXUS Medical Portal..."

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Please run setup.sh first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Start Flask app
echo "Flask app running at http://127.0.0.1:5000"
echo "Press Ctrl+C to stop the server"
python app.py

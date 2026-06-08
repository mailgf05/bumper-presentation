#!/bin/bash

# Bumper Mission Book Presentation Launcher
# IFAG Bachelor RAC - Jury Presentation

echo "🚀 Starting Bumper Mission Book Presentation..."
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Change to the presentation directory
cd "$(dirname "$0")"

# Start HTTP server
echo "📡 Starting HTTP server on port 8080..."
echo "🌐 Open your browser to: http://localhost:8080/bumper-presentation.html"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 -m http.server 8080
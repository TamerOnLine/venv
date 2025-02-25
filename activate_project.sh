#!/bin/bash
set -e  # Stop execution on error

# Navigate to the script directory
cd "$(dirname "$0")" || exit
PROJECT_DIR="$(pwd)"

echo " Setting up the project in: $PROJECT_DIR"

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo " Python3 is not installed! Please install Python 3.6+."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c "import sys; print(sys.version_info[:2])" 2>/dev/null)
if [[ "$PYTHON_VERSION" < "(3, 6)" ]]; then
    echo " Python 3.6+ is required!"
    exit 1
fi

# Create virtual environment if not exists
if [ ! -d "$PROJECT_DIR/venv" ]; then
    echo " Creating virtual environment..."
    python3 -m venv "$PROJECT_DIR/venv"

    if [ ! -d "$PROJECT_DIR/venv" ]; then
        echo " Failed to create virtual environment!"
        exit 1
    fi
fi

# Activate virtual environment
echo " Activating virtual environment..."
source "$PROJECT_DIR/venv/bin/activate"

# Upgrade pip
echo " Updating pip..."
if ! pip install --upgrade pip; then
    echo " Failed to update pip!"
    exit 1
fi

echo " Environment is ready!"

# Keep the terminal open
exec "$SHELL"

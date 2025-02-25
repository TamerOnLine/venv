# Set Project Directory Automatically
$PROJECT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -Path $PROJECT_DIR

# Ensure Python is Installed
if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host " Python is not installed! Please install Python and try again." -ForegroundColor Red
    exit 1
}

# Check and Create Virtual Environment if Not Exists
if (-Not (Test-Path "$PROJECT_DIR\venv")) {
    Write-Host " Creating virtual environment..." -ForegroundColor Yellow
    python -m venv "$PROJECT_DIR\venv"
    
    if (-Not (Test-Path "$PROJECT_DIR\venv")) {
        Write-Host " Failed to create virtual environment!" -ForegroundColor Red
        exit 1
    }
}

# Activate Virtual Environment
Write-Host " Activating virtual environment..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-File `"$PROJECT_DIR\venv\Scripts\Activate.ps1`""

Write-Host " Environment is ready!" -ForegroundColor Green

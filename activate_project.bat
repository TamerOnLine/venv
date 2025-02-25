@echo off
setlocal

:: Move to the script directory
cd /d "%~dp0"
set "PROJECT_DIR=%CD%"

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo  Python is not installed!
    exit /b 1
)

:: Create virtual environment if not present
if not exist "%PROJECT_DIR%\venv" (
    echo  Creating virtual environment...
    python -m venv "%PROJECT_DIR%\venv"
    if %errorlevel% neq 0 (
        echo  Failed to create virtual environment!
        exit /b 1
    )
)

:: Activate virtual environment
call "%PROJECT_DIR%\venv\Scripts\activate"
if %errorlevel% neq 0 (
    echo  Failed to activate virtual environment!
    exit /b 1
)

echo  Environment is ready!

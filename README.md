# tameronline-agent

## Overview
`tameronline-agent` is a lightweight and automated environment setup script designed to streamline the process of creating and activating a virtual environment across different operating systems (Windows, Linux, and macOS). This project ensures that Python dependencies are properly managed and integrated with your development workflow.

## Features
- **Cross-Platform Support**: Works seamlessly on Windows (`.bat`, `.ps1`), Linux (`.sh`), and macOS (`.sh`).
- **Automated Virtual Environment Setup**: Detects Python installation, creates a virtual environment, and activates it.
- **Pip Package Management**: Ensures the latest version of pip and installs dependencies from `requirements.txt`.
- **Integrated with VS Code**: Provides a `.code-workspace` file for one-click environment activation in Visual Studio Code.

## Installation
### Prerequisites
- **Python 3.6+** must be installed.
- **VS Code (optional)** for an integrated development experience.

### Setup Instructions
#### Windows
**Using Command Prompt:**
```cmd
cd path/to/tameronline-agent
activate_project.bat
```
**Using PowerShell:**
```powershell
cd path/to/tameronline-agent
.\activate_project.ps1
```

#### Linux/macOS
```bash
cd path/to/tameronline-agent
chmod +x activate_project.sh
./activate_project.sh
```

## Cloning the Project
To clone the `tameronline-agent` repository to your local machine, follow these steps:

### **1. Ensure Git is Installed**
Check if Git is installed by running:
```bash
git --version
```
If not installed, download and install it from [Git Official Website](https://git-scm.com/).

### **2. Clone the Repository**
Open a terminal or command prompt and execute:
```bash
git clone https://github.com/TamerOnLine/tameronline-agent.git
```
For SSH access:
```bash
git clone git@github.com:TamerOnLine/tameronline-agent.git
```

### **3. Navigate into the Project Directory**
```bash
cd tameronline-agent
```

### **4. Setup the Virtual Environment**
#### **Windows (Command Prompt)**
```cmd
activate_project.bat
```
#### **Windows (PowerShell)**
```powershell
.\activate_project.ps1
```
#### **Linux/macOS**
```bash
chmod +x activate_project.sh
./activate_project.sh
```

### **5. Install Dependencies**
After activating the virtual environment, install the required dependencies:
```bash
pip install -r requirements.txt
```

## File Structure
```
tameronline-agent/
├── README.md                # Documentation
├── activate_project.bat     # Windows CMD script
├── activate_project.ps1     # Windows PowerShell script
├── activate_project.sh      # Linux/macOS Bash script
├── requirements.txt         # List of dependencies
└── workspace.code-workspace # VS Code workspace file
```

## Usage
### Activating the Virtual Environment
After running the respective script for your OS, your terminal will enter the virtual environment. You can confirm this by checking your prompt:
```bash
(venv) user@machine:~/tameronline-agent$
```

### Installing Dependencies
Once the virtual environment is active, install the required dependencies:
```bash
pip install -r requirements.txt
```

### Deactivating the Virtual Environment
To exit the virtual environment, simply run:
```bash
deactivate
```

## Troubleshooting
- **Python Not Found Error**: Ensure Python 3.6+ is installed and available in the system path.
- **Virtual Environment Activation Fails**: Delete the `venv` folder and rerun the activation script.
- **Permission Issues on macOS/Linux**: Run `chmod +x activate_project.sh` to grant execution permissions.

## Contribution
Feel free to submit pull requests or report issues on the [GitHub repository](https://github.com/TamerOnLine/tameronline-agent).

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.


import os

# Define the scripts directory
SCRIPTS_DIR = "tests"

# Fetch all Python scripts dynamically
scripts = {
    str(index): os.path.join(SCRIPTS_DIR, file)
    for index, file in enumerate(os.listdir(SCRIPTS_DIR))
    if file.endswith(".py")
}

# Display available script options
print("Select the script you want to run:\n")
for key, script in scripts.items():
    print(f"{key}. {script}")

# Get user input
choice = input("\nEnter the number of the script to execute: ").strip()

# Execute the selected script
if choice in scripts:
    script_to_run = scripts[choice]
    print(f"\n🔹 Running {script_to_run}...\n")
    os.system(f"python {script_to_run}")
else:
    print("\n Invalid choice. Please select a valid number.")

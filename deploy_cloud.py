import os
import subprocess
import sys

def run_command(command, error_message):
    """Run a system command and check for errors."""
    process = subprocess.run(command, shell=True, text=True)
    if process.returncode != 0:
        print(f"❌ {error_message}")
        sys.exit(1)

# Step 1: Check if Git is installed
print("🚀 Checking for Git installation...")
try:
    subprocess.run("git --version", shell=True, check=True, text=True)
except subprocess.CalledProcessError:
    print("❌ Git is not installed. Please install Git from https://git-scm.com/")
    sys.exit(1)

# Step 2: Initialize Git repository if not already initialized
if not os.path.exists(".git"):
    print("📦 Initializing Git repository...")
    run_command("git init", "Failed to initialize Git repository.")

# Step 3: Add remote GitHub repository
GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"
REPO_NAME = "AccessibleChess"
REMOTE_URL = f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"

print("🔗 Adding GitHub repository...")
run_command(f"git remote add origin {REMOTE_URL}", "Failed to add GitHub repository.")

# Step 4: Commit and push changes
print("📤 Committing and pushing code to GitHub...")
run_command("git add .", "Failed to add files.")
run_command('git commit -m "Deploying chess app"', "Failed to commit changes.")
run_command("git branch -M main", "Failed to set branch.")
run_command("git push -u origin main", "Failed to push code to GitHub.")

print("✅ Deployment complete! Your app is now on GitHub.")

#!/usr/bin/env python3
"""
Heroku deployment script for the humanizer app
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e}")
        print(f"Error output: {e.stderr}")
        return False

def deploy_to_heroku():
    """Deploy the humanizer app to Heroku"""
    
    print("🚀 Deploying Humanizer App to Heroku")
    print("=" * 50)
    
    # Check if Heroku CLI is installed
    if not run_command("heroku --version", "Checking Heroku CLI"):
        print("❌ Please install Heroku CLI first: https://devcenter.heroku.com/articles/heroku-cli")
        return False
    
    # Check if logged in to Heroku
    if not run_command("heroku auth:whoami", "Checking Heroku login"):
        print("❌ Please login to Heroku: heroku login")
        return False
    
    # Initialize Git repository if not already done
    if not os.path.exists(".git"):
        if not run_command("git init", "Initializing Git repository"):
            return False
    
    # Add all files to Git
    if not run_command("git add .", "Adding files to Git"):
        return False
    
    # Commit changes
    if not run_command('git commit -m "Deploy humanizer app to production"', "Committing changes"):
        return False
    
    # Create Heroku app
    app_name = input("📝 Enter your Heroku app name (or press Enter for random name): ").strip()
    if app_name:
        if not run_command(f"heroku create {app_name}", f"Creating Heroku app '{app_name}'"):
            return False
    else:
        if not run_command("heroku create", "Creating Heroku app with random name"):
            return False
    
    # Push to Heroku
    if not run_command("git push heroku main", "Deploying to Heroku"):
        return False
    
    # Open the deployed app
    if run_command("heroku open", "Opening deployed app"):
        print("🎉 Your humanizer app is now live!")
        return True
    
    return False

if __name__ == "__main__":
    if deploy_to_heroku():
        print("\n✅ Deployment successful!")
        print("🌐 Your humanizer is now publicly accessible!")
    else:
        print("\n❌ Deployment failed!")
        print("🔧 Please check the error messages above and try again.")

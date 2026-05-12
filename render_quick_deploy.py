#!/usr/bin/env python3
"""
Render deployment helper for humanizer app
"""

import subprocess
import sys
import os
import webbrowser

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

def check_git_status():
    """Check if Git is initialized and files are committed"""
    if not os.path.exists(".git"):
        print("❌ Git repository not initialized")
        return False
    
    # Check if there are uncommitted changes
    try:
        result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
        if result.stdout.strip():
            print("❌ There are uncommitted changes")
            return False
        return True
    except:
        return False

def deploy_to_render():
    """Guide user through Render deployment"""
    
    print("🚀 Render Deployment Guide for Humanizer App")
    print("=" * 60)
    
    # Step 1: Check Git status
    print("\n📋 Step 1: Check Git Repository")
    if not check_git_status():
        print("\n🔧 Fixing Git repository...")
        
        # Initialize Git if needed
        if not os.path.exists(".git"):
            if not run_command("git init", "Initializing Git repository"):
                return False
        
        # Add all files
        if not run_command("git add .", "Adding files to Git"):
            return False
        
        # Commit changes
        if not run_command('git commit -m "Add humanizer app for Render deployment"', "Committing changes"):
            return False
        
        print("✅ Git repository ready!")
    else:
        print("✅ Git repository is ready!")
    
    # Step 2: Check if GitHub remote exists
    print("\n📋 Step 2: Check GitHub Repository")
    try:
        result = subprocess.run("git remote -v", shell=True, capture_output=True, text=True)
        if "origin" not in result.stdout:
            print("❌ No GitHub remote found")
            print("\n🔧 Please create a GitHub repository first:")
            print("1. Go to https://github.com/new")
            print("2. Create a new repository named 'humanizer'")
            print("3. Copy the repository URL")
            print("4. Run: git remote add origin YOUR_REPO_URL")
            print("5. Run: git push -u origin main")
            return False
        else:
            print("✅ GitHub remote found!")
    except:
        print("❌ Could not check Git remotes")
        return False
    
    # Step 3: Push to GitHub
    print("\n📋 Step 3: Push to GitHub")
    if not run_command("git push origin main", "Pushing to GitHub"):
        print("❌ Failed to push to GitHub")
        return False
    
    # Step 4: Open Render
    print("\n📋 Step 4: Deploy to Render")
    print("🌐 Opening Render dashboard...")
    
    try:
        webbrowser.open("https://dashboard.render.com/")
        print("✅ Render dashboard opened in browser")
    except:
        print("❌ Could not open browser automatically")
        print("🌐 Please manually open: https://dashboard.render.com/")
    
    print("\n📝 Render Deployment Instructions:")
    print("1. Click 'New +' button")
    print("2. Select 'Web Service'")
    print("3. Connect your GitHub repository")
    print("4. Configure:")
    print("   - Name: humanizer-app")
    print("   - Environment: Python 3")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: gunicorn app_production:app")
    print("   - Instance Type: Free")
    print("5. Click 'Create Web Service'")
    print("6. Wait for deployment (2-5 minutes)")
    print("7. Your app will be live at: https://humanizer-app.onrender.com")
    
    print("\n🎯 After deployment, test your app at:")
    print("🌐 Web Interface: https://humanizer-app.onrender.com")
    print("🔌 API: https://humanizer-app.onrender.com/api/enhanced-humanize")
    print("❤️  Health: https://humanizer-app.onrender.com/health")
    
    return True

if __name__ == "__main__":
    if deploy_to_render():
        print("\n✅ Render deployment guide completed!")
        print("🎉 Follow the instructions above to deploy your app!")
    else:
        print("\n❌ Deployment setup failed!")
        print("🔧 Please fix the issues above and try again.")

#!/usr/bin/env python3
"""
Force Render redeploy with cache-busting changes
"""

import subprocess
import sys
import os

def main():
    print("🔄 Force Render Redeploy")
    print("=" * 40)
    print("📝 Adding cache-busting changes to force fresh deployment")
    print("=" * 40)
    
    try:
        # Add cache-busting timestamp to requirements
        with open('requirements_render.txt', 'a') as f:
            f.write(f"\n# Cache-busting: {datetime.now().isoformat()}")
        
        # Commit and push changes
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Add cache-busting for fresh Render deployment'], check=True)
        subprocess.run(['git', 'push', 'origin', 'master'], check=True)
        
        print("✅ Changes pushed to GitHub")
        print("🌐 Render should now redeploy with latest version")
        print("📝 New endpoints added:")
        print("   /api/version - Check app version")
        print("   /api/clear-cache - Clear Render cache")
        print("=" * 40)
        print("🎯 Next steps:")
        print("1. Go to Render dashboard")
        print("2. Check deployment logs")
        print("3. Test /api/version endpoint")
        print("4. Call /api/clear-cache if needed")
        print("5. Test formatting preservation")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    from datetime import datetime
    main()

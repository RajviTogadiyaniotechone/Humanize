#!/usr/bin/env python3
"""
Force Render update with aggressive cache-busting
"""

import subprocess
import sys
import os
from datetime import datetime

def main():
    print("🔄 Force Render Update - Aggressive Cache-Busting")
    print("=" * 60)
    print("📝 Creating multiple cache-busting changes")
    print("=" * 60)
    
    try:
        # Add aggressive cache-busting changes
        with open('requirements_render.txt', 'a') as f:
            f.write(f"\n# AGGRESSIVE CACHE-BUSTING: {datetime.now().isoformat()}")
            f.write(f"\n# FORCE UPDATE: v2.1.0-{datetime.now().strftime('%Y%m%d%H%M%S')}")
        
        # Update app_render.py with timestamp
        with open('app_render.py', 'r') as f:
            content = f.read()
        
        # Add timestamp to force update
        timestamp_comment = f"\n# CACHE-BUSTING TIMESTAMP: {datetime.now().isoformat()}\n"
        content = content.replace("from word_replacement_humanizer import WordReplacementHumanizer", 
                                 f"# CACHE-BUSTING TIMESTAMP: {datetime.now().isoformat()}\nfrom word_replacement_humanizer import WordReplacementHumanizer")
        
        with open('app_render.py', 'w') as f:
            f.write(content)
        
        # Commit and push changes
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 
                       f'AGGRESSIVE CACHE-BUSTING v2.1.0 - Force Render update {datetime.now().strftime("%Y%m%d%H%M%S")}'], 
                       check=True)
        subprocess.run(['git', 'push', 'origin', 'master'], check=True)
        
        print("✅ Aggressive cache-busting changes pushed")
        print("🌐 Render should now force update with latest code")
        print("=" * 60)
        print("🎯 New Features Added:")
        print("   ✅ Version 2.1.0 with aggressive cache-busting")
        print("   ✅ Debug endpoint: /api/debug-formatting")
        print("   ✅ Enhanced version endpoint: /api/version")
        print("   ✅ Commit hash tracking")
        print("   ✅ Format method verification")
        print("=" * 60)
        print("🎯 Next Steps:")
        print("1. Manual deploy from Render dashboard")
        print("2. Test /api/version - should show 2.1.0")
        print("3. Test /api/debug-formatting with newlines")
        print("4. Verify formatting preservation works")
        print("=" * 60)
        print("📝 Test Commands:")
        print(f"curl https://your-url.onrender.com/api/version")
        print(f"curl -X POST https://your-url.onrender.com/api/debug-formatting \\")
        print(f"  -H 'Content-Type: application/json' \\")
        print(f"  -d '{{\"text\":\"Good morning.\\n\\nHow   are   you?\\n\\nI hope you are well.\"}}'")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

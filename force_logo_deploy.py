#!/usr/bin/env python3
"""
Force logo deployment to Render
"""

import subprocess
import sys
from datetime import datetime

def force_logo_deployment():
    """Force logo deployment with aggressive cache-busting"""
    
    print("🔄 Force Logo Deployment")
    print("=" * 50)
    print("📝 Aggressive cache-busting for logo deployment")
    print("=" * 50)
    
    try:
        # Add timestamp to force deployment
        with open('requirements_render.txt', 'a') as f:
            f.write(f"\n# LOGO DEPLOYMENT FORCE: {datetime.now().isoformat()}")
        
        # Update focused_index.html with logo
        with open('templates/focused_index.html', 'r') as f:
            content = f.read()
        
        # Ensure logo is present
        if 'fa-brain' not in content:
            print("❌ Logo not found in HTML - adding it")
            logo_html = '''                <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow-lg mr-4">
                    <i class="fas fa-brain text-3xl gradient-text"></i>
                </div>'''
            
            # Replace old icon section
            old_icon = '''                <i class="fas fa-magic mr-2"></i>'''
            content = content.replace(old_icon, logo_html)
            
            with open('templates/focused_index.html', 'w') as f:
                f.write(content)
        
        # Commit and push
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 
                       f'FORCE LOGO DEPLOYMENT v3.1.0 - {datetime.now().strftime("%Y%m%d%H%M%S")}'], 
                       check=True)
        subprocess.run(['git', 'push', 'origin', 'master'], check=True)
        
        print("✅ Logo deployment forced")
        print("🌐 Render should deploy with logo")
        print("=" * 50)
        print("🎯 Next Steps:")
        print("1. Check Render dashboard for deployment")
        print("2. Test logo display in browser")
        print("3. Verify Font Awesome loads")
        print("4. Check browser console")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    force_logo_deployment()

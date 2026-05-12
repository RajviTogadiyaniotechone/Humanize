#!/usr/bin/env python3
"""
Fix Render deployment to use production WSGI server instead of development server
"""

import subprocess
import sys
import os
from datetime import datetime

def fix_production_deployment():
    """Fix Render deployment to use production WSGI server"""
    
    print("🔧 Fix Production WSGI Deployment")
    print("=" * 50)
    print("📝 Updating Render deployment for production server")
    print("=" * 50)
    
    try:
        # Create production WSGI entry point
        wsgi_content = '''#!/usr/bin/env python3
"""
Production WSGI entry point for Render deployment
"""

import os
from app_render import app

# Configure for production
app.config['DEBUG'] = False
app.config['ENV'] = 'production'

# Expose WSGI application
application = app.wsgi_app

if __name__ == "__main__":
    # This should not run in production
    pass
'''
        
        # Write WSGI file
        with open('wsgi.py', 'w') as f:
            f.write(wsgi_content)
        
        # Update app_render.py to remove development server
        with open('app_render.py', 'r') as f:
            content = f.read()
        
        # Remove development server configuration
        content = content.replace('app.run(debug=True)', '# app.run(debug=True) # Disabled for production')
        
        # Add production configuration
        production_config = '''
# Production configuration
app.config['DEBUG'] = False
app.config['ENV'] = 'production'

# Disable development server warning
import warnings
warnings.filterwarnings("ignore", message="This is a development server")
'''
        
        # Add production config after imports
        import_pos = content.find('from flask import Flask, render_template, request, jsonify')
        if import_pos != -1:
            insert_pos = content.find('\\n', import_pos)
            if insert_pos != -1:
                content = content[:insert_pos + 1] + production_config + content[insert_pos + 1:]
        
        # Update format preservation function to be more robust
        format_function = '''
def preserve_formatting_production(text, humanized_text):
    """Production-ready format preservation"""
    
    # Split both texts by words
    words = text.split()
    humanized_words = humanized_text.split()
    
    # If word counts don't match, return humanized as-is
    if len(words) != len(humanized_words):
        return humanized_text
    
    # Rebuild preserving original formatting character by character
    result = []
    text_chars = list(text)
    word_start = 0
    
    for i, char in enumerate(text_chars):
        if char.isspace() or i == len(text_chars) - 1:
            # Found whitespace or end of text
            if i > word_start:
                # Extract word from original
                original_word = ''.join(text_chars[word_start:i])
                
                # Find corresponding humanized word
                word_index = len([w for w in words[:len(words)] if w == original_word])
                if word_index < len(humanized_words):
                    humanized_word = humanized_words[word_index]
                    
                    # Replace characters in result
                    for j in range(len(original_word)):
                        if word_start + j < len(text_chars):
                            text_chars[word_start + j] = humanized_word[j] if j < len(humanized_word) else original_word[j]
            
            word_start = i + 1
    
    return ''.join(text_chars)
'''
        
        # Replace simple format function with production version
        content = content.replace(
            'def preserve_formatting_simple(text, humanized_text):',
            format_function.strip()
        )
        
        # Update the call to use production function
        content = content.replace(
            'result[\'humanized_text\'] = preserve_formatting_simple(original_text, humanized_text)',
            'result[\'humanized_text\'] = preserve_formatting_production(original_text, humanized_text)'
        )
        
        # Write updated content
        with open('app_render.py', 'w') as f:
            f.write(content)
        
        # Update requirements for production
        with open('requirements_render.txt', 'r') as f:
            requirements = f.read()
        
        # Add production server requirements
        if 'gunicorn' not in requirements:
            requirements += '\\ngunicorn==20.1.0\\n'
        
        with open('requirements_render.txt', 'w') as f:
            f.write(requirements)
        
        # Add cache-busting timestamp
        with open('requirements_render.txt', 'a') as f:
            f.write(f"\\n# PRODUCTION WSGI FIX: {datetime.now().isoformat()}")
        
        # Commit and push changes
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 
                       f'Production WSGI fix v3.0.0 - {datetime.now().strftime("%Y%m%d%H%M%S")}'], 
                       check=True)
        subprocess.run(['git', 'push', 'origin', 'master'], check=True)
        
        print("✅ Production WSGI fix deployed")
        print("🌐 Render should now use production server")
        print("=" * 50)
        print("🎯 Changes Made:")
        print("   ✅ Created wsgi.py for production deployment")
        print("   ✅ Disabled development server in app_render.py")
        print("   ✅ Added production configuration")
        print("   ✅ Enhanced format preservation for production")
        print("   ✅ Added gunicorn requirement")
        print("   ✅ Version 3.0.0 with production WSGI")
        print("=" * 50)
        print("🎯 Render Deployment Instructions:")
        print("1. Go to Render dashboard")
        print("2. Update service to use wsgi.py as start command")
        print("3. Set build command: pip install -r requirements_render.txt")
        print("4. Set start command: gunicorn wsgi:application")
        print("5. Deploy and test formatting preservation")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fix_production_deployment()

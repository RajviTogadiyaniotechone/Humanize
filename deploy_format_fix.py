#!/usr/bin/env python3
"""
Deploy format fix to Render - minimal changes
"""

import subprocess
import sys
import os
from datetime import datetime

def preserve_formatting_simple(text, humanized_text):
    """Simple format preservation that works with deployed logic"""
    
    # Split both texts by words
    words = text.split()
    humanized_words = humanized_text.split()
    
    # If word counts don't match, return humanized as-is
    if len(words) != len(humanized_words):
        return humanized_text
    
    # Rebuild preserving original formatting
    result = text
    
    # Replace each word while preserving exact whitespace
    for i, (orig_word, human_word) in enumerate(zip(words, humanized_words)):
        if orig_word != human_word:
            # Use simple string replace to preserve formatting
            result = result.replace(orig_word, human_word, 1)  # Only replace first occurrence
    
    return result

def update_deployed_app():
    """Update deployed app with format preservation fix"""
    
    print("🔄 Deploy Format Fix to Render")
    print("=" * 50)
    print("📝 Adding simple format preservation to deployed app")
    print("=" * 50)
    
    try:
        # Read current app_render.py
        with open('app_render.py', 'r') as f:
            content = f.read()
        
        # Find the word replacement function and add format preservation
        format_preservation_code = '''
def preserve_formatting_simple(text, humanized_text):
    """Simple format preservation that works with deployed logic"""
    
    # Split both texts by words
    words = text.split()
    humanized_words = humanized_text.split()
    
    # If word counts don't match, return humanized as-is
    if len(words) != len(humanized_words):
        return humanized_text
    
    # Rebuild preserving original formatting
    result = text
    
    # Replace each word while preserving exact whitespace
    for i, (orig_word, human_word) in enumerate(zip(words, humanized_words)):
        if orig_word != human_word:
            # Use simple string replace to preserve formatting
            result = result.replace(orig_word, human_word, 1)  # Only replace first occurrence
    
    return result

'''
        
        # Add format preservation function after imports
        import_pos = content.find('from word_replacement_humanizer import WordReplacementHumanizer')
        if import_pos != -1:
            content = content[:import_pos] + format_preservation_code + content[import_pos:]
        
        # Update the word replacement call to use format preservation
        old_call = 'result = humanizer.word_replacement_humanize(text, intensity)'
        new_call = '''result = humanizer.word_replacement_humanize(text, intensity)
        
        # Apply format preservation to maintain newlines and spaces
        if result['success']:
            original_text = text
            humanized_text = result['humanized_text']
            result['humanized_text'] = preserve_formatting_simple(original_text, humanized_text)'''
        
        content = content.replace(old_call, new_call)
        
        # Write updated content back
        with open('app_render.py', 'w') as f:
            f.write(content)
        
        # Add cache-busting timestamp
        with open('requirements_render.txt', 'a') as f:
            f.write(f"\n# FORMAT FIX DEPLOYMENT: {datetime.now().isoformat()}")
        
        # Commit and push changes
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 
                       f'Deploy format preservation fix v2.2.0 - {datetime.now().strftime("%Y%m%d%H%M%S")}'], 
                       check=True)
        subprocess.run(['git', 'push', 'origin', 'master'], check=True)
        
        print("✅ Format preservation fix deployed")
        print("🌐 Render should now preserve newlines and spaces")
        print("=" * 50)
        print("🎯 Changes Made:")
        print("   ✅ Added simple format preservation function")
        print("   ✅ Updated word replacement to preserve formatting")
        print("   ✅ Minimal changes to existing logic")
        print("   ✅ Version 2.2.0 with format fix")
        print("=" * 50)
        print("🎯 Next Steps:")
        print("1. Manual deploy from Render dashboard")
        print("2. Test with newlines and spaces")
        print("3. Verify formatting is preserved")
        print("4. Check browser console for errors")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    update_deployed_app()

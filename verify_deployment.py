#!/usr/bin/env python3
"""
Verify deployed app formatting preservation
"""

import requests
import json

def test_deployment():
    """Test deployed app to verify formatting preservation"""
    
    print("🔍 Verifying Deployment")
    print("=" * 40)
    print("📝 Testing deployed app formatting preservation")
    print("=" * 40)
    
    # Test with newlines - the main issue
    test_text = "Good morning.\n\nHow   are   you?\n\nI hope you are well."
    
    print(f"📝 Input: {repr(test_text)}")
    print(f"📊 Expected newlines: {test_text.count('\\n')}")
    print(f"📊 Expected spaces: {test_text.count('  ')}")
    
    try:
        # Test your actual deployed app (replace with your URL)
        response = requests.post(
            "https://your-actual-render-url.onrender.com/api/enhanced-humanize",
            json={
                "text": test_text,
                "focused_mode": True,
                "intensity": 0.7
            },
            headers={
                "Content-Type": "application/json"
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"📝 Output: {repr(data.get('humanized_text', 'Error'))}")
            
            # Check formatting preservation
            output_text = data.get('humanized_text', '')
            output_newlines = output_text.count('\\n')
            output_spaces = output_text.count('  ')
            
            print(f"📊 Actual newlines: {output_newlines}")
            print(f"📊 Actual spaces: {output_spaces}")
            
            if test_text.count('\\n') == output_newlines:
                print("✅ Newlines preserved!")
            else:
                print("❌ Newlines NOT preserved!")
                
            if test_text.count('  ') == output_spaces:
                print("✅ Spaces preserved!")
            else:
                print("❌ Spaces NOT preserved!")
                
            # Check version
            version = data.get('version', 'Unknown')
            print(f"🔢 App version: {version}")
            
        else:
            print(f"❌ Request failed: {response.status_code}")
            if response.text:
                print(f"📝 Error response: {response.text}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n🎯 Verification Complete!")
    print("📝 Replace 'your-actual-render-url' with your actual Render URL")
    print("✨ This will help identify the exact issue")

if __name__ == "__main__":
    test_deployment()

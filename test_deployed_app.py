#!/usr/bin/env python3
"""
Test deployed app to verify formatting preservation
"""

import requests
import json

def test_deployed_app():
    """Test the deployed app to verify formatting preservation"""
    
    print("🔍 Testing Deployed App")
    print("=" * 40)
    print("📝 Checking if deployed app uses latest version")
    print("=" * 40)
    
    # Test URL (replace with your actual Render URL)
    render_url = "https://your-app-name.onrender.com"  # Replace this
    
    # Test cases with formatting
    test_cases = [
        {
            "name": "Multiple spaces test",
            "text": "Good    morning   everyone."
        },
        {
            "name": "New line test", 
            "text": "Good morning.\nHow are you today?"
        },
        {
            "name": "Mixed formatting test",
            "text": "Good morning.\n\nHow   are   you?\n\nI hope you're   well."
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test_case['name']}")
        print(f"Input: {repr(test_case['text'])}")
        
        try:
            response = requests.post(
                f"{render_url}/api/enhanced-humanize",
                json={
                    "text": test_case['text'],
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
                print(f"Output: {repr(data.get('humanized_text', 'Error'))}")
                
                # Check formatting preservation
                original_newlines = test_case['text'].count('\n')
                humanized_newlines = data.get('humanized_text', '').count('\n')
                
                original_spaces = test_case['text'].count('  ')
                humanized_spaces = data.get('humanized_text', '').count('  ')
                
                print(f"📊 Formatting Analysis:")
                print(f"   Newlines: {original_newlines} → {humanized_newlines} {'✅' if original_newlines == humanized_newlines else '❌'}")
                print(f"   Spaces: {original_spaces} → {humanized_spaces} {'✅' if original_spaces == humanized_spaces else '❌'}")
                
                if (original_spaces == humanized_spaces and 
                    (original_newlines == humanized_newlines or original_newlines == 0)):
                    print("✅ Formatting preserved correctly!")
                else:
                    print("⚠️  Formatting not fully preserved")
                    
            else:
                print(f"❌ Request failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print(f"\n🎯 Test Complete!")
    print("📝 Update render_url in this script with your actual Render URL")
    print("✨ This will help identify if deployed app is using latest version")

if __name__ == "__main__":
    test_deployed_app()

#!/usr/bin/env python3
"""
Check what's actually deployed on Render
"""

import requests
import json

def check_deployed_app():
    """Check deployed app endpoints and version"""
    
    print("🔍 Checking Deployed App Version")
    print("=" * 50)
    print("📝 URL: https://ai-humanizer-1jea.onrender.com")
    print("=" * 50)
    
    base_url = "https://ai-humanizer-1jea.onrender.com"
    
    # Test endpoints that should exist in latest version
    endpoints_to_test = [
        ("/api/version", "GET", None),
        ("/api/enhanced-humanize", "POST", {
            "text": "Good morning.\n\nHow   are   you?\n\nI hope you are well.",
            "focused_mode": True,
            "intensity": 0.7
        }),
        ("/", "GET", None),
        ("/api/clear-cache", "POST", None),
        ("/api/debug-formatting", "POST", {
            "text": "Good morning.\n\nHow   are   you?\n\nI hope you are well."
        })
    ]
    
    for endpoint, method, data in endpoints_to_test:
        print(f"\n🌐 Testing: {method} {endpoint}")
        
        try:
            if method == "GET":
                response = requests.get(f"{base_url}{endpoint}", timeout=10)
            else:
                response = requests.post(
                    f"{base_url}{endpoint}",
                    json=data,
                    headers={"Content-Type": "application/json"},
                    timeout=10
                )
            
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    result = response.json()
                    if endpoint == "/api/version":
                        print(f"   ✅ Version: {result.get('version', 'Unknown')}")
                        print(f"   ✅ Features: {result.get('features', [])}")
                    elif endpoint == "/api/enhanced-humanize":
                        output_text = result.get('humanized_text', '')
                        print(f"   ✅ Output: {repr(output_text)}")
                        print(f"   ✅ Newlines in output: {output_text.count('\\n')}")
                    elif endpoint == "/api/debug-formatting":
                        print(f"   ✅ Debug data available")
                        debug_info = result.get('debug_info', {})
                        preservation = debug_info.get('preservation', {})
                        print(f"   ✅ Newlines preserved: {preservation.get('newlines_preserved', False)}")
                except:
                    print("   ✅ Response received (not JSON)")
            elif response.status_code == 404:
                print("   ❌ 404 Not Found - Endpoint not available")
                print("   📝 This suggests old version is deployed")
            else:
                print(f"   ⚠️  Error: {response.status_code}")
                if response.text:
                    print(f"   📝 Response: {response.text[:200]}...")
                    
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Network error: {e}")
        except Exception as e:
            print(f"   ❌ Unexpected error: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Analysis:")
    print("   If all endpoints return 404, old version is deployed")
    print("   If /api/version works but shows old version, cache issue")
    print("   If /api/enhanced-humanize works but no newlines, logic issue")
    print("=" * 50)
    print("📝 Solution:")
    print("   1. Manual deploy from Render dashboard")
    print("   2. Check deployment logs for errors")
    print("   3. Verify latest commit is being used")
    print("   4. Clear browser cache and test again")

if __name__ == "__main__":
    check_deployed_app()

#!/usr/bin/env python3
"""
Debug why logo isn't appearing on Render web URL
"""

import requests
import json

def debug_logo_issue():
    """Debug logo display issues on Render"""
    
    print("🔍 Debug Logo Issue on Render")
    print("=" * 50)
    print("📝 Checking deployed app for logo display")
    print("=" * 50)
    
    base_url = "https://ai-humanizer-1jea.onrender.com"
    
    # Test endpoints to check deployment status
    tests = [
        ("GET", "/api/version", "Check version and deployment"),
        ("GET", "/", "Check main page HTML"),
        ("POST", "/api/enhanced-humanize", "Test API functionality")
    ]
    
    for method, endpoint, description in tests:
        print(f"\n🌐 Testing: {method} {endpoint}")
        print(f"   Purpose: {description}")
        
        try:
            if method == "GET":
                response = requests.get(f"{base_url}{endpoint}", timeout=10)
            else:
                response = requests.post(
                    f"{base_url}{endpoint}",
                    json={
                        "text": "Good morning.\n\nHow   are   you?\n\nI hope you are well.",
                        "focused_mode": True,
                        "intensity": 0.7
                    },
                    headers={"Content-Type": "application/json"},
                    timeout=10
                )
            
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                if endpoint == "/":
                    # Check if logo HTML is present
                    html_content = response.text
                    if "fa-brain" in html_content:
                        print("   ✅ Logo icon found in HTML")
                    else:
                        print("   ❌ Logo icon NOT found in HTML")
                    
                    if "w-16 h-16 bg-white rounded-full" in html_content:
                        print("   ✅ Logo styling found in HTML")
                    else:
                        print("   ❌ Logo styling NOT found in HTML")
                    
                    if "fas fa-magic" in html_content:
                        print("   ✅ Old icon still present")
                    else:
                        print("   ✅ Old icon removed")
                        
                elif endpoint == "/api/version":
                    try:
                        data = response.json()
                        print(f"   ✅ Version: {data.get('version', 'Unknown')}")
                        print(f"   ✅ Features: {data.get('features', [])}")
                    except:
                        print("   ✅ Version endpoint working (JSON parse error)")
                        
                else:
                    print("   ✅ API endpoint working")
                    
            else:
                print(f"   ❌ Error: {response.status_code}")
                if response.text:
                    print(f"   📝 Response: {response.text[:200]}...")
                    
        except Exception as e:
            print(f"   ❌ Network error: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Possible Logo Issues:")
    print("   1. Font Awesome not loading on Render")
    print("   2. CSS not applied properly")
    print("   3. Old version still deployed")
    print("   4. CDN blocked on Render")
    print("   5. Caching issues")
    print("=" * 50)
    print("📝 Solutions:")
    print("   1. Check Render deployment logs")
    print("   2. Verify latest commit is deployed")
    print("   3. Test Font Awesome CDN loading")
    print("   4. Check browser console for errors")
    print("   5. Clear browser cache")
    print("   6. Try manual redeploy from dashboard")

if __name__ == "__main__":
    debug_logo_issue()

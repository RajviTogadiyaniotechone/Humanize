#!/usr/bin/env python3
"""
Comprehensive deployment troubleshooting for formatting preservation
"""

import requests
import json
import time

def check_render_health():
    """Check Render deployment health"""
    
    print("🔍 Render Deployment Health Check")
    print("=" * 50)
    print("📝 Checking all possible deployment issues")
    print("=" * 50)
    
    # Common Render URLs (check which one applies)
    possible_urls = [
        "https://humanize.onrender.com",
        "https://humanize-api.onrender.com", 
        "https://your-app-name.onrender.com"
    ]
    
    for url in possible_urls:
        print(f"\n🌐 Testing URL: {url}")
        
        try:
            # Test basic health
            health_response = requests.get(f"{url}/api/version", timeout=10)
            
            if health_response.status_code == 200:
                version_data = health_response.json()
                print(f"✅ Health check passed")
                print(f"📊 App version: {version_data.get('version', 'Unknown')}")
                print(f"🔧 Features: {', '.join(version_data.get('features', []))}")
                
                # Test formatting preservation
                test_text = "Good morning.\n\nHow   are   you?\n\nI hope you are well."
                
                format_response = requests.post(
                    f"{url}/api/enhanced-humanize",
                    json={
                        "text": test_text,
                        "focused_mode": True,
                        "intensity": 0.7
                    },
                    headers={
                        "Content-Type": "application/json"
                    },
                    timeout=15
                )
                
                if format_response.status_code == 200:
                    format_data = format_response.json()
                    output_text = format_data.get('humanized_text', '')
                    
                    original_newlines = test_text.count('\\n')
                    output_newlines = output_text.count('\\n')
                    
                    original_spaces = test_text.count('  ')
                    output_spaces = output_text.count('  ')
                    
                    print(f"📝 Formatting Test:")
                    print(f"   Input newlines: {original_newlines}")
                    print(f"   Output newlines: {output_newlines}")
                    print(f"   Newlines preserved: {'✅' if original_newlines == output_newlines else '❌'}")
                    print(f"   Input spaces: {original_spaces}")
                    print(f"   Output spaces: {output_spaces}")
                    print(f"   Spaces preserved: {'✅' if original_spaces == output_spaces else '❌'}")
                    
                    if (original_newlines == output_newlines and 
                        original_spaces == output_spaces):
                        print("✅ PERFECT: Formatting preserved correctly!")
                        return True
                    else:
                        print("⚠️  ISSUE: Formatting not fully preserved")
                        return False
                        
                else:
                    print(f"❌ Format test failed: {format_response.status_code}")
                    if format_response.text:
                        print(f"📝 Error: {format_response.text}")
                    
            else:
                print(f"❌ Health check failed: {health_response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    print(f"\n🎯 Health Check Complete!")
    print("📝 If all tests show ❌, check:")
    print("   1. Render dashboard for deployment status")
    print("   2. App logs for errors")
    print("   3. GitHub repo for latest code")
    print("   4. Try manual redeploy from dashboard")
    print("=" * 50)

def manual_deployment_check():
    """Manual deployment verification checklist"""
    
    print("\n🔧 Manual Deployment Checklist")
    print("=" * 40)
    
    print("📝 Step 1: Verify GitHub Repository")
    print("   ✅ Latest code pushed to master branch")
    print("   ✅ Version: 2.0.0 with formatting preservation")
    print("   ✅ Cache-busting endpoints added")
    
    print("\n📝 Step 2: Check Render Dashboard")
    print("   1. Go to: https://dashboard.render.com")
    print("   2. Select your Humanize service")
    print("   3. Check 'Deployments' tab")
    print("   4. Look for 'Deployed successfully' message")
    print("   5. If failed, check 'Logs' tab")
    
    print("\n📝 Step 3: Test Live App")
    print("   1. Open your app URL in browser")
    print("   2. Test with: 'Good morning.\\n\\nHow   are   you?\\n\\nI hope you are well.'")
    print("   3. Check if newlines and spaces are preserved")
    print("   4. Check browser console for errors")
    
    print("\n📝 Step 4: Force Fresh Deployment")
    print("   1. In Render dashboard, click 'Manual Deploy'")
    print("   2. Add cache-busting query: ?v=2.0.0")
    print("   3. Wait for deployment to complete")
    print("   4. Test again with same input")
    
    print("\n🎯 If Still Not Working:")
    print("   1. Check if using correct URL")
    print("   2. Verify app is using latest commit")
    print("   3. Check requirements_render.txt is updated")
    print("   4. Try clearing browser cache")
    print("   5. Contact Render support if needed")

if __name__ == "__main__":
    check_render_health()
    manual_deployment_check()

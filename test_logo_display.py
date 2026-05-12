#!/usr/bin/env python3
"""
Test logo display in browser
"""

import subprocess
import webbrowser
import time

def test_logo_display():
    """Test logo display in browser"""
    
    print("🧪 Testing Logo Display")
    print("=" * 40)
    print("📝 Opening app in browser to test logo")
    print("=" * 40)
    
    try:
        # Start local server
        print("🚀 Starting local Flask server...")
        server_process = subprocess.Popen(
            ['python', 'app_render.py'],
            cwd='y:\\D Drive\\Rajvi_python\\N8N\\Humanize',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for server to start
        time.sleep(3)
        
        # Open browser
        url = "http://127.0.0.1:5000"
        print(f"🌐 Opening: {url}")
        webbrowser.open(url)
        
        print("✅ Logo should now be visible!")
        print("📝 Check for:")
        print("   - White circular logo with brain icon")
        print("   - Gradient text effect on icon")
        print("   - Proper alignment with title")
        print("   - Shadow effect on logo")
        print("=" * 40)
        print("🎯 Logo Features:")
        print("   ✅ Brain icon (fas fa-brain)")
        print("   ✅ Gradient text effect")
        print("   ✅ White background circle")
        print("   ✅ Shadow effect")
        print("   ✅ Responsive sizing")
        print("   ✅ Proper spacing")
        print("=" * 40)
        print("📝 Press Ctrl+C to stop server")
        
        # Keep server running
        try:
            server_process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")
            server_process.terminate()
    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_logo_display()

#!/usr/bin/env python3
"""
Test formatting preservation in word replacement humanizer
"""

from word_replacement_humanizer import WordReplacementHumanizer

def test_formatting_preservation():
    """Test that new lines and spaces are preserved"""
    
    print("🔄 Testing Formatting Preservation")
    print("=" * 50)
    print("📝 Testing new lines and spaces preservation")
    print("=" * 50)
    
    humanizer = WordReplacementHumanizer()
    
    # Test cases with various formatting
    test_cases = [
        {
            "name": "Simple sentence",
            "text": "Good morning everyone."
        },
        {
            "name": "Multiple spaces",
            "text": "Good    morning   everyone."
        },
        {
            "name": "New line",
            "text": "Good morning.\nHow are you today?"
        },
        {
            "name": "Multiple new lines",
            "text": "Good morning.\n\nHow are you?\n\nI hope you're well."
        },
        {
            "name": "Mixed formatting",
            "text": "Good morning.\n\nHow   are   you?\n\nI hope you're   well."
        },
        {
            "name": "Tabs and spaces",
            "text": "Good morning.\t\tHow are you?\n\nI hope you're well."
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test_case['name']}")
        print(f"Original: {repr(test_case['text'])}")
        
        result = humanizer.word_replacement_humanize(test_case['text'], intensity=0.7)
        
        if result['success']:
            print(f"Humanized: {repr(result['humanized_text'])}")
            
            # Check if formatting is preserved
            original_newlines = test_case['text'].count('\n')
            humanized_newlines = result['humanized_text'].count('\n')
            
            original_spaces = test_case['text'].count('  ')
            humanized_spaces = result['humanized_text'].count('  ')
            
            original_tabs = test_case['text'].count('\t')
            humanized_tabs = result['humanized_text'].count('\t')
            
            print(f"📊 Formatting Check:")
            print(f"   New lines: {original_newlines} → {humanized_newlines} {'✅' if original_newlines == humanized_newlines else '❌'}")
            print(f"   Multiple spaces: {original_spaces} → {humanized_spaces} {'✅' if original_spaces == humanized_spaces else '❌'}")
            print(f"   Tabs: {original_tabs} → {humanized_tabs} {'✅' if original_tabs == humanized_tabs else '❌'}")
            
            if (original_newlines == humanized_newlines and 
                original_spaces == humanized_spaces and 
                original_tabs == humanized_tabs):
                print("✅ Formatting preserved perfectly!")
            else:
                print("⚠️  Formatting not fully preserved")
                
        else:
            print(f"❌ Error: {result['error']}")
        
        print("-" * 50)
    
    print("\n🎯 Formatting Preservation Test Complete!")
    print("✨ Ready to verify new lines and spaces are maintained!")

if __name__ == "__main__":
    test_formatting_preservation()

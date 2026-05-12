#!/usr/bin/env python3
"""
Debug Render app to check formatting preservation
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from word_replacement_humanizer import WordReplacementHumanizer

def test_formatting_preservation():
    """Test formatting preservation with debug output"""
    
    print("🔍 Debug: Testing Formatting Preservation")
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
            
            # Detailed formatting analysis
            original_newlines = test_case['text'].count('\n')
            humanized_newlines = result['humanized_text'].count('\n')
            
            original_spaces = test_case['text'].count('  ')
            humanized_spaces = result['humanized_text'].count('  ')
            
            original_tabs = test_case['text'].count('\t')
            humanized_tabs = result['humanized_text'].count('\t')
            
            print(f"📊 Detailed Analysis:")
            print(f"   Original newlines: {original_newlines}")
            print(f"   Humanized newlines: {humanized_newlines}")
            print(f"   Newlines preserved: {original_newlines == humanized_newlines}")
            print(f"   Original spaces: {original_spaces}")
            print(f"   Humanized spaces: {humanized_spaces}")
            print(f"   Spaces preserved: {original_spaces == humanized_spaces}")
            print(f"   Original tabs: {original_tabs}")
            print(f"   Humanized tabs: {humanized_tabs}")
            print(f"   Tabs preserved: {original_tabs == humanized_tabs}")
            
            # Check character-by-character comparison
            if len(test_case['text']) == len(result['humanized_text']):
                chars_match = all(test_case['text'][i] == result['humanized_text'][i] 
                                  for i in range(len(test_case['text'])))
                print(f"   Characters match: {chars_match}")
            
        else:
            print(f"❌ Error: {result['error']}")
        
        print("-" * 50)
    
    print("\n🎯 Debug Test Complete!")
    print("✨ Use this to verify formatting preservation behavior")

if __name__ == "__main__":
    test_formatting_preservation()

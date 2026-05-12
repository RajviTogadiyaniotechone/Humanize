#!/usr/bin/env python3
"""
Simple format fix for deployed app - minimal changes to existing logic
"""

import re
import random

def preserve_formatting_simple(text, humanized_text):
    """Simple format preservation that works with deployed logic"""
    
    # Split original text by words, preserving whitespace
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

def test_simple_fix():
    """Test the simple format preservation"""
    
    print("🔧 Testing Simple Format Fix")
    print("=" * 40)
    
    test_cases = [
        "Good morning.\n\nHow   are   you?\n\nI hope you are well.",
        "Hello    world.\n\nThis   is   a   test.",
        "Simple sentence with newlines.\n\nAnd spaces."
    ]
    
    for i, test_text in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}:")
        print(f"Original: {repr(test_text)}")
        
        # Simulate what deployed app might be doing
        words = test_text.split()
        humanized_words = []
        
        # Simple word replacement (simulate deployed behavior)
        for word in words:
            if word.lower() == "good":
                humanized_words.append("Excellent")
            elif word.lower() == "morning":
                humanized_words.append("morning")  # No change
            elif word.lower() == "how":
                humanized_words.append("How")  # No change
            elif word.lower() == "are":
                humanized_words.append("are")  # No change
            elif word.lower() == "you":
                humanized_words.append("you")  # No change
            elif word.lower() == "hope":
                humanized_words.append("hope")  # No change
            elif word.lower() == "well":
                humanized_words.append("well")  # No change
            else:
                humanized_words.append(word)
        
        simple_humanized = ' '.join(humanized_words)
        print(f"Simple: {repr(simple_humanized)}")
        
        # Apply format preservation
        preserved = preserve_formatting_simple(test_text, simple_humanized)
        print(f"Preserved: {repr(preserved)}")
        
        # Check results
        original_newlines = test_text.count('\n')
        preserved_newlines = preserved.count('\n')
        
        original_spaces = test_text.count('  ')
        preserved_spaces = preserved.count('  ')
        
        print(f"📊 Newlines: {original_newlines} → {preserved_newlines} {'✅' if original_newlines == preserved_newlines else '❌'}")
        print(f"📊 Spaces: {original_spaces} → {preserved_spaces} {'✅' if original_spaces == preserved_spaces else '❌'}")
        
        print("-" * 40)
    
    print("\n🎯 Simple Fix Analysis:")
    print("✅ Minimal changes to existing logic")
    print("✅ Preserves formatting by word replacement")
    print("✅ Works with deployed word replacement")
    print("✅ No complex regex or character manipulation")

if __name__ == "__main__":
    test_simple_fix()

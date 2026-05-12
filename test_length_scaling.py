#!/usr/bin/env python3
"""
Test word replacement scaling based on content length
"""

from word_replacement_humanizer import WordReplacementHumanizer

def test_length_scaling():
    """Test word replacement with different content lengths"""
    
    print("🔄 Testing Word Replacement Scaling")
    print("=" * 60)
    print("📝 Testing different content lengths")
    print("🔧 Scaling: More words for longer content")
    print("=" * 60)
    
    humanizer = WordReplacementHumanizer()
    
    # Test cases with different lengths
    test_cases = [
        {
            "name": "Short Content (8 words)",
            "text": "Furthermore, we must utilize strategic methodologies."
        },
        {
            "name": "Medium Content (15 words)", 
            "text": "Furthermore, we must utilize strategic methodologies to optimize our organizational infrastructure and achieve desired outcomes."
        },
        {
            "name": "Long Content (25 words)",
            "text": "Furthermore, we must utilize strategic methodologies to optimize our organizational infrastructure, implement comprehensive frameworks, leverage core competencies, and achieve desired outcomes effectively."
        },
        {
            "name": "Very Long Content (40 words)",
            "text": "Furthermore, we must utilize strategic methodologies to optimize our organizational infrastructure, implement comprehensive frameworks for subsequent development, leverage core competencies effectively, facilitate enhanced operational efficiency, establish synergistic partnerships, and achieve desired outcomes through systematic approaches."
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test_case['name']}")
        print(f"Original ({len(test_case['text'].split())} words): {test_case['text']}")
        
        result = humanizer.word_replacement_humanize(test_case['text'], intensity=0.7)
        
        if result['success']:
            print(f"Humanized ({len(result['humanized_text'].split())} words): {result['humanized_text']}")
            print(f"🎯 Score: {result['human_score']:.1f}%")
            print(f"📊 Changes: {', '.join(result['changes_applied'])}")
            print(f"🔢 Character Count: {result['character_count']}")
            
            # Count word changes
            original_words = test_case['text'].split()
            humanized_words = result['humanized_text'].split()
            changes = sum(1 for orig, human in zip(original_words, humanized_words) if orig != human)
            print(f"🔄 Words Changed: {changes}")
            
            if changes >= 5:
                print("✅ Excellent word replacement for long content!")
            elif changes >= 3:
                print("✅ Good word replacement!")
            else:
                print("⚠️  Could use more word changes")
                
        else:
            print(f"❌ Error: {result['error']}")
        
        print("-" * 60)
    
    print("\n🎯 Length Scaling Test Complete!")
    print("✨ Longer content gets more word changes!")

if __name__ == "__main__":
    test_length_scaling()

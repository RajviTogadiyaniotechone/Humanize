#!/usr/bin/env python3
"""
Test built-in synonym libraries for Python
Compare NLTK WordNet, spaCy, and TextBlob for synonym generation
"""

import nltk
from nltk.corpus import wordnet as wn
import spacy
from textblob import Word
import random

# Download required NLTK data
try:
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)
except:
    pass

def test_nltk_wordnet():
    """Test NLTK WordNet for synonyms"""
    print("🔍 Testing NLTK WordNet")
    print("=" * 40)
    
    test_words = ["good", "bad", "big", "small", "fast", "slow", "important", "utilize", "furthermore"]
    
    for word in test_words:
        synonyms = []
        for syn in wn.synsets(word):
            for lemma in syn.lemmas():
                synonym = lemma.name().replace('_', ' ')
                if synonym != word and synonym not in synonyms:
                    synonyms.append(synonym)
        
        print(f"📝 '{word}': {len(synonyms)} synonyms - {synonyms[:5]}")
    
    print()

def test_spacy_similarity():
    """Test spaCy for word similarity"""
    print("🔍 Testing spaCy Word Similarity")
    print("=" * 40)
    
    try:
        nlp = spacy.load("en_core_web_sm")
        test_words = ["good", "bad", "big", "small", "fast", "slow", "important", "utilize", "furthermore"]
        
        for word in test_words:
            word_token = nlp(word)
            similar_words = []
            
            # Test similarity with common words
            common_words = ["great", "terrible", "large", "tiny", "quick", "sluggish", "crucial", "use", "also"]
            
            for common_word in common_words:
                common_token = nlp(common_word)
                similarity = word_token.similarity(common_token)
                if similarity > 0.6:  # High similarity threshold
                    similar_words.append((common_word, similarity))
            
            # Sort by similarity score
            similar_words.sort(key=lambda x: x[1], reverse=True)
            top_similar = [word for word, score in similar_words[:3]]
            scores = [f"{score:.2f}" for word, score in similar_words[:3]]
            
            print(f"📝 '{word}': {len(similar_words)} similar - {top_similar} ({scores})")
    
    except Exception as e:
        print(f"❌ spaCy error: {e}")
    
    print()

def test_textblob_synonyms():
    """Test TextBlob for synonyms"""
    print("🔍 Testing TextBlob Synonyms")
    print("=" * 40)
    
    test_words = ["good", "bad", "big", "small", "fast", "slow", "important", "utilize", "furthermore"]
    
    for word in test_words:
        try:
            word_obj = Word(word)
            synonyms = word_obj.synsets
            
            if synonyms:
                # Get synonyms from first synset
                first_synset = synonyms[0]
                synonym_names = [lemma.name() for lemma in first_synset.lemmas()]
                synonym_names = [name.replace('_', ' ') for name in synonym_names if name != word]
                
                print(f"📝 '{word}': {len(synonym_names)} synonyms - {synonym_names[:5]}")
            else:
                print(f"📝 '{word}': No synonyms found")
        except Exception as e:
            print(f"📝 '{word}': Error - {e}")
    
    print()

def get_nltk_synonyms(word, max_synonyms=5):
    """Get synonyms using NLTK WordNet"""
    synonyms = []
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            synonym = lemma.name().replace('_', ' ')
            if synonym != word and synonym not in synonyms:
                synonyms.append(synonym)
                if len(synonyms) >= max_synonyms:
                    break
        if len(synonyms) >= max_synonyms:
            break
    return synonyms

def test_comprehensive_coverage():
    """Test comprehensive coverage of all libraries"""
    print("🔍 Testing Comprehensive Coverage")
    print("=" * 40)
    
    # Test with a variety of words
    test_words = [
        "good", "excellent", "wonderful", "great", "amazing",
        "bad", "terrible", "awful", "horrible", "poor",
        "big", "large", "huge", "enormous", "massive",
        "small", "tiny", "little", "minor", "petite",
        "fast", "quick", "rapid", "swift", "speedy",
        "slow", "sluggish", "gradual", "leisurely", "unhurried",
        "important", "crucial", "vital", "essential", "significant",
        "utilize", "use", "apply", "employ", "work with",
        "furthermore", "moreover", "additionally", "also", "plus"
    ]
    
    nltk_count = 0
    textblob_count = 0
    
    for word in test_words:
        # Test NLTK
        nltk_syns = get_nltk_synonyms(word)
        if nltk_syns:
            nltk_count += 1
        
        # Test TextBlob
        try:
            word_obj = Word(word)
            textblob_syns = word_obj.synsets
            if textblob_syns:
                textblob_count += 1
        except:
            pass
    
    print(f"📊 NLTK WordNet: {nltk_count}/{len(test_words)} words have synonyms ({nltk_count/len(test_words)*100:.1f}%)")
    print(f"📊 TextBlob: {textblob_count}/{len(test_words)} words have synonyms ({textblob_count/len(test_words)*100:.1f}%)")
    
    # Test some specific examples
    print("\n🎯 Example Synonyms:")
    examples = ["utilize", "furthermore", "important", "good", "big"]
    
    for word in examples:
        nltk_syns = get_nltk_synonyms(word, 3)
        print(f"📝 '{word}': NLTK - {nltk_syns}")
        
        # Test TextBlob
        try:
            word_obj = Word(word)
            textblob_syns = word_obj.synsets
            if textblob_syns:
                first_synset = textblob_syns[0]
                synonym_names = [lemma.name() for lemma in first_synset.lemmas()]
                synonym_names = [name.replace('_', ' ') for name in synonym_names if name != word]
                print(f"📝 '{word}': TextBlob - {synonym_names[:3]}")
        except:
            print(f"📝 '{word}': TextBlob - Error")

def compare_performance():
    """Compare performance of different approaches"""
    print("🔍 Performance Comparison")
    print("=" * 40)
    
    import time
    
    test_word = "good"
    iterations = 100
    
    # Test NLTK WordNet
    start_time = time.time()
    for _ in range(iterations):
        get_nltk_synonyms(test_word)
    nltk_time = time.time() - start_time
    
    # Test manual dictionary lookup
    from comprehensive_synonyms import get_comprehensive_synonyms
    manual_dict = get_comprehensive_synonyms()
    
    start_time = time.time()
    for _ in range(iterations):
        manual_dict.get(test_word, [])
    manual_time = time.time() - start_time
    
    print(f"📊 NLTK WordNet: {nltk_time:.4f}s for {iterations} lookups")
    print(f"📊 Manual Dictionary: {manual_time:.4f}s for {iterations} lookups")
    print(f"📊 Speed Ratio: {nltk_time/manual_time:.1f}x (NLTK vs Manual)")

if __name__ == "__main__":
    print("🔄 Testing Built-in Synonym Libraries")
    print("=" * 60)
    print("🔍 Comparing NLTK WordNet, spaCy, and TextBlob")
    print("=" * 60)
    
    test_nltk_wordnet()
    test_spacy_similarity()
    test_textblob_synonyms()
    test_comprehensive_coverage()
    compare_performance()
    
    print("\n🎯 Library Testing Complete!")
    print("✨ Ready to choose the best approach!")

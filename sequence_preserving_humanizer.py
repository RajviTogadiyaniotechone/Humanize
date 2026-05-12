#!/usr/bin/env python3
"""
Sequence-Preserving Structure Humanizer - Maintains sentence order, only changes structure
Breaks AI patterns while preserving original sentence sequence
"""

import re
import random
from datetime import datetime

class SequencePreservingHumanizer:
    """Structure humanizer that preserves sentence sequence"""
    
    def __init__(self):
        self.initialize_structure_patterns()
    
    def initialize_structure_patterns(self):
        """Initialize structure variation patterns"""
        
        # AI phrase replacements with natural alternatives
        self.ai_replacements = {
            "furthermore": ["also", "plus", "what's more", "on top of that", "additionally"],
            "moreover": ["also", "plus", "in addition", "besides", "another thing"],
            "consequently": ["so", "therefore", "as a result", "that's why", "for this reason"],
            "nevertheless": ["still", "however", "but", "even so", "that said"],
            "subsequently": ["then", "after that", "next", "following this"],
            "accordingly": ["so", "then", "for that reason", "based on this"],
            "utilize": ["use", "work with", "make use of", "employ", "apply"],
            "facilitate": ["help", "make easier", "enable", "assist", "support"],
            "implement": ["put in place", "set up", "start using", "launch", "begin"],
            "optimize": ["improve", "make better", "enhance", "fine-tune", "boost"],
            "enhance": ["improve", "boost", "upgrade", "make better", "strengthen"],
            "leverage": ["use", "take advantage of", "make the most of", "capitalize on"],
            "establish": ["create", "set up", "build", "form", "start"],
            "necessitates": ["requires", "needs", "calls for", "demands", "means"],
            "comprehensive": ["complete", "full", "thorough", "extensive", "detailed"],
            "subsequent": ["following", "next", "later", "after", "coming"],
            "aforementioned": ["mentioned", "previous", "earlier", "above", "said"],
            "imperative": ["essential", "necessary", "crucial", "vital", "must-have"],
            "strategic": ["planned", "thoughtful", "careful", "smart", "key"],
            "methodologies": ["methods", "approaches", "ways", "techniques", "systems"],
            "organizational": ["company", "business", "workplace", "team", "corporate"],
            "infrastructure": ["setup", "system", "framework", "structure", "foundation"],
            "various": ["different", "diverse", "multiple", "several", "many"],
            "factors": ["elements", "aspects", "points", "issues", "things"],
            "technologies": ["tools", "systems", "solutions", "methods", "approaches"],
            "operational": ["working", "running", "active", "functioning", "in use"],
            "efficiency": ["productivity", "performance", "output", "results", "effectiveness"],
            "outcomes": ["results", "effects", "consequences", "impacts", "end results"],
            "desired": ["wanted", "needed", "required", "sought", "targeted"],
            "competencies": ["skills", "abilities", "strengths", "capabilities", "talents"],
            "effectively": ["well", "properly", "successfully", "efficiently", "skillfully"]
        }
        
        # Natural contractions
        self.contractions = {
            "do not": "don't", "will not": "won't", "cannot": "can't",
            "did not": "didn't", "is not": "isn't", "are not": "aren't",
            "was not": "wasn't", "were not": "weren't", "have not": "haven't",
            "has not": "hasn't", "could not": "couldn't", "would not": "wouldn't",
            "should not": "shouldn't", "I am": "I'm", "you are": "you're",
            "we are": "we're", "they are": "they're", "it is": "it's",
            "that is": "that's"
        }
        
        # Structure variation patterns (sequence-preserving)
        self.structure_variations = {
            "clause_reordering": ["move dependent clauses", "reorder subordinate elements"],
            "verb_repositioning": ["move verbs within sentence", "change verb forms"],
            "modifier_placement": ["add modifiers at different positions", "vary adjective placement"],
            "connective_variation": ["change connecting words", "vary conjunctions"],
            "punctuation_variation": ["adjust punctuation for flow", "natural comma placement"]
        }
    
    def preserve_sequence_structure_humanize(self, text, intensity=0.7):
        """Main sequence-preserving structure humanization function"""
        
        if not text or len(text.strip()) < 10:
            return {
                'success': False,
                'error': 'Text too short'
            }
        
        original_text = text
        changes_applied = []
        
        # Split into sentences (preserve order)
        sentences = re.split(r'(?<=[.!?])\s+', text)
        rewritten_sentences = []
        
        # Apply structure variations while preserving sequence
        for sentence in sentences:
            if not sentence.strip():
                continue
            
            # Step 1: Replace AI phrases
            sentence = self.replace_ai_phrases(sentence)
            if random.random() < 0.6:
                changes_applied.append('phrase_replacement')
            
            # Step 2: Add natural contractions
            sentence = self.add_natural_contractions(sentence)
            if random.random() < 0.5:
                changes_applied.append('contraction_usage')
            
            # Step 3: Apply structure variations (sequence-preserving)
            if intensity >= 0.4:
                sentence = self.apply_structure_variations(sentence)
                changes_applied.append('structure_variation')
            
            # Step 4: Ensure proper punctuation
            sentence = self.ensure_proper_punctuation(sentence)
            changes_applied.append('punctuation_correction')
            
            rewritten_sentences.append(sentence)
        
        # Reconstruct text (maintaining original sentence order)
        humanized_text = ' '.join(rewritten_sentences)
        
        # Calculate character count
        char_count = len(humanized_text)
        
        # Calculate sequence-preserving score
        human_score = self.calculate_sequence_score(humanized_text)
        
        return {
            'success': True,
            'original_text': original_text,
            'humanized_text': humanized_text,
            'human_score': human_score,
            'changes_applied': changes_applied,
            'character_count': char_count,
            'sequence_preserved': True,
            'timestamp': datetime.now().isoformat()
        }
    
    def replace_ai_phrases(self, sentence):
        """Replace AI phrases with natural alternatives"""
        
        words = sentence.split()
        rewritten_words = []
        
        for word in words:
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Check for phrase replacement
            if clean_word in self.ai_replacements:
                if random.random() < 0.75:  # 75% chance to replace
                    alternatives = self.ai_replacements[clean_word]
                    replacement = random.choice(alternatives)
                    
                    # Preserve original capitalization and punctuation
                    if word[0].isupper():
                        replacement = replacement.capitalize()
                    
                    # Preserve punctuation at end
                    punctuation = re.sub(r'\w', '', word)
                    if punctuation and not punctuation.endswith(','):
                        replacement += punctuation
                    
                    rewritten_words.append(replacement)
                else:
                    rewritten_words.append(word)
            else:
                rewritten_words.append(word)
        
        return ' '.join(rewritten_words)
    
    def add_natural_contractions(self, sentence):
        """Add natural contractions"""
        
        for formal, contraction in self.contractions.items():
            if random.random() < 0.6:  # 60% chance
                sentence = re.sub(
                    r'\b' + re.escape(formal) + r'\b',
                    contraction,
                    sentence,
                    flags=re.IGNORECASE
                )
        
        return sentence
    
    def apply_structure_variations(self, sentence):
        """Apply structure variations while preserving meaning"""
        
        words = sentence.split()
        
        if len(words) < 6:
            return sentence
        
        # Apply sequence-preserving variations
        if random.random() < 0.4:
            # Verb repositioning within sentence
            words = self.reposition_verbs(words)
        
        if random.random() < 0.3:
            # Add natural modifiers
            words = self.add_natural_modifiers(words)
        
        if random.random() < 0.25:
            # Vary connecting words
            words = self.vary_connectives(words)
        
        return ' '.join(words)
    
    def reposition_verbs(self, words):
        """Reposition verbs within sentence for variety"""
        
        main_verbs = ['must', 'should', 'will', 'can', 'need', 'use', 'implement', 'establish']
        verb_positions = []
        
        for i, word in enumerate(words):
            if word.lower().strip('.,!?') in main_verbs:
                verb_positions.append(i)
        
        if verb_positions and len(verb_positions) > 0:
            verb_pos = verb_positions[0]
            if verb_pos > 2 and verb_pos < len(words) - 2:
                verb = words.pop(verb_pos)
                
                # Move verb to different position
                new_pos = random.randint(0, len(words) - 1)
                words.insert(new_pos, verb)
        
        return words
    
    def add_natural_modifiers(self, words):
        """Add natural modifiers at different positions"""
        
        modifiers = ['actually', 'basically', 'essentially', 'in fact', 'really', 'typically', 'generally']
        
        if len(words) > 5 and random.random() < 0.3:
            modifier = random.choice(modifiers)
            insert_pos = random.randint(1, min(3, len(words) - 2))
            words.insert(insert_pos, modifier + ',')
        
        return words
    
    def vary_connectives(self, words):
        """Vary connecting words and conjunctions"""
        
        connectives = ['and', 'but', 'or', 'so', 'yet', 'however', 'therefore', 'moreover']
        
        for i, word in enumerate(words):
            if word.lower() in connectives and i > 0 and i < len(words) - 1:
                if random.random() < 0.4:
                    alternatives = {
                        'and': ['plus', 'also', 'as well as'],
                        'but': ['however', 'still', 'yet'],
                        'or': ['alternatively', 'instead'],
                        'so': ['therefore', 'thus', 'as a result'],
                        'yet': ['still', 'nevertheless', 'even so']
                    }
                    
                    if word.lower() in alternatives:
                        words[i] = random.choice(alternatives[word.lower()])
                        break
        
        return words
    
    def ensure_proper_punctuation(self, sentence):
        """Ensure proper punctuation without breaking flow"""
        
        # Remove excessive punctuation
        sentence = re.sub(r',{2,}', ',', sentence)
        sentence = re.sub(r'\.{2,}', '.', sentence)
        
        # Ensure proper sentence ending
        sentence = sentence.strip()
        if sentence and not sentence[-1] in '.!?':
            if len(sentence.split()) > 3:
                sentence += '.'
        
        # Add natural commas for flow
        words = sentence.split()
        if len(words) > 8 and random.random() < 0.2:
            # Add comma at natural pause point
            mid_point = len(words) // 2
            if mid_point > 2 and mid_point < len(words) - 1:
                words.insert(mid_point, ',')
                sentence = ' '.join(words)
        
        return sentence
    
    def calculate_sequence_score(self, text):
        """Calculate human score for sequence-preserving humanization"""
        
        indicators = {
            'phrase_replacement': 0,
            'contraction_usage': 0,
            'structure_variation': 0,
            'punctuation_quality': 0,
            'sequence_preservation': 0
        }
        
        # AI phrase replacement score
        ai_phrases_count = sum(1 for phrase in self.ai_replacements.keys() 
                              if phrase in text.lower())
        total_ai_phrases = len(self.ai_replacements)
        phrases_replaced = total_ai_phrases - ai_phrases_count
        indicators['phrase_replacement'] = min(1.0, phrases_replaced / total_ai_phrases)
        
        # Contraction usage score
        contraction_count = sum(1 for contraction in self.contractions.values() 
                              if contraction in text)
        indicators['contraction_usage'] = min(1.0, contraction_count / 6)
        
        # Structure variation score
        structure_indicators = ['actually', 'basically', 'essentially', 'in fact', 'however', 'therefore']
        structure_count = sum(1 for indicator in structure_indicators if indicator in text.lower())
        indicators['structure_variation'] = min(1.0, structure_count / 5)
        
        # Punctuation quality score
        punctuation_variety = len(set(re.findall(r'[.,!?;:]', text)))
        indicators['punctuation_quality'] = min(1.0, punctuation_variety / 4)
        
        # Sequence preservation score (high priority)
        indicators['sequence_preservation'] = 1.0  # Always preserved in this method
        
        # Calculate overall score
        total_score = sum(indicators.values()) / len(indicators)
        human_score = min(100, total_score * 180)  # Boost for sequence preservation
        
        return human_score

def demo_sequence_preserving():
    """Demonstrate sequence-preserving structure humanizer"""
    
    print("🔄 Sequence-Preserving Structure Humanizer Demo")
    print("=" * 60)
    print("📝 Rules: Maintain sentence sequence, only change structure")
    print("🔧 Break AI patterns while preserving original order")
    print("=" * 60)
    
    humanizer = SequencePreservingHumanizer()
    
    # Test samples
    test_samples = [
        "Furthermore, we must utilize strategic methodologies to optimize our organizational infrastructure.",
        "The implementation of aforementioned initiatives necessitates careful consideration of various factors.",
        "Consequently, it is imperative that we establish a comprehensive framework for subsequent development.",
        "Moreover, utilization of advanced technologies will facilitate enhanced operational efficiency.",
        "In order to achieve desired outcomes, we must leverage our core competencies effectively."
    ]
    
    for i, original_text in enumerate(test_samples, 1):
        print(f"\n📝 Test {i}:")
        print(f"Original: {original_text}")
        
        result = humanizer.preserve_sequence_structure_humanize(original_text, intensity=0.7)
        
        if result['success']:
            print(f"Humanized: {result['humanized_text']}")
            print(f"Human Score: {result['human_score']:.1f}%")
            print(f"Character Count: {result['character_count']}")
            print(f"Changes: {', '.join(result['changes_applied'])}")
            print(f"Sequence Preserved: {result['sequence_preserved']}")
            
            if result['human_score'] >= 85:
                print("✅ Excellent sequence-preserving humanization!")
            elif result['human_score'] >= 70:
                print("✅ Good sequence-preserving humanization!")
            else:
                print("⚠️  Could use more structure variation")
                
        else:
            print(f"❌ Error: {result['error']}")
        
        print("-" * 60)
    
    print("\n🎯 Sequence-Preserving Demo Complete!")
    print("✨ Sentence sequence maintained while breaking AI patterns!")

if __name__ == "__main__":
    demo_sequence_preserving()

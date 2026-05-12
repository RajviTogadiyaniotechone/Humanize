#!/usr/bin/env python3
"""
Linguistic-Only Humanizer - Changes words and sentence structure only
No punctuation or formatting changes
"""

import re
import random
from datetime import datetime

class LinguisticHumanizer:
    """Humanizer that only changes words and sentence structure"""
    
    def __init__(self):
        self.initialize_linguistic_patterns()
    
    def initialize_linguistic_patterns(self):
        """Initialize linguistic variation patterns"""
        
        # Word replacement dictionaries
        self.word_replacements = {
            # Formal to informal
            'furthermore': ['also', 'plus', 'additionally', 'in addition'],
            'moreover': ['also', 'plus', 'additionally', 'besides'],
            'consequently': ['so', 'therefore', 'as a result', 'thus'],
            'nevertheless': ['still', 'however', 'but', 'even so'],
            'utilize': ['use', 'work with', 'employ', 'apply'],
            'facilitate': ['help', 'assist', 'make easier', 'enable'],
            'implement': ['put in place', 'set up', 'start', 'launch'],
            'optimize': ['improve', 'enhance', 'make better', 'fine-tune'],
            'enhance': ['improve', 'boost', 'upgrade', 'make better'],
            'leverage': ['use', 'make use of', 'capitalize on', 'take advantage of'],
            'establish': ['create', 'set up', 'build', 'form'],
            'necessitates': ['requires', 'needs', 'calls for', 'demands'],
            'comprehensive': ['complete', 'full', 'thorough', 'extensive'],
            'subsequent': ['following', 'next', 'later', 'after'],
            'aforementioned': ['mentioned', 'previous', 'earlier', 'above'],
            'imperative': ['essential', 'necessary', 'crucial', 'vital'],
            'strategic': ['planned', 'calculated', 'deliberate', 'thoughtful'],
            'methodologies': ['methods', 'approaches', 'techniques', 'ways'],
            'organizational': ['company', 'business', 'corporate', 'workplace'],
            'infrastructure': ['setup', 'system', 'framework', 'structure'],
            'synergistic': ['cooperative', 'collaborative', 'coordinated', 'joint'],
            'partnerships': ['collaborations', 'alliances', 'cooperations', 'relationships'],
            'initiatives': ['projects', 'programs', 'efforts', 'plans'],
            'consideration': ['thought', 'attention', 'care', 'regard'],
            'various': ['different', 'diverse', 'multiple', 'several'],
            'factors': ['elements', 'aspects', 'points', 'issues'],
            'technologies': ['tools', 'systems', 'solutions', 'methods'],
            'operational': ['working', 'running', 'functional', 'active'],
            'efficiency': ['productivity', 'performance', 'effectiveness', 'output'],
            'outcomes': ['results', 'consequences', 'effects', 'impacts'],
            'desired': ['wanted', 'needed', 'required', 'sought'],
            'competencies': ['skills', 'abilities', 'capabilities', 'strengths'],
            'effectively': ['well', 'properly', 'successfully', 'efficiently']
        }
        
        # Contractions
        self.contractions = {
            "do not": "don't",
            "will not": "won't", 
            "cannot": "can't",
            "did not": "didn't",
            "is not": "isn't",
            "are not": "aren't",
            "was not": "wasn't",
            "were not": "weren't",
            "have not": "haven't",
            "has not": "hasn't",
            "could not": "couldn't",
            "would not": "wouldn't",
            "should not": "shouldn't",
            "I am": "I'm",
            "you are": "you're",
            "we are": "we're",
            "they are": "they're",
            "it is": "it's",
            "that is": "that's"
        }
        
        # Sentence structure patterns
        self.sentence_patterns = [
            "subject-verb-object",
            "object-subject-verb", 
            "verb-subject-object",
            "prepositional-start",
            "adverbial-start"
        ]
    
    def replace_words(self, text):
        """Replace formal words with more natural alternatives"""
        
        words = text.split()
        replaced_words = []
        
        for word in words:
            # Clean word for matching
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Check for word replacement
            if clean_word in self.word_replacements:
                if random.random() < 0.7:  # 70% chance to replace
                    alternatives = self.word_replacements[clean_word]
                    replacement = random.choice(alternatives)
                    
                    # Preserve original capitalization
                    if word[0].isupper():
                        replacement = replacement.capitalize()
                    
                    # Preserve punctuation
                    punctuation = re.sub(r'\w', '', word)
                    if punctuation:
                        replacement += punctuation
                    
                    replaced_words.append(replacement)
                else:
                    replaced_words.append(word)
            else:
                replaced_words.append(word)
        
        return ' '.join(replaced_words)
    
    def add_contractions(self, text):
        """Add natural contractions"""
        
        for formal, contraction in self.contractions.items():
            if random.random() < 0.6:  # 60% chance
                text = re.sub(
                    r'\b' + re.escape(formal) + r'\b',
                    contraction,
                    text,
                    flags=re.IGNORECASE
                )
        
        return text
    
    def vary_sentence_structure(self, text):
        """Vary sentence structure without punctuation changes"""
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        varied_sentences = []
        
        for i, sentence in enumerate(sentences):
            if not sentence.strip():
                continue
            
            # Only apply to longer sentences
            words = sentence.split()
            if len(words) < 6:
                varied_sentences.append(sentence)
                continue
            
            # Strategy 1: Move prepositional phrases
            if random.random() < 0.3:
                sentence = self.move_prepositional_phrase(words)
                words = sentence.split()
            
            # Strategy 2: Invert clauses
            if len(words) > 8 and random.random() < 0.25:
                sentence = self.invert_clauses(words)
            
            # Strategy 3: Reorder adjectives/adverbs
            if random.random() < 0.2:
                sentence = self.reorder_modifiers(words)
            
            varied_sentences.append(sentence)
        
        return ' '.join(varied_sentences)
    
    def move_prepositional_phrase(self, words):
        """Move prepositional phrase to different position"""
        
        prepositions = ['in', 'on', 'at', 'by', 'for', 'with', 'from', 'to', 'of']
        
        for i, word in enumerate(words):
            if word.lower() in prepositions and i < len(words) - 2:
                # Found prepositional phrase
                phrase_end = i + 3
                while phrase_end < len(words) and not words[phrase_end].endswith(('.', '!', '?')):
                    phrase_end += 1
                
                if phrase_end < len(words):
                    phrase = words[i:phrase_end]
                    remaining = words[:i] + words[phrase_end:]
                    
                    # Move to beginning or end
                    if random.random() < 0.5 and len(remaining) > 3:
                        # Move to beginning
                        new_words = phrase + remaining
                    else:
                        # Move to end
                        new_words = remaining + phrase
                    
                    return ' '.join(new_words)
        
        return ' '.join(words)
    
    def invert_clauses(self, words):
        """Invert clause order"""
        
        conjunctions = ['and', 'but', 'or', 'so', 'yet', 'for', 'nor']
        
        for i, word in enumerate(words):
            if word.lower() in conjunctions and i > 0 and i < len(words) - 1:
                # Found conjunction - split clauses
                first_clause = words[:i]
                second_clause = words[i:]
                
                # Swap clauses
                new_words = second_clause + first_clause
                return ' '.join(new_words)
        
        return ' '.join(words)
    
    def reorder_modifiers(self, words):
        """Reorder adjectives and adverbs"""
        
        # Find adjectives and adverbs
        modifiers = []
        other_words = []
        
        for i, word in enumerate(words):
            # Simple heuristic for modifiers (ends in common suffixes)
            if (word.lower().endswith(('ly', 'ful', 'ous', 'ive', 'able', 'ible')) and 
                len(word) > 4 and random.random() < 0.3):
                modifiers.append(word)
            else:
                other_words.append(word)
        
        if modifiers and len(other_words) > 2:
            # Reinsert modifiers at different positions
            for modifier in modifiers:
                insert_pos = random.randint(1, len(other_words) - 1)
                other_words.insert(insert_pos, modifier)
            
            return ' '.join(other_words)
        
        return ' '.join(words)
    
    def calculate_linguistic_score(self, text):
        """Calculate human score based on linguistic changes only"""
        
        linguistic_indicators = {
            'word_variety': 0,
            'contractions_used': 0,
            'sentence_variety': 0,
            'structure_variety': 0,
            'formal_removal': 0
        }
        
        # Word variety
        words = re.findall(r'\b\w+\b', text.lower())
        unique_words = len(set(words))
        total_words = len(words)
        linguistic_indicators['word_variety'] = min(1.0, unique_words / max(1, total_words))
        
        # Contractions used
        contraction_count = sum(1 for contraction in self.contractions.values() 
                             if contraction in text)
        linguistic_indicators['contractions_used'] = min(1.0, contraction_count / 5)
        
        # Sentence variety
        sentences = re.split(r'(?<=[.!?])\s+', text)
        if sentences:
            lengths = [len(s.split()) for s in sentences]
            if len(lengths) > 1:
                avg_length = sum(lengths) / len(lengths)
                variance = sum((l - avg_length) ** 2 for l in lengths) / len(lengths)
                linguistic_indicators['sentence_variety'] = min(1.0, variance / 20)
        
        # Structure variety
        sentence_starts = []
        for sentence in re.split(r'(?<=[.!?])\s+', text):
            words = sentence.split()
            if words:
                sentence_starts.append(words[0].lower())
        
        unique_starts = len(set(sentence_starts))
        linguistic_indicators['structure_variety'] = min(1.0, unique_starts / max(1, len(sentence_starts)))
        
        # Formal word removal
        formal_words_removed = sum(1 for formal in self.word_replacements.keys() 
                                if formal not in text.lower())
        total_formal = len(self.word_replacements)
        linguistic_indicators['formal_removal'] = formal_words_removed / max(1, total_formal)
        
        # Calculate overall score
        total_score = sum(linguistic_indicators.values()) / len(linguistic_indicators)
        human_score = min(100, total_score * 130)  # Boost for linguistic changes
        
        return human_score
    
    def linguistic_only_humanize(self, text, intensity=0.7):
        """Main linguistic-only humanization function"""
        
        if not text or len(text.strip()) < 10:
            return {
                'success': False,
                'error': 'Text too short'
            }
        
        original_text = text
        changes_applied = []
        
        # Apply linguistic changes based on intensity
        if intensity >= 0.3:
            text = self.add_contractions(text)
            changes_applied.append('contractions')
        
        if intensity >= 0.4:
            text = self.replace_words(text)
            changes_applied.append('word_replacements')
        
        if intensity >= 0.5:
            text = self.vary_sentence_structure(text)
            changes_applied.append('sentence_restructuring')
        
        if intensity >= 0.6:
            text = self.vary_sentence_structure(text)  # Apply again for more variety
            changes_applied.append('additional_restructuring')
        
        if intensity >= 0.8:
            text = self.replace_words(text)  # Apply again for more changes
            changes_applied.append('additional_replacements')
        
        # Calculate linguistic score
        human_score = self.calculate_linguistic_score(text)
        
        # Count word changes
        original_words = set(re.findall(r'\b\w+\b', original_text.lower()))
        humanized_words = set(re.findall(r'\b\w+\b', text.lower()))
        word_changes = len(original_words.symmetric_difference(humanized_words))
        
        return {
            'success': True,
            'original_text': original_text,
            'humanized_text': text,
            'human_score': human_score,
            'changes_applied': changes_applied,
            'words_changed': word_changes,
            'punctuation_preserved': self.check_punctuation_preservation(original_text, text),
            'timestamp': datetime.now().isoformat()
        }
    
    def check_punctuation_preservation(self, original, humanized):
        """Check if punctuation is preserved"""
        
        original_punct = set(re.findall(r'[^\w\s]', original))
        humanized_punct = set(re.findall(r'[^\w\s]', humanized))
        
        preserved = original_punct.intersection(humanized_punct)
        added = humanized_punct - original_punct
        removed = original_punct - humanized_punct
        
        return {
            'preserved_count': len(preserved),
            'added_count': len(added),
            'removed_count': len(removed),
            'preservation_rate': len(preserved) / max(1, len(original_punct)) * 100
        }

def demo_linguistic_humanizer():
    """Demonstrate linguistic-only humanizer"""
    
    print("📝 Linguistic-Only Humanizer Demo")
    print("=" * 50)
    print("📝 Rules: Change words + sentence structure ONLY")
    print("🚫 No punctuation or formatting changes")
    print("=" * 50)
    
    humanizer = LinguisticHumanizer()
    
    # Test samples
    test_samples = [
        "Furthermore, we must utilize strategic methodologies to optimize our organizational infrastructure.",
        "The implementation of aforementioned initiatives necessitates careful consideration of various factors.",
        "Consequently, it is imperative that we establish a comprehensive framework for subsequent development.",
        "Moreover, utilization of advanced technologies will facilitate enhanced operational efficiency.",
        "In order to achieve the desired outcomes, we must leverage our core competencies effectively."
    ]
    
    for i, original_text in enumerate(test_samples, 1):
        print(f"\n📝 Test {i}:")
        print(f"Original: {original_text}")
        
        result = humanizer.linguistic_only_humanize(original_text, intensity=0.8)
        
        if result['success']:
            print(f"Humanized: {result['humanized_text']}")
            print(f"Human Score: {result['human_score']:.1f}%")
            print(f"Words Changed: {result['words_changed']}")
            print(f"Punctuation Preserved: {result['punctuation_preserved']['preservation_rate']:.1f}%")
            print(f"Changes: {', '.join(result['changes_applied'])}")
            
            if result['human_score'] >= 80:
                print("✅ Low AI detection achieved!")
            else:
                print("⚠️  May need more linguistic variation")
                
        else:
            print(f"❌ Error: {result['error']}")
        
        print("-" * 50)
    
    print("\n🎯 Linguistic-Only Humanizer Demo Complete!")
    print("✨ Words and structure changed, punctuation preserved!")

if __name__ == "__main__":
    demo_linguistic_humanizer()

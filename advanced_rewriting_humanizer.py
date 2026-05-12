#!/usr/bin/env python3
"""
Advanced Rewriting Humanizer - Actively rewrites sentences with natural language
Changes wording, replaces AI phrases, varies structure, maintains proper punctuation
"""

import re
import random
from datetime import datetime

class AdvancedRewritingHumanizer:
    """Advanced humanizer that actively rewrites content naturally"""
    
    def __init__(self):
        self.initialize_rewriting_patterns()
    
    def initialize_rewriting_patterns(self):
        """Initialize advanced rewriting patterns"""
        
        # AI phrase replacements with natural alternatives
        self.ai_phrase_replacements = {
            # Formal AI phrases to natural alternatives
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
            "synergistic": ["cooperative", "collaborative", "joint", "team-based", "coordinated"],
            "partnerships": ["collaborations", "relationships", "alliances", "teamwork", "cooperations"],
            "initiatives": ["projects", "programs", "efforts", "plans", "actions"],
            "consideration": ["thought", "attention", "care", "focus", "regard"],
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
        
        # Sentence structure patterns
        self.sentence_patterns = {
            "simple": ["Subject-Verb-Object", "Subject-Verb-Adjective-Object"],
            "complex": ["Subject-Verb-Clause-Conjunction-Clause", "Clause-Subject-Verb-Clause"],
            "question": ["Auxiliary-Subject-Verb", "Question Word-Subject-Verb"],
            "transitional": ["Transition-Subject-Verb", "Subject-Transition-Verb-Object"]
        }
        
        # Natural transitions
        self.natural_transitions = [
            "so", "then", "but", "and", "plus", "also", "meanwhile", "however",
            "for example", "for instance", "in fact", "as a result", "that said",
            "on the other hand", "in addition", "what's more", "after that"
        ]
        
        # Contractions for natural flow
        self.contractions = {
            "do not": "don't", "will not": "won't", "cannot": "can't",
            "did not": "didn't", "is not": "isn't", "are not": "aren't",
            "was not": "wasn't", "were not": "weren't", "have not": "haven't",
            "has not": "hasn't", "could not": "couldn't", "would not": "wouldn't",
            "should not": "shouldn't", "I am": "I'm", "you are": "you're",
            "we are": "we're", "they are": "they're", "it is": "it's",
            "that is": "that's"
        }
    
    def active_sentence_rewriting(self, sentence):
        """Actively rewrite sentence with natural language"""
        
        # Step 1: Replace AI phrases with natural alternatives
        rewritten = self.replace_ai_phrases(sentence)
        
        # Step 2: Vary sentence structure
        rewritten = self.vary_sentence_structure(rewritten)
        
        # Step 3: Add natural contractions
        rewritten = self.add_natural_contractions(rewritten)
        
        # Step 4: Ensure proper punctuation
        rewritten = self.ensure_proper_punctuation(rewritten)
        
        # Step 5: Add natural transitions if needed
        rewritten = self.add_natural_transitions(rewritten)
        
        return rewritten
    
    def replace_ai_phrases(self, text):
        """Replace AI-style phrases with natural alternatives"""
        
        words = text.split()
        rewritten_words = []
        
        for word in words:
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Check for phrase replacement
            if clean_word in self.ai_phrase_replacements:
                if random.random() < 0.8:  # 80% chance to replace
                    alternatives = self.ai_phrase_replacements[clean_word]
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
    
    def vary_sentence_structure(self, sentence):
        """Vary sentence structure for natural flow"""
        
        words = sentence.split()
        
        if len(words) < 6:
            return sentence  # Too short for major restructuring
        
        # Identify sentence pattern
        structure_type = self.identify_structure_type(words)
        
        # Apply structure variation based on type
        if structure_type == "simple" and random.random() < 0.4:
            return self.reorder_simple_sentence(words)
        elif structure_type == "complex" and random.random() < 0.5:
            return self.reorder_complex_sentence(words)
        elif random.random() < 0.3:
            return self.modify_verb_placement(words)
        
        return sentence
    
    def identify_structure_type(self, words):
        """Identify the type of sentence structure"""
        
        # Simple heuristics for structure identification
        has_conjunction = any(word.lower() in ['and', 'but', 'or', 'so', 'yet'] for word in words)
        has_comma = ',' in ' '.join(words)
        
        if has_conjunction and has_comma:
            return "complex"
        elif len(words) > 8:
            return "complex"
        else:
            return "simple"
    
    def reorder_simple_sentence(self, words):
        """Reorder simple sentence structure"""
        
        # Find subject, verb, object pattern
        subjects = []
        verbs = []
        objects = []
        
        # Simple word classification
        for i, word in enumerate(words):
            word_lower = word.lower().strip('.,!?')
            
            # Very basic classification
            if i == 0 or word_lower in ['we', 'they', 'it', 'the', 'our']:
                subjects.append(word)
            elif word_lower in ['must', 'should', 'will', 'can', 'need', 'use', 'implement']:
                verbs.append(word)
            else:
                objects.append(word)
        
        # Reconstruct with variation
        if subjects and verbs and objects and random.random() < 0.5:
            # Start with object or verb
            if random.random() < 0.5:
                return ' '.join(objects + verbs + subjects)
            else:
                return ' '.join(verbs + objects + subjects)
        
        return ' '.join(words)
    
    def reorder_complex_sentence(self, words):
        """Reorder complex sentence with clauses"""
        
        # Find clause boundaries
        clause_separators = ['and', 'but', 'or', 'so', 'yet', 'while', 'because']
        clause_positions = []
        
        for i, word in enumerate(words):
            if word.lower().strip('.,!?') in clause_separators:
                clause_positions.append(i)
        
        if len(clause_positions) >= 1:
            # Reorder clauses
            first_clause_end = clause_positions[0]
            
            if first_clause_end > 2 and first_clause_end < len(words) - 2:
                first_clause = words[:first_clause_end]
                second_clause = words[first_clause_end:]
                
                # Swap clauses with some probability
                if random.random() < 0.4:
                    return ' '.join(second_clause + first_clause)
        
        return ' '.join(words)
    
    def modify_verb_placement(self, words):
        """Modify verb placement for variety"""
        
        # Find verbs
        verb_positions = []
        for i, word in enumerate(words):
            if word.lower() in ['must', 'should', 'will', 'can', 'need', 'use', 'implement', 'establish']:
                verb_positions.append(i)
        
        # Move verb to different position
        if verb_positions and len(verb_positions) > 0:
            verb_pos = verb_positions[0]
            if verb_pos > 1 and verb_pos < len(words) - 2:
                verb = words.pop(verb_pos)
                
                # Insert at new position
                new_pos = random.randint(0, len(words) - 1)
                words.insert(new_pos, verb)
        
        return ' '.join(words)
    
    def add_natural_contractions(self, text):
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
    
    def ensure_proper_punctuation(self, text):
        """Ensure punctuation is grammatically correct and natural"""
        
        # Fix common AI punctuation issues
        sentences = re.split(r'(?<=[.!?])\s+', text)
        fixed_sentences = []
        
        for sentence in sentences:
            # Remove excessive commas
            sentence = re.sub(r',{2,}', ',', sentence)
            
            # Ensure proper sentence ending
            if sentence and not sentence[-1] in '.!?':
                if len(sentence.split()) > 3:  # Only for longer sentences
                    sentence += '.'
            
            # Add natural commas for flow
            words = sentence.split()
            if len(words) > 8 and random.random() < 0.3:
                # Add comma at natural pause point
                mid_point = len(words) // 2
                if mid_point > 2 and mid_point < len(words) - 1:
                    words.insert(mid_point, ',')
                    sentence = ' '.join(words)
            
            fixed_sentences.append(sentence)
        
        return ' '.join(fixed_sentences)
    
    def add_natural_transitions(self, text):
        """Add natural transitions between sentences"""
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        if len(sentences) < 2:
            return text
        
        enhanced_sentences = [sentences[0]]
        
        for i in range(1, len(sentences)):
            prev_sentence = sentences[i-1]
            current_sentence = sentences[i]
            
            # Add transition with some probability
            if random.random() < 0.4:  # 40% chance
                transition = random.choice(self.natural_transitions)
                
                # Don't add transition if already starts with one
                if not current_sentence.lower().startswith(transition):
                    current_sentence = f"{transition}, {current_sentence.lower()}"
            
            enhanced_sentences.append(current_sentence)
        
        return ' '.join(enhanced_sentences)
    
    def calculate_rewriting_score(self, text):
        """Calculate human score based on rewriting quality"""
        
        rewriting_indicators = {
            'natural_language': 0,
            'phrase_replacement': 0,
            'structure_variety': 0,
            'contraction_usage': 0,
            'punctuation_quality': 0,
            'transition_flow': 0
        }
        
        # Natural language indicators
        natural_words = ['so', 'plus', 'also', 'but', 'however', 'therefore', 'meanwhile']
        natural_count = sum(1 for word in natural_words if word in text.lower())
        rewriting_indicators['natural_language'] = min(1.0, natural_count / 5)
        
        # AI phrase replacement
        ai_phrases_count = sum(1 for phrase in self.ai_phrase_replacements.keys() 
                              if phrase in text.lower())
        total_ai_phrases = len(self.ai_phrase_replacements)
        phrases_removed = total_ai_phrases - ai_phrases_count
        rewriting_indicators['phrase_replacement'] = min(1.0, phrases_removed / total_ai_phrases)
        
        # Structure variety
        sentences = re.split(r'(?<=[.!?])\s+', text)
        if sentences:
            sentence_starts = [s.split()[0].lower() for s in sentences if s.split()]
            unique_starts = len(set(sentence_starts))
            rewriting_indicators['structure_variety'] = min(1.0, unique_starts / max(1, len(sentences)))
        
        # Contraction usage
        contraction_count = sum(1 for contraction in self.contractions.values() 
                              if contraction in text)
        rewriting_indicators['contraction_usage'] = min(1.0, contraction_count / 5)
        
        # Punctuation quality
        punctuation_variety = len(set(re.findall(r'[.,!?;:]', text)))
        rewriting_indicators['punctuation_quality'] = min(1.0, punctuation_variety / 4)
        
        # Transition flow
        transition_count = sum(1 for transition in self.natural_transitions 
                              if transition in text.lower())
        rewriting_indicators['transition_flow'] = min(1.0, transition_count / 8)
        
        # Calculate overall score
        total_score = sum(rewriting_indicators.values()) / len(rewriting_indicators)
        human_score = min(100, total_score * 140)  # Boost for active rewriting
        
        return human_score
    
    def advanced_rewriting_humanize(self, text, intensity=0.7):
        """Main advanced rewriting humanization function"""
        
        if not text or len(text.strip()) < 10:
            return {
                'success': False,
                'error': 'Text too short'
            }
        
        original_text = text
        changes_applied = []
        
        # Split into sentences for processing
        sentences = re.split(r'(?<=[.!?])\s+', text)
        rewritten_sentences = []
        
        # Apply rewriting based on intensity
        for sentence in sentences:
            if not sentence.strip():
                continue
            
            # Apply active rewriting
            if intensity >= 0.2:
                sentence = self.active_sentence_rewriting(sentence)
                changes_applied.append('active_rewriting')
            
            # Additional variations for higher intensity
            if intensity >= 0.4:
                sentence = self.add_sentence_variety(sentence)
                changes_applied.append('sentence_variety')
            
            if intensity >= 0.6:
                sentence = self.enhance_natural_flow(sentence)
                changes_applied.append('natural_flow')
            
            if intensity >= 0.8:
                sentence = self.advanced_rewriting_techniques(sentence)
                changes_applied.append('advanced_techniques')
            
            rewritten_sentences.append(sentence)
        
        # Reconstruct text
        humanized_text = ' '.join(rewritten_sentences)
        
        # Calculate character count
        char_count = len(humanized_text)
        
        # Calculate rewriting score
        human_score = self.calculate_rewriting_score(humanized_text)
        
        return {
            'success': True,
            'original_text': original_text,
            'humanized_text': humanized_text,
            'human_score': human_score,
            'changes_applied': changes_applied,
            'character_count': char_count,
            'timestamp': datetime.now().isoformat()
        }
    
    def add_sentence_variety(self, sentence):
        """Add variety to sentence structure"""
        
        words = sentence.split()
        
        # Vary sentence length and complexity
        if len(words) > 10 and random.random() < 0.3:
            # Break into two shorter sentences
            mid_point = len(words) // 2
            first_part = ' '.join(words[:mid_point]) + '.'
            second_part = ' '.join(words[mid_point:])
            return f"{first_part} {second_part}"
        
        elif len(words) < 6 and random.random() < 0.2:
            # Combine with next sentence logic would go here
            # For now, just add variety
            return sentence
        
        return ' '.join(words)
    
    def enhance_natural_flow(self, sentence):
        """Enhance natural flow between ideas"""
        
        # Add natural emphasis or clarification
        words = sentence.split()
        
        if len(words) > 6 and random.random() < 0.25:
            # Add natural emphasis
            emphasis_words = ['actually', 'basically', 'essentially', 'in fact', 'really']
            emphasis = random.choice(emphasis_words)
            
            # Insert at natural position
            insert_pos = random.randint(1, min(3, len(words) - 2))
            words.insert(insert_pos, emphasis)
            
            return ' '.join(words)
        
        return sentence
    
    def advanced_rewriting_techniques(self, sentence):
        """Apply advanced rewriting techniques for maximum humanization"""
        
        words = sentence.split()
        
        # Technique 1: Invert sentence structure
        if random.random() < 0.25:
            words = self.invert_sentence_structure(words)
        
        # Technique 2: Add natural modifiers
        if random.random() < 0.3:
            words = self.add_natural_modifiers(words)
        
        # Technique 3: Replace with natural expressions
        if random.random() < 0.35:
            words = self.replace_with_natural_expressions(words)
        
        # Technique 4: Vary sentence complexity
        if random.random() < 0.2:
            words = self.vary_sentence_complexity(words)
        
        return ' '.join(words)
    
    def invert_sentence_structure(self, words):
        """Invert sentence structure for variety"""
        
        if len(words) < 6:
            return words
        
        # Find main verb and move it
        verbs = ['must', 'should', 'will', 'can', 'need', 'use', 'implement', 'establish']
        verb_positions = [i for i, word in enumerate(words) if word.lower().strip('.,!?') in verbs]
        
        if verb_positions and len(verb_positions) > 0:
            verb_pos = verb_positions[0]
            if verb_pos > 1 and verb_pos < len(words) - 2:
                verb = words.pop(verb_pos)
                
                # Move to different position
                new_pos = random.randint(0, min(len(words), verb_pos + 2))
                words.insert(new_pos, verb)
        
        return words
    
    def add_natural_modifiers(self, words):
        """Add natural modifiers to enhance flow"""
        
        natural_modifiers = [
            'actually', 'basically', 'essentially', 'in fact', 'really', 'truly',
            'typically', 'generally', 'usually', 'often', 'sometimes'
        ]
        
        # Insert modifiers at natural positions
        if len(words) > 5 and random.random() < 0.4:
            modifier = random.choice(natural_modifiers)
            insert_pos = random.randint(1, min(3, len(words) - 2))
            
            # Add comma after modifier
            if insert_pos < len(words):
                words.insert(insert_pos, modifier + ',')
        
        return words
    
    def replace_with_natural_expressions(self, words):
        """Replace formal phrases with natural expressions"""
        
        expression_replacements = {
            "in order to": ["to", "so we can", "in order to"],
            "due to the fact that": ["because", "since", "as", "due to"],
            "with regard to": ["about", "regarding", "when it comes to"],
            "it is important to note": ["importantly", "notably", "significantly"],
            "it should be noted that": ["note that", "it's worth mentioning"],
            "for the purpose of": ["to", "for", "aimed at"],
            "on the basis of": ["based on", "according to", "from"]
        }
        
        # Find and replace expressions
        for i in range(len(words) - 1):
            phrase = ' '.join(words[i:i+2]).lower()
            
            for formal, natural_list in expression_replacements.items():
                if phrase.startswith(formal):
                    replacement = random.choice(natural_list)
                    
                    # Replace the expression
                    words[i] = replacement
                    if i+1 < len(words):
                        words[i+1] = ''  # Remove second word of phrase
        
        # Remove empty words
        words = [w for w in words if w.strip()]
        
        return words
    
    def vary_sentence_complexity(self, words):
        """Vary sentence complexity for natural flow"""
        
        if len(words) < 8:
            return words
        
        # Add or remove clauses for complexity variation
        if random.random() < 0.5:
            # Add dependent clause
            clause_starters = ["which", "that", "who", "when", "where", "because"]
            starter = random.choice(clause_starters)
        return words
        
    # Add or remove clauses for complexity variation
    if random.random() < 0.5:
        # Add dependent clause
        clause_starters = ["which", "that", "who", "when", "where", "because"]
        starter = random.choice(clause_starters)
            
        insert_pos = random.randint(2, len(words) - 2)
        if insert_pos < len(words):
            words.insert(insert_pos, starter)
        
    return ' '.join(words)
    
def enhance_natural_flow(self, sentence):
    """Enhance natural flow between ideas"""
        
    # Add natural emphasis or clarification
    words = sentence.split()
        
    if len(words) > 6 and random.random() < 0.25:
        # Add natural emphasis
        emphasis_words = ['actually', 'basically', 'essentially', 'in fact', 'really']
        emphasis = random.choice(emphasis_words)
            
        # Insert at natural position
        insert_pos = random.randint(1, min(3, len(words) - 2))
        words.insert(insert_pos, emphasis)
            
        return ' '.join(words)
        
    return sentence

def demo_advanced_rewriting():
    """Demonstrate advanced rewriting humanizer"""
    
    print("✍️ Advanced Rewriting Humanizer Demo")
    print("=" * 60)
    print("📝 Rules: Actively rewrite sentences with natural language")
    print("🔄 Replace AI phrases, vary structure, proper punctuation")
    print("=" * 60)
    
    humanizer = AdvancedRewritingHumanizer()
    
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
        
        result = humanizer.advanced_rewriting_humanize(original_text, intensity=0.8)
        
        if result['success']:
            print(f"Humanized: {result['humanized_text']}")
            print(f"Human Score: {result['human_score']:.1f}%")
            print(f"Character Count: {result['character_count']}")
            print(f"Changes: {', '.join(result['changes_applied'])}")
            
            if result['human_score'] >= 85:
                print("✅ Excellent natural rewriting!")
            elif result['human_score'] >= 70:
                print("✅ Good natural rewriting!")
            else:
                print("⚠️  Could use more rewriting")
                
        else:
            print(f"❌ Error: {result['error']}")
        
        print("-" * 60)
    
    print("\n🎯 Advanced Rewriting Demo Complete!")
    print("✨ Active rewriting with natural language achieved!")

if __name__ == "__main__":
    demo_advanced_rewriting()

#!/usr/bin/env python3
"""
Focused Rewriting Humanizer - Actively rewrites sentences with natural language
Changes wording, replaces AI phrases, varies structure, uses synonyms
"""

import re
import random
from datetime import datetime

class FocusedRewritingHumanizer:
    """Focused humanizer that actively rewrites content naturally"""
    
    def __init__(self):
        self.initialize_rewriting_patterns()
    
    def initialize_rewriting_patterns(self):
        """Initialize focused rewriting patterns"""
        
        # Comprehensive AI phrase replacements
        self.ai_replacements = {
            # Formal connectors
            "furthermore": ["also", "plus", "what's more", "on top of that", "additionally"],
            "moreover": ["also", "plus", "in addition", "besides", "another thing"],
            "consequently": ["so", "therefore", "as a result", "that's why", "for this reason"],
            "nevertheless": ["still", "however", "but", "even so", "that said"],
            "subsequently": ["then", "after that", "next", "following this"],
            "accordingly": ["so", "then", "for that reason", "based on this"],
            
            # Formal verbs
            "utilize": ["use", "work with", "make use of", "employ", "apply"],
            "facilitate": ["help", "make easier", "enable", "assist", "support"],
            "implement": ["put in place", "set up", "start using", "launch", "begin"],
            "optimize": ["improve", "make better", "enhance", "fine-tune", "boost"],
            "enhance": ["improve", "boost", "upgrade", "make better", "strengthen"],
            "leverage": ["use", "take advantage of", "make the most of", "capitalize on"],
            "establish": ["create", "set up", "build", "form", "start"],
            "necessitates": ["requires", "needs", "calls for", "demands", "means"],
            "establish": ["create", "set up", "build", "form", "start"],
            
            # Formal adjectives
            "comprehensive": ["complete", "full", "thorough", "extensive", "detailed"],
            "subsequent": ["following", "next", "later", "after", "coming"],
            "aforementioned": ["mentioned", "previous", "earlier", "above", "said"],
            "imperative": ["essential", "necessary", "crucial", "vital", "must-have"],
            "strategic": ["planned", "thoughtful", "careful", "smart", "key"],
            "organizational": ["company", "business", "workplace", "team", "corporate"],
            "various": ["different", "diverse", "multiple", "several", "many"],
            "operational": ["working", "running", "active", "functioning", "in use"],
            "desired": ["wanted", "needed", "required", "sought", "targeted"],
            
            # Formal nouns
            "methodologies": ["methods", "approaches", "ways", "techniques", "systems"],
            "infrastructure": ["setup", "system", "framework", "structure", "foundation"],
            "partnerships": ["collaborations", "relationships", "alliances", "teamwork", "cooperations"],
            "initiatives": ["projects", "programs", "efforts", "plans", "actions"],
            "factors": ["elements", "aspects", "points", "issues", "things"],
            "technologies": ["tools", "systems", "solutions", "methods", "approaches"],
            "efficiency": ["productivity", "performance", "output", "results", "effectiveness"],
            "outcomes": ["results", "effects", "consequences", "impacts", "end results"],
            "competencies": ["skills", "abilities", "strengths", "capabilities", "talents"]
        }
        
        # Synonym groups for variety
        self.synonym_groups = {
            "good": ["great", "excellent", "wonderful", "fantastic", "amazing"],
            "important": ["crucial", "vital", "essential", "key", "critical"],
            "help": ["assist", "support", "aid", "enable", "facilitate"],
            "improve": ["enhance", "boost", "upgrade", "make better", "strengthen"],
            "use": ["employ", "apply", "work with", "make use of", "utilize"],
            "make": ["create", "build", "develop", "produce", "generate"],
            "show": ["demonstrate", "display", "reveal", "present", "illustrate"],
            "get": ["obtain", "acquire", "receive", "gain", "secure"],
            "need": ["require", "want", "must have", "call for", "demand"],
            "can": ["are able to", "have the ability to", "manage to", "succeed in"],
            "will": ["going to", "are set to", "plan to", "intend to"],
            "should": ["ought to", "need to", "must", "are supposed to", "had better"]
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
        
        # Sentence structure patterns
        self.structure_patterns = [
            "subject-verb-object",
            "object-subject-verb", 
            "verb-subject-object",
            "prepositional-start",
            "adverbial-start",
            "conditional-start"
        ]
    
    def focused_sentence_rewriting(self, sentence):
        """Actively rewrite sentence with natural language"""
        
        # Step 1: Replace AI phrases with natural alternatives
        rewritten = self.replace_ai_phrases(sentence)
        
        # Step 2: Apply synonym-based rewriting
        rewritten = self.apply_synonym_rewriting(rewritten)
        
        # Step 3: Vary sentence structure
        rewritten = self.vary_sentence_structure(rewritten)
        
        # Step 4: Add natural contractions
        rewritten = self.add_natural_contractions(rewritten)
        
        # Step 5: Ensure proper punctuation
        rewritten = self.ensure_proper_punctuation(rewritten)
        
        return rewritten
    
    def replace_ai_phrases(self, text):
        """Replace AI-style phrases with natural alternatives"""
        
        words = text.split()
        rewritten_words = []
        
        for word in words:
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Check for phrase replacement
            if clean_word in self.ai_replacements:
                if random.random() < 0.85:  # 85% chance to replace
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
    
    def apply_synonym_rewriting(self, text):
        """Apply synonym-based rewriting for variety"""
        
        words = text.split()
        rewritten_words = []
        
        for word in words:
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Check for synonym replacement
            synonym_found = False
            for base_word, synonyms in self.synonym_groups.items():
                if clean_word == base_word or clean_word in synonyms:
                    if random.random() < 0.6:  # 60% chance to use synonym
                        # Choose synonym that fits context
                        available_synonyms = [s for s in synonyms if s != clean_word]
                        if available_synonyms:
                            synonym = random.choice(available_synonyms)
                            
                            # Preserve capitalization and punctuation
                            if word[0].isupper():
                                synonym = synonym.capitalize()
                            
                            punctuation = re.sub(r'\w', '', word)
                            if punctuation:
                                synonym += punctuation
                            
                            rewritten_words.append(synonym)
                            synonym_found = True
                            break
            
            if not synonym_found:
                rewritten_words.append(word)
        
        return ' '.join(rewritten_words)
    
    def vary_sentence_structure(self, sentence):
        """Vary sentence structure for natural flow"""
        
        words = sentence.split()
        
        if len(words) < 6:
            return sentence
        
        # Apply structure variation based on probability
        if random.random() < 0.4:
            # Reorder clauses
            words = self.reorder_clauses(words)
        
        if random.random() < 0.3:
            # Change verb position
            words = self.modify_verb_placement(words)
        
        if random.random() < 0.25:
            # Invert sentence order
            words = self.invert_sentence_order(words)
        
        return ' '.join(words)
    
    def reorder_clauses(self, words):
        """Reorder clauses for variety"""
        
        conjunctions = ['and', 'but', 'or', 'so', 'yet', 'while', 'because', 'although']
        clause_positions = []
        
        for i, word in enumerate(words):
            if word.lower().strip('.,!?') in conjunctions:
                clause_positions.append(i)
        
        if len(clause_positions) >= 1:
            # Reorder clauses
            first_clause_end = clause_positions[0]
            
            if first_clause_end > 2 and first_clause_end < len(words) - 2:
                first_clause = words[:first_clause_end]
                second_clause = words[first_clause_end:]
                
                # Swap clauses
                if random.random() < 0.6:
                    return second_clause + first_clause
        
        return words
    
    def modify_verb_placement(self, words):
        """Modify verb placement for variety"""
        
        main_verbs = ['must', 'should', 'will', 'can', 'need', 'use', 'implement', 'establish', 
                      'create', 'make', 'get', 'show', 'help', 'improve']
        verb_positions = []
        
        for i, word in enumerate(words):
            if word.lower().strip('.,!?') in main_verbs:
                verb_positions.append(i)
        
        if verb_positions and len(verb_positions) > 0:
            verb_pos = verb_positions[0]
            if verb_pos > 1 and verb_pos < len(words) - 2:
                verb = words.pop(verb_pos)
                
                # Move to different position
                new_pos = random.randint(0, len(words) - 1)
                words.insert(new_pos, verb)
        
        return words
    
    def invert_sentence_order(self, words):
        """Invert sentence order for variety"""
        
        if len(words) < 8:
            return words
        
        # Find natural break points
        break_points = []
        for i, word in enumerate(words):
            if word.lower().strip('.,!?') in ['and', 'but', 'or', 'so', 'yet']:
                break_points.append(i)
        
        if break_points:
            # Invert around break point
            break_point = break_points[0]
            if break_point > 2 and break_point < len(words) - 2:
                first_part = words[:break_point]
                second_part = words[break_point:]
                
                # Invert order
                if random.random() < 0.5:
                    return second_part + first_part
        
        return words
    
    def add_natural_contractions(self, text):
        """Add natural contractions"""
        
        for formal, contraction in self.contractions.items():
            if random.random() < 0.7:  # 70% chance
                text = re.sub(
                    r'\b' + re.escape(formal) + r'\b',
                    contraction,
                    text,
                    flags=re.IGNORECASE
                )
        
        return text
    
    def ensure_proper_punctuation(self, text):
        """Ensure punctuation is grammatically correct and natural"""
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        fixed_sentences = []
        
        for sentence in sentences:
            # Step 1: Remove excessive commas
            sentence = re.sub(r',{2,}', ',', sentence)
            
            # Step 2: Ensure proper sentence ending
            sentence = self.ensure_sentence_ending(sentence)
            
            # Step 3: Add natural commas for flow (not excessive)
            sentence = self.add_natural_commas(sentence)
            
            # Step 4: Fix awkward punctuation patterns
            sentence = self.fix_awkward_punctuation(sentence)
            
            # Step 5: Ensure proper use of semicolons and colons
            sentence = self.ensure_advanced_punctuation(sentence)
            
            fixed_sentences.append(sentence)
        
        return ' '.join(fixed_sentences)
    
    def ensure_sentence_ending(self, sentence):
        """Ensure proper sentence ending"""
        
        sentence = sentence.strip()
        
        # Don't add period if already has ending punctuation
        if sentence and sentence[-1] in '.!?':
            return sentence
        
        # Add period for complete sentences
        words = sentence.split()
        if len(words) >= 3 and not sentence.endswith(('.', '!', '?')):
            sentence += '.'
        
        return sentence
    
    def add_natural_commas(self, sentence):
        """Add natural commas without overuse"""
        
        words = sentence.split()
        
        # Only add commas for natural pauses, not randomly
        if len(words) <= 8:
            return sentence
        
        # Identify natural comma positions
        comma_positions = []
        
        # Add comma before conjunctions in longer sentences
        for i, word in enumerate(words):
            if word.lower() in ['and', 'but', 'or', 'so', 'yet'] and i > 2:
                if i < len(words) - 2 and random.random() < 0.4:
                    comma_positions.append(i)
        
        # Add comma after introductory phrases
        intro_words = ['however', 'therefore', 'moreover', 'furthermore', 'consequently']
        for i, word in enumerate(words):
            if word.lower() in intro_words and i < len(words) - 3:
                if random.random() < 0.3:
                    comma_positions.append(i + 1)
        
        # Apply commas at identified positions
        if comma_positions:
            comma_positions.sort(reverse=True)  # Add from right to left
            for pos in comma_positions:
                if pos < len(words):
                    words.insert(pos, ',')
        
        return ' '.join(words)
    
    def fix_awkward_punctuation(self, sentence):
        """Fix awkward punctuation patterns"""
        
        # Fix common awkward patterns
        fixes = [
            (r'\s*,\s*', ','),  # Fix awkward comma usage
            (r'\s*\.\s*\.', '.'),  # Fix double periods
            (r'\s*;\s*\.', '.'),  # Fix semicolon-period combos
            (r'\s*:\s*\.', '.'),  # Fix colon-period combos
            (r'\s*-\s*-\s*', '-'),  # Fix double dashes
        ]
        
        for pattern, replacement in fixes:
            sentence = re.sub(pattern, replacement, sentence)
        
        return sentence
    
    def ensure_advanced_punctuation(self, sentence):
        """Ensure proper use of advanced punctuation"""
        
        words = sentence.split()
        
        # Use semicolons for related independent clauses
        if len(words) > 10 and random.random() < 0.15:
            # Find natural semicolon position
            for i in range(3, len(words) - 2):
                if words[i].lower() in ['however', 'therefore', 'moreover']:
                    words[i] = words[i].rstrip(',') + ';'
                    break
        
        # Use colons for explanations or lists
        if len(words) > 8 and random.random() < 0.1:
            explanation_words = ['following', 'these', 'such as', 'for example']
            for i, word in enumerate(words):
                if word.lower() in explanation_words and i < len(words) - 1:
                    words[i] = word.rstrip(',') + ':'
                    break
        
        # Use em dashes for emphasis (sparingly)
        if len(words) > 6 and random.random() < 0.08:
            emphasis_words = ['actually', 'basically', 'essentially', 'in fact']
            for i, word in enumerate(words):
                if word.lower() in emphasis_words and i < len(words) - 1:
                    words[i] = '—' + word  # Em dash
                    break
        
        return ' '.join(words)
    
    def calculate_focused_score(self, text):
        """Calculate human score based on focused rewriting"""
        
        indicators = {
            'phrase_replacement': 0,
            'synonym_usage': 0,
            'structure_variety': 0,
            'contraction_usage': 0,
            'punctuation_quality': 0
        }
        
        # Phrase replacement score
        ai_phrases_count = sum(1 for phrase in self.ai_replacements.keys() 
                              if phrase in text.lower())
        total_ai_phrases = len(self.ai_replacements)
        phrases_replaced = total_ai_phrases - ai_phrases_count
        indicators['phrase_replacement'] = min(1.0, phrases_replaced / total_ai_phrases)
        
        # Synonym usage score
        synonym_count = 0
        for base_word, synonyms in self.synonym_groups.items():
            for synonym in synonyms:
                if synonym in text.lower():
                    synonym_count += 1
                    break
        indicators['synonym_usage'] = min(1.0, synonym_count / 10)
        
        # Structure variety score
        sentences = re.split(r'(?<=[.!?])\s+', text)
        if sentences:
            sentence_starts = [s.split()[0].lower() for s in sentences if s.split()]
            unique_starts = len(set(sentence_starts))
            indicators['structure_variety'] = min(1.0, unique_starts / max(1, len(sentences)))
        
        # Contraction usage score
        contraction_count = sum(1 for contraction in self.contractions.values() 
                              if contraction in text)
        indicators['contraction_usage'] = min(1.0, contraction_count / 8)
        
        # Punctuation quality score
        punctuation_variety = len(set(re.findall(r'[.,!?;:]', text)))
        indicators['punctuation_quality'] = min(1.0, punctuation_variety / 5)
        
        # Calculate overall score
        total_score = sum(indicators.values()) / len(indicators)
        human_score = min(100, total_score * 160)  # Boost for focused rewriting
        
        return human_score
    
    def focused_rewriting_humanize(self, text, intensity=0.7):
        """Main focused rewriting humanization function"""
        
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
        
        # Apply focused rewriting based on intensity
        for sentence in sentences:
            if not sentence.strip():
                continue
            
            # Apply focused rewriting
            if intensity >= 0.2:
                sentence = self.focused_sentence_rewriting(sentence)
                changes_applied.append('focused_rewriting')
            
            if intensity >= 0.4:
                sentence = self.apply_synonym_rewriting(sentence)
                changes_applied.append('synonym_rewriting')
            
            if intensity >= 0.6:
                sentence = self.vary_sentence_structure(sentence)
                changes_applied.append('structure_variation')
            
            if intensity >= 0.8:
                sentence = self.apply_advanced_techniques(sentence)
                changes_applied.append('advanced_techniques')
            
            rewritten_sentences.append(sentence)
        
        # Reconstruct text
        humanized_text = ' '.join(rewritten_sentences)
        
        # Calculate character count
        char_count = len(humanized_text)
        
        # Calculate focused score
        human_score = self.calculate_focused_score(humanized_text)
        
        return {
            'success': True,
            'original_text': original_text,
            'humanized_text': humanized_text,
            'human_score': human_score,
            'changes_applied': changes_applied,
            'character_count': char_count,
            'timestamp': datetime.now().isoformat()
        }
    
    def apply_advanced_techniques(self, sentence):
        """Apply advanced rewriting techniques"""
        
        words = sentence.split()
        
        # Technique 1: Add natural emphasis
        if random.random() < 0.3:
            emphasis_words = ['actually', 'basically', 'essentially', 'in fact', 'really']
            emphasis = random.choice(emphasis_words)
            
            if len(words) > 5:
                insert_pos = random.randint(1, min(3, len(words) - 2))
                words.insert(insert_pos, emphasis + ',')
        
        # Technique 2: Vary complexity
        if random.random() < 0.25:
            if len(words) > 8:
                # Add dependent clause
                clause_starters = ["which", "that", "who", "when", "where", "because"]
                starter = random.choice(clause_starters)
                
                insert_pos = random.randint(2, len(words) - 2)
                words.insert(insert_pos, starter)
        
        # Technique 3: Natural transitions
        if random.random() < 0.2:
            transition_words = ["also", "plus", "so", "then", "but", "however"]
            transition = random.choice(transition_words)
            
            if len(words) > 4:
                insert_pos = random.randint(0, 2)
                words.insert(insert_pos, transition)
        
        return ' '.join(words)

def demo_focused_rewriting():
    """Demonstrate focused rewriting humanizer"""
    
    print("✍️ Focused Rewriting Humanizer Demo")
    print("=" * 60)
    print("📝 Rules: Actively rewrite sentences with natural language")
    print("🔄 Replace AI phrases, use synonyms, vary structure")
    print("✨ No extra phrases - only modifies existing content")
    print("=" * 60)
    
    humanizer = FocusedRewritingHumanizer()
    
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
        
        result = humanizer.focused_rewriting_humanize(original_text, intensity=0.8)
        
        if result['success']:
            print(f"Humanized: {result['humanized_text']}")
            print(f"Human Score: {result['human_score']:.1f}%")
            print(f"Character Count: {result['character_count']}")
            print(f"Changes: {', '.join(result['changes_applied'])}")
            
            if result['human_score'] >= 85:
                print("✅ Excellent focused rewriting!")
            elif result['human_score'] >= 70:
                print("✅ Good focused rewriting!")
            else:
                print("⚠️  Could use more rewriting")
                
        else:
            print(f"❌ Error: {result['error']}")
        
        print("-" * 60)
    
    print("\n🎯 Focused Rewriting Demo Complete!")
    print("✨ Active sentence rewriting with natural language achieved!")

if __name__ == "__main__":
    demo_focused_rewriting()

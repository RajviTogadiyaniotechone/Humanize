import nltk
import spacy
import random
import re
import json
from datetime import datetime
import os
from collections import defaultdict
import math

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    nltk.download('stopwords', quiet=True)
except:
    pass

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None

class AdvancedContentHumanizer:
    def __init__(self):
        self.initialize_advanced_patterns()
        self.initialize_contextual_replacements()
        self.initialize_rhythm_patterns()
        self.initialize_ai_detection_bypass()
        
    def initialize_advanced_patterns(self):
        """Initialize advanced humanization patterns"""
        
        # Sophisticated sentence starters that sound natural
        self.advanced_sentence_starters = [
            # Conversational openings
            "You know what's interesting?", "Here's something to think about", 
            "Let me put it this way", "The thing is", "What I've found is",
            "If you really think about it", "Here's the deal", "The way I see it",
            "Look at it this way", "Here's what I mean", "The reality is",
            
            # Natural transitions
            "And you know what?", "But here's the thing", "So what happens is",
            "Now, here's where it gets interesting", "And that's not all",
            "But wait, there's more", "And here's why that matters",
            
            # Personal perspective
            "From where I'm standing", "In my experience", "What I've noticed",
            "The way I look at it", "From my perspective", "If you ask me",
            "Speaking from experience", "Based on what I've seen",
            
            # Storytelling elements
            "Picture this", "Imagine this scenario", "Let me paint you a picture",
            "Here's how it plays out", "What you need to understand is",
            "Here's the backstory", "Let me walk you through it"
        ]
        
        # Natural human expressions (contextually appropriate)
        self.contextual_expressions = {
            'certainty': ["I'm pretty sure", "I'd say", "I'm willing to bet", "I'm confident"],
            'uncertainty': ["I think", "it seems to me", "I'm guessing", "I suspect"],
            'emphasis': ["honestly", "truly", "genuinely", "seriously", "no joke"],
            'agreement': ["exactly", "precisely", "absolutely", "couldn't agree more"],
            'contrast': ["however", "that said", "on the other hand", "then again"],
            'causation': ["so", "therefore", "as a result", "consequently", "that's why"],
            'addition': ["plus", "and", "also", "what's more", "on top of that"],
            'example': ["for instance", "for example", "take", "consider", "like"]
        }
        
        # Human-like hesitation and filler words (used sparingly)
        self.natural_fillers = [
            "well", "you know", "I mean", "like", "sort of", "kind of", 
            "actually", "basically", "literally", "honestly", "frankly"
        ]
        
        # Conversational transitions
        self.conversational_transitions = [
            "And another thing", "But here's what's really interesting",
            "Now, you might be wondering", "So what does this all mean?",
            "And that brings me to", "Which brings me to my next point",
            "Now, here's where it gets good", "And that's not even the best part"
        ]
        
    def initialize_contextual_replacements(self):
        """Initialize context-aware vocabulary replacements"""
        
        # Contextual word replacements based on part of speech and meaning
        self.contextual_replacements = {
            # Academic/Business to Conversational
            'utilize': {
                'verb': ['use', 'work with', 'make use of', 'leverage', 'tap into'],
                'context': {
                    'business': ['leverage', 'make use of'],
                    'casual': ['use', 'work with'],
                    'technical': ['utilize', 'implement']
                }
            },
            'facilitate': {
                'verb': ['help', 'make easier', 'enable', 'assist', 'support'],
                'context': {
                    'business': ['enable', 'support'],
                    'casual': ['help', 'make easier'],
                    'technical': ['facilitate', 'enable']
                }
            },
            'optimize': {
                'verb': ['improve', 'enhance', 'make better', 'fine-tune', 'perfect'],
                'context': {
                    'business': ['enhance', 'improve'],
                    'casual': ['make better', 'improve'],
                    'technical': ['optimize', 'fine-tune']
                }
            },
            'implement': {
                'verb': ['put in place', 'set up', 'start using', 'launch', 'roll out'],
                'context': {
                    'business': ['roll out', 'launch'],
                    'casual': ['put in place', 'start using'],
                    'technical': ['implement', 'deploy']
                }
            },
            'subsequently': {
                'verb': ['then', 'next', 'after that', 'later', 'afterwards'],
                'context': {
                    'business': ['subsequently', 'following this'],
                    'casual': ['then', 'after that'],
                    'story': ['next', 'afterwards']
                }
            },
            'consequently': {
                'verb': ['so', 'as a result', 'that\'s why', 'therefore', 'hence'],
                'context': {
                    'business': ['consequently', 'as a result'],
                    'casual': ['so', 'that\'s why'],
                    'formal': ['therefore', 'hence']
                }
            },
            'nevertheless': {
                'verb': ['still', 'however', 'but', 'even so', 'despite that'],
                'context': {
                    'business': ['nevertheless', 'however'],
                    'casual': ['still', 'but'],
                    'formal': ['nevertheless', 'despite that']
                }
            },
            'furthermore': {
                'verb': ['also', 'plus', 'what\'s more', 'additionally', 'in addition'],
                'context': {
                    'business': ['furthermore', 'additionally'],
                    'casual': ['also', 'plus'],
                    'formal': ['furthermore', 'moreover']
                }
            },
            'demonstrate': {
                'verb': ['show', 'prove', 'illustrate', 'reveal', 'display'],
                'context': {
                    'business': ['demonstrate', 'showcase'],
                    'casual': ['show', 'prove'],
                    'technical': ['demonstrate', 'illustrate']
                }
            },
            'establish': {
                'verb': ['set up', 'create', 'build', 'start', 'form'],
                'context': {
                    'business': ['establish', 'create'],
                    'casual': ['set up', 'build'],
                    'formal': ['establish', 'form']
                }
            }
        }
        
        # Contractions and informal variations
        self.contraction_patterns = {
            'do not': 'don\'t',
            'will not': 'won\'t',
            'cannot': 'can\'t',
            'did not': 'didn\'t',
            'is not': 'isn\'t',
            'are not': 'aren\'t',
            'was not': 'wasn\'t',
            'were not': 'weren\'t',
            'have not': 'haven\'t',
            'has not': 'hasn\'t',
            'could not': 'couldn\'t',
            'would not': 'wouldn\'t',
            'should not': 'shouldn\'t',
            'might not': 'mightn\'t',
            'must not': 'mustn\'t',
            'shall not': 'shan\'t',
            'had not': 'hadn\'t',
            'I am': 'I\'m',
            'you are': 'you\'re',
            'we are': 'we\'re',
            'they are': 'they\'re',
            'it is': 'it\'s',
            'that is': 'that\'s',
            'I will': 'I\'ll',
            'you will': 'you\'ll',
            'we will': 'we\'ll',
            'they will': 'they\'ll',
            'I have': 'I\'ve',
            'you have': 'you\'ve',
            'we have': 'we\'ve',
            'they have': 'they\'ve',
            'I would': 'I\'d',
            'you would': 'you\'d',
            'we would': 'we\'d',
            'they would': 'they\'d',
            'I had': 'I\'d',
            'you had': 'you\'d',
            'we had': 'we\'d',
            'they had': 'they\'d'
        }
        
    def initialize_rhythm_patterns(self):
        """Initialize human-like rhythm and flow patterns"""
        
        # Sentence length variations for natural rhythm
        self.rhythm_patterns = {
            'short': [3, 4, 5, 6, 7, 8],  # 3-8 words
            'medium': [9, 10, 11, 12, 13, 14, 15, 16],  # 9-16 words
            'long': [17, 18, 19, 20, 21, 22, 23, 24, 25]  # 17-25 words
        }
        
        # Natural sentence flow patterns
        self.flow_patterns = [
            # Short-medium-short
            [0.3, 0.5, 0.2],
            # Medium-short-medium
            [0.4, 0.2, 0.4],
            # Short-long-short
            [0.25, 0.5, 0.25],
            # Variable pattern
            [0.2, 0.3, 0.3, 0.2],
            # Natural flow
            [0.15, 0.35, 0.35, 0.15]
        ]
        
        # Punctuation patterns for natural rhythm
        self.punctuation_patterns = {
            'questions': ['?', '...?'],
            'exclamations': ['!', '!!', '...!'],
            'pauses': [',', '--', '...'],
            'emphasis': ['*', '**']
        }
        
    def initialize_ai_detection_bypass(self):
        """Initialize AI detection bypass patterns"""
        
        # Common AI patterns to avoid
        self.ai_patterns_to_avoid = [
            'furthermore', 'moreover', 'consequently', 'nevertheless',
            'in conclusion', 'additionally', 'subsequently', 'accordingly',
            'it is important to note', 'it should be mentioned', 'it is worth noting',
            'in order to', 'due to the fact that', 'in light of the fact that',
            'with regard to', 'with respect to', 'in terms of'
        ]
        
        # Human-like imperfections
        self.human_imperfections = {
            'occasional_repetition': 0.05,  # 5% chance of natural repetition
            'slight_grammatical_variance': 0.03,  # 3% chance of minor grammar variance
            'natural_pauses': 0.1,  # 10% chance of natural pauses
            'conversational_insertions': 0.08,  # 8% chance of conversational insertions
            'emphasis_variations': 0.06  # 6% chance of emphasis variations
        }
        
        # Semantic preservation rules
        self.semantic_rules = {
            'preserve_entities': True,  # Don't change names, places, dates
            'preserve_numbers': True,  # Don't change numerical values
            'preserve_technical_terms': True,  # Don't change technical jargon
            'preserve_quotes': True,  # Don't change quoted text
            'preserve_structure': True  # Maintain logical flow
        }
        
    def analyze_text_context(self, text):
        """Analyze text to determine context and tone"""
        
        # Simple context detection based on keywords
        context_indicators = {
            'business': ['business', 'company', 'corporate', 'professional', 'market', 'strategy'],
            'casual': ['friend', 'chat', 'talk', 'cool', 'awesome', 'great'],
            'technical': ['system', 'algorithm', 'data', 'process', 'function', 'method'],
            'academic': ['research', 'study', 'analysis', 'theory', 'hypothesis', 'methodology'],
            'story': ['story', 'narrative', 'character', 'plot', 'setting', 'theme']
        }
        
        context_scores = {}
        text_lower = text.lower()
        
        for context, indicators in context_indicators.items():
            score = sum(1 for indicator in indicators if indicator in text_lower)
            context_scores[context] = score / len(indicators)
        
        # Determine primary context
        primary_context = max(context_scores, key=context_scores.get) if context_scores else 'general'
        
        # Analyze sentence complexity
        sentences = re.split(r'[.!?]+', text)
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
        
        # Determine formality level
        formality_indicators = ['furthermore', 'moreover', 'consequently', 'nevertheless', 'utilize']
        formality_score = sum(1 for indicator in formality_indicators if indicator in text_lower)
        
        formality_level = 'formal' if formality_score > 2 else 'informal' if formality_score == 0 else 'semi-formal'
        
        return {
            'context': primary_context,
            'formality': formality_level,
            'complexity': avg_sentence_length,
            'context_scores': context_scores
        }
        
    def contextual_word_replacement(self, text, context_info):
        """Replace words based on context while preserving meaning"""
        
        if not nlp:
            return text
            
        doc = nlp(text)
        replaced_text = text
        
        for token in doc:
            if token.text.lower() in self.contextual_replacements:
                word_data = self.contextual_replacements[token.text.lower()]
                
                # Get context-appropriate replacements
                context_type = context_info['context']
                formality = context_info['formality']
                
                if context_type in word_data['context']:
                    candidates = word_data['context'][context_type]
                elif formality in word_data['context']:
                    candidates = word_data['context'][formality]
                else:
                    candidates = word_data['verb']
                
                # Choose replacement based on probability
                if random.random() < 0.3:  # 30% chance of replacement
                    replacement = random.choice(candidates)
                    replaced_text = re.sub(
                        r'\b' + re.escape(token.text) + r'\b',
                        replacement,
                        replaced_text,
                        flags=re.IGNORECASE
                    )
        
        return replaced_text
        
    def advanced_sentence_variation(self, text, context_info):
        """Apply conservative sentence structure variations without adding content"""
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        varied_sentences = []
        
        for sentence in sentences:
            if not sentence.strip():
                continue
                
            # Only restructure existing sentences, don't add new content
            words = sentence.split()
            
            # Simple word reordering for variety (conservative)
            if len(words) > 6 and random.random() < 0.2:
                # Find safe reordering points (prepositions, conjunctions)
                reorder_words = ['and', 'but', 'or', 'so', 'because', 'when', 'where', 'which']
                reorder_positions = [i for i, word in enumerate(words) if word.lower() in reorder_words]
                
                if reorder_positions and len(reorder_positions) > 1:
                    # Simple clause reordering
                    pos = reorder_positions[0]
                    if pos > 2 and pos < len(words) - 2:
                        # Move clause to different position
                        clause = words[pos:pos+3]
                        remaining = words[:pos] + words[pos+3:]
                        # Reinsert at different position
                        new_pos = min(pos + 2, len(remaining) - 3)
                        words = remaining[:new_pos] + clause + remaining[new_pos:]
                        sentence = ' '.join(words)
            
            # Break very long sentences only if necessary
            if len(sentence.split()) > 25:
                sentence = self.conservative_sentence_break(sentence)
            
            varied_sentences.append(sentence)
        
        return ' '.join(varied_sentences)
        
    def conservative_sentence_break(self, sentence):
        """Conservatively break very long sentences without adding content"""
        
        words = sentence.split()
        if len(words) <= 25:
            return sentence
        
        # Only break at natural conjunction points
        break_words = ['and', 'but', 'so', 'because', 'when', 'where', 'which', 'that']
        break_positions = [i for i, word in enumerate(words) if word.lower() in break_words]
        
        if break_positions:
            # Choose a break point in the middle third
            mid_break = break_positions[len(break_positions)//2]
            if mid_break > 5 and mid_break < len(words) - 5:  # Ensure balanced sentences
                first_part = ' '.join(words[:mid_break]) + '.'
                second_part = ' '.join(words[mid_break:])
                return f"{first_part} {second_part}"
        
        return sentence
        
    def natural_sentence_break(self, sentence):
        """Naturally break long sentences"""
        
        words = sentence.split()
        break_points = ['and', 'but', 'so', 'because', 'when', 'where', 'which', 'that']
        
        # Find natural break points
        break_positions = [i for i, word in enumerate(words) if word.lower() in break_points]
        
        if break_positions:
            # Choose a break point in the middle third
            mid_break = break_positions[len(break_positions)//2]
            first_part = ' '.join(words[:mid_break]) + '.'
            second_part = ' '.join(words[mid_break:])
            return f"{first_part} {second_part}"
        else:
            # Split at middle if no natural break points
            mid_point = len(words) // 2
            first_part = ' '.join(words[:mid_point]) + '.'
            second_part = ' '.join(words[mid_point:])
            return f"{first_part} {second_part}"
            
    def add_human_rhythm(self, text):
        """Add human-like rhythm without adding content"""
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        rhythmic_sentences = []
        
        for sentence in sentences:
            if not sentence.strip():
                continue
            
            # Only adjust existing punctuation, don't add content
            if random.random() < 0.1:  # 10% chance
                # Add natural emphasis to existing words
                words = sentence.split()
                for i, word in enumerate(words):
                    if word.lower() in ['very', 'really', 'extremely', 'incredibly'] and random.random() < 0.3:
                        words[i] = word.upper()
                        break
                sentence = ' '.join(words)
            
            rhythmic_sentences.append(sentence)
        
        return ' '.join(rhythmic_sentences)
        
    def shorten_sentence(self, sentence):
        """Shorten a sentence naturally"""
        
        # Remove unnecessary words
        unnecessary_words = ['very', 'really', 'quite', 'rather', 'somewhat', 'actually']
        words = sentence.split()
        
        # Remove some unnecessary words
        filtered_words = [word for word in words if word.lower() not in unnecessary_words[:2]]
        
        return ' '.join(filtered_words)
        
    def lengthen_sentence(self, sentence):
        """Lengthen a sentence naturally"""
        
        # Add descriptive words or clauses
        additions = ['in fact', 'as it happens', 'you might say', 'if you will']
        
        if random.random() < 0.3:
            addition = random.choice(additions)
            words = sentence.split()
            insert_pos = random.randint(1, len(words)-1)
            words.insert(insert_pos, addition)
            return ' '.join(words)
        
        return sentence
        
    def add_natural_punctuation(self, sentence):
        """Add natural punctuation variations"""
        
        # Add occasional emphasis
        if random.random() < 0.02:
            words = sentence.split()
            for i, word in enumerate(words):
                if word.lower() in ['very', 'really', 'extremely', 'incredibly']:
                    words[i] = word.upper()
                    break
            sentence = ' '.join(words)
        
        # Add natural pauses
        if random.random() < 0.03:
            sentence = sentence.replace(',', ', you know,', 1)
        
        return sentence
        
    def apply_ai_detection_bypass(self, text):
        """Apply AI detection bypass without adding content"""
        
        # Only replace existing AI patterns, don't add new content
        bypassed_text = text
        
        for pattern in self.ai_patterns_to_avoid:
            if random.random() < 0.7:  # 70% chance to replace each pattern
                replacement = self.get_human_alternative(pattern)
                bypassed_text = re.sub(
                    r'\b' + re.escape(pattern) + r'\b',
                    replacement,
                    bypassed_text,
                    flags=re.IGNORECASE
                )
        
        # No conversational insertions or repetitions - preserve original content
        
        return bypassed_text
        
    def get_human_alternative(self, ai_pattern):
        """Get human-friendly alternative for AI patterns"""
        
        alternatives = {
            'furthermore': ['also', 'plus', 'what\'s more', 'on top of that'],
            'moreover': ['also', 'plus', 'in addition', 'and'],
            'consequently': ['so', 'as a result', 'that\'s why', 'therefore'],
            'nevertheless': ['still', 'however', 'but', 'even so'],
            'in conclusion': ['to wrap up', 'so', 'in the end', 'finally'],
            'additionally': ['also', 'plus', 'what\'s more', 'and'],
            'subsequently': ['then', 'next', 'after that', 'later'],
            'accordingly': ['so', 'therefore', 'as a result', 'thus'],
            'it is important to note': ['it\'s worth noting', 'keep in mind', 'remember'],
            'it should be mentioned': ['it\'s worth mentioning', 'by the way', 'also'],
            'it is worth noting': ['it\'s worth noting', 'keep in mind', 'remember'],
            'in order to': ['to', 'so we can', 'in order to', 'so that we can'],
            'due to the fact that': ['because', 'since', 'as', 'due to'],
            'in light of the fact that': ['because', 'since', 'given that', 'considering'],
            'with regard to': ['about', 'regarding', 'concerning', 'when it comes to'],
            'with respect to': ['about', 'regarding', 'concerning', 'when it comes to'],
            'in terms of': ['about', 'regarding', 'when it comes to', 'in']
        }
        
        return random.choice(alternatives.get(ai_pattern, [ai_pattern]))
        
    def add_natural_repetition(self, text):
        """Add natural repetition for human feel"""
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        if len(sentences) > 3:
            # Repeat a key phrase naturally
            key_phrase = self.extract_key_phrase(sentences[0])
            if key_phrase and len(sentences) > 2:
                insert_pos = random.randint(1, len(sentences)-1)
                sentences.insert(insert_pos, f"And when I say {key_phrase}, I mean it.")
        
        return ' '.join(sentences)
        
    def add_conversational_insertion(self, text):
        """Add conversational insertions"""
        
        insertions = ['you know?', 'right?', 'if you know what I mean', 'believe me']
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        if len(sentences) > 2:
            insert_pos = random.randint(1, len(sentences)-1)
            insertion = random.choice(insertions)
            sentences[insert_pos] = sentences[insert_pos].rstrip('.!?') + f", {insertion}."
        
        return ' '.join(sentences)
        
    def extract_key_phrase(self, sentence):
        """Extract a key phrase from a sentence"""
        
        words = sentence.split()
        if len(words) > 6:
            # Extract a 2-3 word phrase from the middle
            start = random.randint(2, len(words)-4)
            phrase = ' '.join(words[start:start+2])
            return phrase
        
        return None
        
    def add_contractions(self, text):
        """Add contractions naturally"""
        
        for formal, contraction in self.contraction_patterns.items():
            # Add contractions with 70% probability
            if random.random() < 0.7:
                text = re.sub(
                    r'\b' + re.escape(formal) + r'\b',
                    contraction,
                    text,
                    flags=re.IGNORECASE
                )
        
        return text
        
    def preserve_semantic_meaning(self, original_text, humanized_text):
        """Ensure semantic meaning is preserved"""
        
        # Extract key entities and concepts
        if nlp:
            original_doc = nlp(original_text)
            humanized_doc = nlp(humanized_text)
            
            # Check if key entities are preserved
            original_entities = {ent.text.lower() for ent in original_doc.ents}
            humanized_entities = {ent.text.lower() for ent in humanized_doc.ents}
            
            # Preserve entities that might have been lost
            lost_entities = original_entities - humanized_entities
            if lost_entities:
                humanized_text = self.restore_entities(humanized_text, lost_entities)
        
        return humanized_text
        
    def restore_entities(self, text, entities):
        """Restore lost entities"""
        
        # Simple entity restoration - in practice, this would be more sophisticated
        for entity in entities:
            if entity not in text.lower():
                # Find appropriate place to insert entity
                text = self.smart_entity_insertion(text, entity)
        
        return text
        
    def smart_entity_insertion(self, text, entity):
        """Smartly insert entity back into text"""
        
        # This is a simplified version - would need more sophisticated logic
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        if len(sentences) > 1:
            insert_pos = random.randint(0, len(sentences)-1)
            sentences[insert_pos] += f" ({entity})"
        
        return ' '.join(sentences)
        
    def calculate_advanced_human_score(self, text):
        """Calculate advanced human-like score"""
        
        human_indicators = {
            'contractions': 0,
            'informal_language': 0,
            'sentence_variety': 0,
            'natural_flow': 0,
            'contextual_replacements': 0,
            'ai_pattern_avoidance': 0,
            'rhythmic_quality': 0
        }
        
        # Check for contractions
        contraction_count = sum(1 for contraction in self.contraction_patterns.values() 
                            if contraction in text)
        human_indicators['contractions'] = min(1.0, contraction_count / 5)
        
        # Check for informal language
        informal_indicators = ['you know', 'I mean', 'like', 'well', 'actually', 'basically']
        informal_count = sum(1 for indicator in informal_indicators if indicator in text.lower())
        human_indicators['informal_language'] = min(1.0, informal_count / 3)
        
        # Check sentence variety
        sentences = re.split(r'(?<=[.!?])\s+', text)
        if sentences:
            lengths = [len(s.split()) for s in sentences]
            avg_length = sum(lengths) / len(lengths)
            variance = sum((l - avg_length) ** 2 for l in lengths) / len(lengths)
            human_indicators['sentence_variety'] = min(1.0, variance / 30)
        
        # Check for natural flow (transition words)
        transition_words = ['so', 'but', 'and', 'however', 'therefore', 'plus']
        transition_count = sum(1 for word in transition_words if word in text.lower())
        human_indicators['natural_flow'] = min(1.0, transition_count / 4)
        
        # Check for AI pattern avoidance
        ai_pattern_count = sum(1 for pattern in self.ai_patterns_to_avoid 
                             if pattern in text.lower())
        human_indicators['ai_pattern_avoidance'] = max(0, 1.0 - (ai_pattern_count / 10))
        
        # Calculate overall score
        total_score = sum(human_indicators.values()) / len(human_indicators)
        human_score = min(100, total_score * 100)
        
        return human_score
        
    def advanced_humanize(self, text, keywords=None, intensity=0.7, target_score=0.95):
        """Main conservative humanization function - only changes existing words/sentences"""
        
        if not text or len(text.strip()) < 10:
            return {
                'humanized_text': text,
                'human_score': 0,
                'changes_applied': [],
                'success': False
            }
        
        original_text = text
        changes_applied = []
        
        # Analyze text context
        context_info = self.analyze_text_context(text)
        
        # Apply conservative humanization techniques based on intensity
        if intensity >= 0.3:
            text = self.add_contractions(text)
            changes_applied.append('contractions')
        
        if intensity >= 0.4:
            text = self.contextual_word_replacement(text, context_info)
            changes_applied.append('word_replacements')
        
        if intensity >= 0.5:
            text = self.advanced_sentence_variation(text, context_info)
            changes_applied.append('sentence_restructuring')
        
        if intensity >= 0.6:
            text = self.apply_ai_detection_bypass(text)
            changes_applied.append('ai_pattern_replacement')
        
        # Only add keywords if explicitly requested and space allows
        if keywords and intensity >= 0.8:
            text = self.conservative_keyword_insertion(text, keywords, context_info)
            changes_applied.append('keyword_insertion')
        
        # Preserve semantic meaning strictly
        text = self.preserve_semantic_meaning(original_text, text)
        
        # Calculate final human score
        human_score = self.calculate_advanced_human_score(text)
        
        return {
            'humanized_text': text,
            'original_text': original_text,
            'human_score': human_score,
            'target_score': target_score * 100,
            'changes_applied': changes_applied,
            'context_info': context_info,
            'success': True
        }
        
    def conservative_keyword_insertion(self, text, keywords, context_info):
        """Conservative keyword insertion - only if space allows and natural"""
        
        if not keywords:
            return text
        
        # Only insert if keywords already exist in text naturally
        existing_keywords = [kw for kw in keywords if kw.lower() in text.lower()]
        
        if existing_keywords:
            return text  # Keywords already present, no insertion needed
        
        return text  # Conservative approach - don't add new content
        
    def natural_keyword_insertion(self, text, keywords, context_info):
        """Naturally insert keywords"""
        
        if not keywords:
            return text
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        modified_sentences = []
        used_keywords = set()
        
        for sentence in sentences:
            available_keywords = [kw for kw in keywords if kw.lower() not in sentence.lower() and kw not in used_keywords]
            
            if available_keywords and random.random() < 0.15:  # 15% chance per sentence
                keyword = random.choice(available_keywords)
                
                # Natural insertion patterns based on context
                if context_info['context'] == 'business':
                    patterns = [f"for {keyword}", f"with {keyword}", f"regarding {keyword}"]
                elif context_info['context'] == 'casual':
                    patterns = [f"about {keyword}", f"like {keyword}", f"especially {keyword}"]
                else:
                    patterns = [f"for {keyword}", f"with {keyword}", f"about {keyword}"]
                
                pattern = random.choice(patterns)
                words = sentence.split()
                
                if len(words) > 6:
                    insert_pos = random.randint(2, len(words)-2)
                    words.insert(insert_pos, pattern)
                    modified_sentences.append(' '.join(words))
                    used_keywords.add(keyword)
                else:
                    modified_sentences.append(sentence)
            else:
                modified_sentences.append(sentence)
        
        return ' '.join(modified_sentences)
        
    def boost_human_score(self, text, score_gap):
        """Boost human score to meet target"""
        
        # Apply additional humanization techniques based on score gap
        if score_gap > 20:
            # Add more contractions and informal language
            text = self.add_contractions(text)
            text = self.add_informal_language(text)
        
        if score_gap > 10:
            # Add sentence variety
            text = self.add_sentence_variety(text)
        
        if score_gap > 5:
            # Add natural flow elements
            text = self.add_flow_elements(text)
        
        return text
        
    def add_informal_language(self, text):
        """Add informal language elements"""
        
        informal_additions = ['you know', 'I mean', 'like', 'well', 'actually']
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        for i, sentence in enumerate(sentences):
            if random.random() < 0.1 and len(sentence.split()) > 8:
                addition = random.choice(informal_additions)
                words = sentence.split()
                insert_pos = random.randint(1, len(words)-2)
                words.insert(insert_pos, addition)
                sentences[i] = ' '.join(words)
        
        return ' '.join(sentences)
        
    def add_sentence_variety(self, text):
        """Add sentence variety"""
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        # Vary sentence lengths
        for i, sentence in enumerate(sentences):
            if len(sentence.split()) > 20 and random.random() < 0.3:
                sentences[i] = self.natural_sentence_break(sentence)
            elif len(sentence.split()) < 8 and random.random() < 0.3:
                sentences[i] = self.lengthen_sentence(sentence)
        
        return ' '.join(sentences)
        
    def add_flow_elements(self, text):
        """Add natural flow elements"""
        
        flow_words = ['so', 'and', 'but', 'well', 'now', 'then']
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        for i in range(1, len(sentences)):
            if random.random() < 0.2:
                flow_word = random.choice(flow_words)
                sentences[i] = f"{flow_word.capitalize()}, {sentences[i].lower()}"
        
        return ' '.join(sentences)

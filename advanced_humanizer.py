import re
import random
import numpy as np
from collections import Counter
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob
import spacy
from typing import List, Dict, Tuple
import markovify
import yake

class AdvancedContentHumanizer:
    def __init__(self):
        # Load advanced models
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            self.nlp = None
            
        # Human-like patterns
        self.filler_words = [
            "you know", "I mean", "like", "basically", "actually", "honestly",
            "to be fair", "if you think about it", "at the end of the day",
            "the thing is", "what happens is", "the reality is"
        ]
        
        self.transition_phrases = [
            "and what's more", "on top of that", "not to mention", "as it turns out",
            "believe it or not", "funnily enough", "coincidentally", "speaking of which",
            "that reminds me", "while we're on the subject", "in the same vein"
        ]
        
        self.conversational_starters = [
            "let me tell you something", "here's the deal", "the way I see it",
            "if you ask me", "from where I'm standing", "in my experience",
            "what I've found is", "the funny thing is", "it's interesting because"
        ]
        
        self.emotional_words = [
            "absolutely", "definitely", "completely", "totally", "literally",
            "seriously", "honestly", "truly", "genuinely", "really"
        ]
        
        self.informal_connectors = [
            "plus", "so", "and", "but", "cause", "cuz", "though", "anyway"
        ]
    
    def analyze_ai_patterns(self, text: str) -> Dict:
        """Analyze text for AI-like patterns"""
        blob = TextBlob(text)
        sentences = blob.sentences
        
        patterns = {
            'perfect_grammar': 0,
            'uniform_length': 0,
            'formal_words': 0,
            'no_contractions': 0,
            'repetitive_structure': 0,
            'complex_sentences': 0
        }
        
        # Check for perfect grammar indicators
        formal_words = ['furthermore', 'moreover', 'consequently', 'nevertheless']
        patterns['formal_words'] = sum(1 for word in formal_words if word in text.lower())
        
        # Check sentence length uniformity
        lengths = [len(sent.words) for sent in sentences]
        if lengths:
            avg_length = np.mean(lengths)
            variance = np.var(lengths)
            patterns['uniform_length'] = 1 if variance < 25 else 0
        
        # Check for contractions
        contractions = ["n't", "'ll", "'ve", "'re", "'m"]
        patterns['no_contractions'] = 1 if not any(contr in text for contr in contractions) else 0
        
        # Check for complex sentences
        patterns['complex_sentences'] = sum(1 for length in lengths if length > 25)
        
        return patterns
    
    def add_human_variations(self, text: str) -> str:
        """Add human-like variations to text"""
        sentences = sent_tokenize(text)
        modified_sentences = []
        
        for i, sentence in enumerate(sentences):
            # Add filler words occasionally
            if random.random() < 0.15 and len(sentence.split()) > 8:
                filler = random.choice(self.filler_words)
                words = sentence.split()
                insert_pos = random.randint(1, len(words) - 2)
                words.insert(insert_pos, filler)
                sentence = ' '.join(words)
            
            # Add emotional emphasis
            if random.random() < 0.1:
                emotional = random.choice(self.emotional_words)
                sentence = f"{emotional}, {sentence}"
            
            # Add conversational starters
            if random.random() < 0.08 and i > 0:
                starter = random.choice(self.conversational_starters)
                sentence = f"{starter}, {sentence}"
            
            modified_sentences.append(sentence)
        
        return ' '.join(modified_sentences)
    
    def vary_sentence_patterns(self, text: str) -> str:
        """Vary sentence patterns to sound more natural"""
        if self.nlp is None:
            return text
            
        doc = self.nlp(text)
        sentences = list(doc.sents)
        varied_sentences = []
        
        for i, sent in enumerate(sentences):
            text = sent.text
            
            # Add transitions between sentences
            if i > 0 and random.random() < 0.25:
                transition = random.choice(self.transition_phrases)
                text = f"{transition}, {text.lower()}"
            
            # Vary sentence beginnings
            if random.random() < 0.2:
                words = text.split()
                if len(words) > 5:
                    # Move a phrase to the beginning
                    if "because" in text.lower():
                        text = re.sub(r'\bbecause\b', 'Because', text, count=1)
                    elif "when" in text.lower():
                        text = re.sub(r'\bwhen\b', 'When', text, count=1)
            
            # Add rhetorical questions
            if random.random() < 0.05:
                text += ", right?" if random.random() < 0.5 else ", you know?"
            
            varied_sentences.append(text)
        
        return ' '.join(varied_sentences)
    
    def naturalize_vocabulary(self, text: str) -> str:
        """Replace formal words with natural alternatives"""
        formal_to_informal = {
            'furthermore': 'plus',
            'moreover': 'also',
            'consequently': 'so',
            'therefore': 'that\'s why',
            'nevertheless': 'still',
            'however': 'but',
            'additionally': 'also',
            'subsequently': 'then',
            'accordingly': 'so',
            'thus': 'so',
            'hence': 'that\'s why'
        }
        
        for formal, informal in formal_to_informal.items():
            text = re.sub(r'\b' + re.escape(formal) + r'\b', informal, text, flags=re.IGNORECASE)
        
        return text
    
    def add_perfect_imperfections(self, text: str) -> str:
        """Add subtle imperfections that make text seem human"""
        # Occasional sentence fragments
        if random.random() < 0.1:
            sentences = sent_tokenize(text)
            if len(sentences) > 1:
                fragment_pos = random.randint(1, len(sentences) - 1)
                fragment = random.choice(["You know?", "Right?", "Exactly.", "For sure."])
                sentences.insert(fragment_pos, fragment)
                text = ' '.join(sentences)
        
        # Slightly awkward phrasing
        if random.random() < 0.08:
            text = re.sub(r'\b(the|a|an)\s+(\w+)\s+(is|are)\s+(\w+)', 
                         lambda m: f"{m.group(2)} {m.group(3)} {m.group(4)}", text)
        
        # Occasional redundancy
        if random.random() < 0.05:
            text += " if you know what I mean."
        
        return text
    
    def optimize_for_readability(self, text: str) -> str:
        """Optimize text for human readability"""
        sentences = sent_tokenize(text)
        optimized_sentences = []
        
        for sentence in sentences:
            words = sentence.split()
            
            # Break up very long sentences
            if len(words) > 30:
                mid_point = len(words) // 2
                # Try to break at a natural point
                break_points = [i for i, word in enumerate(words) if word.endswith(('.', ',', ';'))]
                if break_points:
                    break_point = min(break_points, key=lambda x: abs(x - mid_point))
                    first_part = ' '.join(words[:break_point + 1])
                    second_part = ' '.join(words[break_point + 1:])
                    optimized_sentences.extend([first_part, second_part])
                else:
                    optimized_sentences.append(sentence)
            else:
                optimized_sentences.append(sentence)
        
        return ' '.join(optimized_sentences)
    
    def extract_keywords(self, text: str, max_keywords: int = 5) -> List[str]:
        """Extract keywords for SEO optimization"""
        kw_extractor = yake.KeywordExtractor(lan="en", n=3, dedupLim=0.7, top=max_keywords)
        keywords = kw_extractor.extract_keywords(text)
        return [kw[0] for kw in keywords]
    
    def naturally_insert_keywords(self, text: str, keywords: List[str]) -> str:
        """Naturally insert keywords into text"""
        if not keywords:
            return text
            
        sentences = sent_tokenize(text)
        modified_sentences = []
        used_keywords = set()
        
        for sentence in sentences:
            # Try to insert a keyword naturally
            available_keywords = [kw for kw in keywords if kw not in used_keywords]
            if available_keywords and random.random() < 0.3:
                keyword = random.choice(available_keywords)
                
                # Natural insertion patterns
                patterns = [
                    f"especially when it comes to {keyword}",
                    f"particularly for {keyword}",
                    f"which is great for {keyword}",
                    f"making it perfect for {keyword}",
                    f"if you're interested in {keyword}"
                ]
                
                pattern = random.choice(patterns)
                words = sentence.split()
                insert_pos = random.randint(1, len(words) - 1) if len(words) > 2 else 1
                words.insert(insert_pos, pattern)
                modified_sentences.append(' '.join(words))
                used_keywords.add(keyword)
            else:
                modified_sentences.append(sentence)
        
        return ' '.join(modified_sentences)
    
    def calculate_human_score(self, text: str) -> float:
        """Calculate human-like score for text"""
        patterns = self.analyze_ai_patterns(text)
        
        # Reverse score (lower AI patterns = higher human score)
        ai_score = sum(patterns.values()) / len(patterns)
        human_score = max(0, min(1, 1 - ai_score))
        
        # Bonus factors
        blob = TextBlob(text)
        
        # Contractions bonus
        contractions = ["n't", "'ll", "'ve", "'re", "'m"]
        contraction_bonus = sum(1 for contr in contractions if contr in text) * 0.1
        
        # Sentence variety bonus
        lengths = [len(sent.words) for sent in blob.sentences]
        if lengths:
            variety_bonus = min(0.2, np.var(lengths) / 100)
        else:
            variety_bonus = 0
        
        # Informal language bonus
        informal_words = ['yeah', 'yep', 'nope', 'gonna', 'wanna', 'kinda', 'sorta']
        informal_bonus = sum(1 for word in informal_words if word in text.lower()) * 0.05
        
        final_score = min(1.0, human_score + contraction_bonus + variety_bonus + informal_bonus)
        return final_score
    
    def advanced_humanize(self, text: str, keywords: List[str] = None, 
                        intensity: float = 0.7, target_score: float = 0.95) -> Dict:
        """Advanced humanization with target score"""
        if not text or len(text.strip()) < 10:
            return {
                'original_text': text,
                'humanized_text': text,
                'human_score': 1.0,
                'iterations': 0
            }
        
        original_text = text
        current_text = text
        iterations = 0
        max_iterations = 10
        
        # Extract keywords if none provided
        if keywords is None:
            keywords = self.extract_keywords(text)
        
        while iterations < max_iterations:
            current_score = self.calculate_human_score(current_text)
            
            if current_score >= target_score:
                break
            
            # Apply humanization techniques based on intensity
            if intensity >= 0.3:
                current_text = self.add_human_variations(current_text)
            
            if intensity >= 0.5:
                current_text = self.vary_sentence_patterns(current_text)
            
            if intensity >= 0.4:
                current_text = self.naturalize_vocabulary(current_text)
            
            if intensity >= 0.6:
                current_text = self.add_perfect_imperfections(current_text)
            
            if intensity >= 0.2:
                current_text = self.optimize_for_readability(current_text)
            
            if keywords and intensity >= 0.3:
                current_text = self.naturally_insert_keywords(current_text, keywords)
            
            iterations += 1
        
        final_score = self.calculate_human_score(current_text)
        
        return {
            'original_text': original_text,
            'humanized_text': current_text,
            'human_score': final_score,
            'iterations': iterations,
            'keywords_used': keywords,
            'ai_patterns': self.analyze_ai_patterns(current_text)
        }

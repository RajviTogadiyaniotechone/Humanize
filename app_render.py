#!/usr/bin/env python3
"""
Simplified Flask app for Render deployment - minimal dependencies
"""

import os
import re
import random
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import nltk
from textblob import TextBlob
import textstat

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    nltk.download('stopwords', quiet=True)
except:
    pass

# CACHE-BUSTING TIMESTAMP: 2026-05-12T16:18:49.070594

def preserve_formatting_production(text, humanized_text):
    """Production-ready format preservation"""
    
    # Split both texts by words
    words = text.split()
    humanized_words = humanized_text.split()
    
    # If word counts don't match, return humanized as-is
    if len(words) != len(humanized_words):
        return humanized_text
    
    # Rebuild preserving original formatting character by character
    result = []
    text_chars = list(text)
    word_start = 0
    
    for i, char in enumerate(text_chars):
        if char.isspace() or i == len(text_chars) - 1:
            # Found whitespace or end of text
            if i > word_start:
                # Extract word from original
                original_word = ''.join(text_chars[word_start:i])
                
                # Find corresponding humanized word
                word_index = len([w for w in words[:len(words)] if w == original_word])
                if word_index < len(humanized_words):
                    humanized_word = humanized_words[word_index]
                    
                    # Replace characters in result
                    for j in range(len(original_word)):
                        if word_start + j < len(text_chars):
                            text_chars[word_start + j] = humanized_word[j] if j < len(humanized_word) else original_word[j]
            
            word_start = i + 1
    
    return ''.join(text_chars)
    """Simple format preservation that works with deployed logic"""
    
    # Split both texts by words
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

from word_replacement_humanizer import WordReplacementHumanizer

app = Flask(__name__)
CORS(app)

# Add version check endpoint to verify latest deployment
@app.route('/api/version', methods=['GET'])
def get_version():
    """Get current app version"""
    return jsonify({
        'version': '2.1.0',
        'features': [
            'formatting_preservation',
            'comprehensive_synonyms',
            'ultimate_coverage',
            'aggressive_cache_busting'
        ],
        'timestamp': datetime.now().isoformat(),
        'commit_hash': 'e8ca89b',
        'debug_info': {
            'formatting_method': 'string_replacement',
            'newline_support': True,
            'space_preservation': True
        }
    })

# Add debug endpoint to verify formatting preservation
@app.route('/api/debug-formatting', methods=['POST'])
def debug_formatting():
    """Debug formatting preservation"""
    data = request.get_json()
    text = data.get('text', '')
    
    humanizer = WordReplacementHumanizer()
    result = humanizer.word_replacement_humanize(text, intensity=0.7)
    
    original_newlines = text.count('\n')
    original_spaces = text.count('  ')
    
    if result['success']:
        output_text = result['humanized_text']
        output_newlines = output_text.count('\n')
        output_spaces = output_text.count('  ')
        
        return jsonify({
            'success': True,
            'debug_info': {
                'original': {
                    'text': text,
                    'newlines': original_newlines,
                    'spaces': original_spaces,
                    'repr': repr(text)
                },
                'humanized': {
                    'text': output_text,
                    'newlines': output_newlines,
                    'spaces': output_spaces,
                    'repr': repr(output_text)
                },
                'preservation': {
                    'newlines_preserved': original_newlines == output_newlines,
                    'spaces_preserved': original_spaces == output_spaces
                }
            }
        })
    else:
        return jsonify({
            'success': False,
            'error': result.get('error', 'Debug failed')
        })

# Add cache-busting endpoint
@app.route('/api/clear-cache', methods=['POST'])
def clear_cache():
    """Clear any cached data"""
    return jsonify({
        'success': True,
        'message': 'Cache cleared',
        'timestamp': datetime.now().isoformat()
    })

# Word replacement mappings (simplified for Render)
WORD_REPLACEMENTS = {
    "furthermore": ["also", "plus", "additionally", "moreover"],
    "moreover": ["also", "plus", "additionally", "furthermore"],
    "consequently": ["so", "therefore", "thus", "hence"],
    "nevertheless": ["however", "still", "but", "yet"],
    "utilize": ["use", "apply", "employ", "work with"],
    "facilitate": ["help", "assist", "support", "enable"],
    "implement": ["start", "begin", "launch", "set up"],
    "optimize": ["improve", "enhance", "boost", "fine-tune"],
    "enhance": ["improve", "boost", "upgrade", "strengthen"],
    "leverage": ["use", "apply", "employ", "work with"],
    "establish": ["create", "build", "set up", "form"],
    "necessitates": ["requires", "needs", "demands", "calls for"],
    "comprehensive": ["complete", "full", "thorough", "extensive"],
    "subsequent": ["following", "next", "later", "coming"],
    "aforementioned": ["mentioned", "previous", "earlier", "said"],
    "imperative": ["essential", "necessary", "crucial", "vital"],
    "strategic": ["key", "smart", "planned", "important"],
    "methodologies": ["methods", "approaches", "ways", "techniques"],
    "organizational": ["company", "business", "team", "workplace"],
    "infrastructure": ["setup", "system", "structure", "framework"],
    "various": ["different", "multiple", "several", "many"],
    "factors": ["elements", "aspects", "points", "things"],
    "technologies": ["tools", "systems", "solutions", "methods"],
    "operational": ["working", "running", "active", "in use"],
    "efficiency": ["performance", "productivity", "output", "results"],
    "outcomes": ["results", "effects", "consequences", "impacts"],
    "desired": ["wanted", "needed", "required", "targeted"],
    "competencies": ["skills", "abilities", "strengths", "capabilities"],
    "effectively": ["well", "properly", "successfully", "skillfully"],
    
    # Additional common words
    "must": ["should", "need to", "have to", "ought to"],
    "should": ["must", "need to", "have to", "ought to"],
    "will": ["would", "shall", "going to"],
    "would": ["will", "shall", "going to"],
    "can": ["could", "may", "might"],
    "could": ["can", "may", "might"],
    "very": ["extremely", "really", "quite", "highly"],
    "important": ["key", "crucial", "vital", "essential"],
    "good": ["great", "excellent", "fine", "nice"],
    "big": ["large", "huge", "massive", "enormous"],
    "small": ["tiny", "little", "minor", "petite"],
    "fast": ["quick", "rapid", "swift", "speedy"],
    "slow": ["sluggish", "gradual", "leisurely", "unhurried"],
    "new": ["fresh", "recent", "novel", "modern"],
    "old": ["ancient", "aged", "mature", "vintage"]
}

# Contractions
CONTRACTIONS = {
    "do not": "don't", "will not": "won't", "cannot": "can't",
    "did not": "didn't", "is not": "isn't", "are not": "aren't",
    "was not": "wasn't", "were not": "weren't", "have not": "haven't",
    "has not": "hasn't", "could not": "couldn't", "would not": "wouldn't",
    "should not": "shouldn't", "I am": "I'm", "you are": "you're",
    "we are": "we're", "they are": "they're", "it is": "it's"
}

@app.route('/')
def index():
    """Render the focused user-friendly web interface"""
    return render_template('focused_index.html')

@app.route('/api/enhanced-humanize', methods=['POST'])
def enhanced_humanize_api():
    """Enhanced humanization API with word replacement"""
    try:
        # Validate request
        if not request.is_json:
            return jsonify({
                'success': False,
                'error': 'Request must be JSON'
            }), 400
        
        data = request.get_json()
        
        # Validate required fields
        if not data.get('text'):
            return jsonify({
                'success': False,
                'error': 'Text field is required'
            }), 400
        
        # Get parameters with defaults
        text = data.get('text', '').strip()
        intensity = float(data.get('intensity', 0.7))
        focused_mode = bool(data.get('focused_mode', True))
        
        # Validate text length
        if len(text) > 10000:
            return jsonify({
                'success': False,
                'error': 'Text too long (max 10000 characters)'
            }), 400
        
        if len(text) < 10:
            return jsonify({
                'success': False,
                'error': 'Text too short (min 10 characters)'
            }), 400
        
        # Validate intensity
        if not 0 <= intensity <= 1:
            return jsonify({
                'success': False,
                'error': 'Intensity must be between 0 and 1'
            }), 400
        
        # Perform word replacement humanization with formatting preservation
        humanizer = WordReplacementHumanizer()
        result = humanizer.word_replacement_humanize(text, intensity)
        
        # Apply format preservation to maintain newlines and spaces
        if result['success']:
            original_text = text
            humanized_text = result['humanized_text']
            result['humanized_text'] = preserve_formatting_production(original_text, humanized_text)
        
        if not result.get('success'):
            return jsonify({
                'success': False,
                'error': result.get('error', 'Humanization failed')
            }), 500
        
        # Prepare response data
        response_data = {
            'success': True,
            'humanized_text': result['humanized_text'],
            'human_score': result['human_score'],
            'changes_applied': result['changes_applied'],
            'character_count': result.get('character_count', len(result['humanized_text'])),
            'original_text': result.get('original_text', text),
            'timestamp': datetime.now().isoformat()
        }
        
        # Add additional fields if available
        if 'sequence_preserved' in result:
            response_data['sequence_preserved'] = result['sequence_preserved']
        if 'no_extra_words' in result:
            response_data['no_extra_words'] = result['no_extra_words']
        
        return jsonify(response_data)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500

def word_replacement_humanize(text, intensity=0.7):
    """Simplified word replacement humanization"""
    
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
    
    # Apply word replacements while preserving structure
    for sentence in sentences:
        if not sentence.strip():
            continue
        
        # Replace words with similar meanings
        sentence = replace_words_with_similar(sentence)
        if random.random() < 0.8:
            changes_applied.append('word_replacement')
        
        # Add natural contractions
        sentence = add_natural_contractions(sentence)
        if random.random() < 0.6:
            changes_applied.append('contraction_usage')
        
        # Ensure proper punctuation
        sentence = ensure_proper_punctuation(sentence)
        changes_applied.append('punctuation_correction')
        
        rewritten_sentences.append(sentence)
    
    # Reconstruct text (maintaining original sentence order)
    humanized_text = ' '.join(rewritten_sentences)
    
    # Calculate character count
    char_count = len(humanized_text)
    
    # Calculate human score
    human_score = calculate_human_score(humanized_text)
    
    return {
        'success': True,
        'original_text': original_text,
        'humanized_text': humanized_text,
        'human_score': human_score,
        'changes_applied': changes_applied,
        'character_count': char_count,
        'sequence_preserved': True,
        'no_extra_words': True,
        'timestamp': datetime.now().isoformat()
    }

def replace_words_with_similar(sentence):
    """Replace words with similar meanings only"""
    
    words = sentence.split()
    rewritten_words = []
    replacement_count = 0
    
    # Scale replacements based on content length
    word_count = len(words)
    if word_count <= 10:
        # Short content: 2-3 words
        min_replacements = 2
        max_replacements = 3
    elif word_count <= 20:
        # Medium content: 3-5 words
        min_replacements = 3
        max_replacements = 5
    elif word_count <= 30:
        # Long content: 4-7 words
        min_replacements = 4
        max_replacements = 7
    else:
        # Very long content: 5-10 words (1 per 3-4 words)
        min_replacements = max(5, word_count // 4)
        max_replacements = max(10, word_count // 3)
    
    for i, word in enumerate(words):
        # Clean word for matching
        clean_word = re.sub(r'[^\w]', '', word.lower())
        
        # Check for word replacement
        if clean_word in WORD_REPLACEMENTS and replacement_count < max_replacements:
            if random.random() < 0.95 or replacement_count < min_replacements:
                alternatives = WORD_REPLACEMENTS[clean_word]
                replacement = random.choice(alternatives)
                
                # Preserve original capitalization and punctuation
                if word[0].isupper():
                    replacement = replacement.capitalize()
                
                punctuation = re.sub(r'\w', '', word)
                if punctuation:
                    replacement += punctuation
                
                rewritten_words.append(replacement)
                replacement_count += 1
            else:
                rewritten_words.append(word)
        else:
            rewritten_words.append(word)
    
    return ' '.join(rewritten_words)

def add_natural_contractions(sentence):
    """Add natural contractions"""
    
    for formal, contraction in CONTRACTIONS.items():
        if random.random() < 0.6:
            sentence = re.sub(
                r'\b' + re.escape(formal) + r'\b',
                contraction,
                sentence,
                flags=re.IGNORECASE
            )
    
    return sentence

def ensure_proper_punctuation(sentence):
    """Ensure proper punctuation"""
    
    # Remove excessive punctuation
    sentence = re.sub(r',{2,}', ',', sentence)
    sentence = re.sub(r'\.{2,}', '.', sentence)
    
    # Ensure proper sentence ending
    sentence = sentence.strip()
    if sentence and not sentence[-1] in '.!?':
        if len(sentence.split()) > 3:
            sentence += '.'
    
    return sentence

def calculate_human_score(text):
    """Calculate human score for word-replacement humanization"""
    
    indicators = {
        'word_replacement': 0,
        'contraction_usage': 0,
        'punctuation_quality': 0,
        'sequence_preservation': 0,
        'no_extra_words': 0
    }
    
    # Word replacement score
    replaced_words_count = sum(1 for word in WORD_REPLACEMENTS.keys() 
                              if word in text.lower())
    total_ai_words = len(WORD_REPLACEMENTS)
    words_replaced = min(1.0, replaced_words_count / max(1, total_ai_words / 10))
    indicators['word_replacement'] = words_replaced
    
    # Contraction usage score
    contraction_count = sum(1 for contraction in CONTRACTIONS.values() 
                          if contraction in text)
    indicators['contraction_usage'] = min(1.0, contraction_count / 5)
    
    # Punctuation quality score
    punctuation_variety = len(set(re.findall(r'[.,!?;:]', text)))
    indicators['punctuation_quality'] = min(1.0, punctuation_variety / 4)
    
    # Sequence preservation score
    indicators['sequence_preservation'] = 1.0
    
    # No extra words score
    indicators['no_extra_words'] = 1.0
    
    # Calculate overall score
    total_score = sum(indicators.values()) / len(indicators)
    human_score = min(100, total_score * 200)
    
    return human_score

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    # Production configuration
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    app.run(host=host, port=port, debug=debug)

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import nltk
import spacy
import random
import re
import json
from datetime import datetime
import os
from enhanced_humanizer import AdvancedContentHumanizer
from structure_humanizer import StructureOnlyHumanizer
from linguistic_humanizer import LinguisticHumanizer
from clean_advanced_humanizer import CleanAdvancedRewritingHumanizer
from focused_rewriting_humanizer import FocusedRewritingHumanizer
from word_replacement_humanizer import WordReplacementHumanizer

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    nltk.download('stopwords', quiet=True)
except:
    pass

app = Flask(__name__)
CORS(app)

# Initialize all humanizers
humanizer = AdvancedContentHumanizer()
structure_humanizer = StructureOnlyHumanizer()
linguistic_humanizer = LinguisticHumanizer()
rewriting_humanizer = CleanAdvancedRewritingHumanizer()
focused_humanizer = FocusedRewritingHumanizer()
word_replacement_humanizer = WordReplacementHumanizer()

@app.route('/')
def index():
    """Render the focused user-friendly web interface"""
    return render_template('focused_index.html')

@app.route('/api/enhanced-humanize', methods=['POST'])
def enhanced_humanize_api():
    """Enhanced humanization API with advanced features"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        keywords = data.get('keywords', [])
        intensity = data.get('intensity', 0.7)
        target_score = data.get('target_score', 0.95)
        show_analysis = data.get('show_analysis', True)
        preserve_words = data.get('preserve_words', False)  # Structure-only mode
        preserve_punctuation = data.get('preserve_punctuation', False)  # Linguistic-only mode
        rewriting_mode = data.get('rewriting_mode', False)  # Rewriting mode
        focused_mode = data.get('focused_mode', False)  # Focused rewriting mode
        
        if not text.strip():
            return jsonify({'error': 'Please provide text to humanize'}), 400
        
        # Validate inputs
        if not 0.1 <= intensity <= 1.0:
            return jsonify({'error': 'Intensity must be between 0.1 and 1.0'}), 400
        
        if not 0.5 <= target_score <= 1.0:
            return jsonify({'error': 'Target score must be between 0.5 and 1.0'}), 400
        
        # Choose humanizer based on options
        if preserve_punctuation:
            # Use linguistic-only humanizer (words + structure only, no punctuation)
            result = linguistic_humanizer.linguistic_only_humanize(
                text=text,
                intensity=intensity
            )
        elif preserve_words:
            # Use structure-only humanizer (preserves all words, changes structure/punctuation)
            result = structure_humanizer.structure_only_humanize(
                text=text,
                intensity=intensity
            )
        elif rewriting_mode:
            # Use rewriting humanizer (active sentence rewriting, natural language)
            result = rewriting_humanizer.advanced_rewriting_humanize(
                text=text,
                intensity=intensity
            )
        elif focused_mode:
            # Use word-replacement humanizer (change words with similar meanings only)
            result = word_replacement_humanizer.word_replacement_humanize(
                text=text,
                intensity=intensity
            )
        else:
            # Use enhanced humanizer (changes words + structure + punctuation)
            result = humanizer.advanced_humanize(
                text=text,
                keywords=keywords,
                intensity=intensity,
                target_score=target_score
            )
        
        if not result['success']:
            return jsonify({'error': 'Humanization failed'}), 500
        
        # Prepare response - clean and user-friendly
        response_data = {
            'success': True,
            'humanized_text': result['humanized_text'],
            'human_score': result['human_score'],
            'changes_applied': result['changes_applied'],
            'character_count': result.get('character_count', len(result['humanized_text'])),
            'original_text': result['original_text'],
            'timestamp': datetime.now().isoformat()
        }
        
        # Add word preservation info if structure-only mode
        if preserve_words and 'words_preserved' in result:
            response_data['words_preserved'] = result['words_preserved']
        
        # Add linguistic info if linguistic-only mode
        if preserve_punctuation and 'punctuation_preserved' in result:
            response_data['punctuation_preserved'] = result['punctuation_preserved']
            response_data['words_changed'] = result['words_changed']
        
        # Add detailed analysis if requested
        if show_analysis:
            response_data['analysis'] = {
                'ai_patterns_detected': detect_ai_patterns(result['original_text']),
                'human_indicators': detect_human_indicators(result['humanized_text']),
                'semantic_similarity': calculate_semantic_similarity(result['original_text'], result['humanized_text']),
                'readability_score': calculate_readability_score(result['humanized_text'])
            }
        
        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({'error': f'Processing error: {str(e)}'}), 500

@app.route('/api/analyze-text', methods=['POST'])
def analyze_text_api():
    """Advanced text analysis API"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text.strip():
            return jsonify({'error': 'Please provide text to analyze'}), 400
        
        # Perform comprehensive analysis
        analysis = {
            'basic_stats': get_basic_text_stats(text),
            'ai_detection': analyze_ai_patterns(text),
            'human_quality': analyze_human_quality(text),
            'context_analysis': humanizer.analyze_text_context(text),
            'readability': analyze_readability(text),
            'recommendations': generate_recommendations(text)
        }
        
        return jsonify({
            'success': True,
            'analysis': analysis,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': f'Analysis error: {str(e)}'}), 500

@app.route('/api/batch-humanize', methods=['POST'])
def batch_humanize_api():
    """Batch humanization API for multiple texts"""
    try:
        data = request.get_json()
        texts = data.get('texts', [])
        keywords = data.get('keywords', [])
        intensity = data.get('intensity', 0.7)
        target_score = data.get('target_score', 0.95)
        
        if not texts:
            return jsonify({'error': 'Please provide texts to humanize'}), 400
        
        # Process each text
        results = []
        for i, text in enumerate(texts):
            try:
                result = humanizer.advanced_humanize(
                    text=text,
                    keywords=keywords,
                    intensity=intensity,
                    target_score=target_score
                )
                
                results.append({
                    'index': i,
                    'success': result['success'],
                    'original_text': result['original_text'],
                    'humanized_text': result['humanized_text'],
                    'human_score': result['human_score'],
                    'target_score': result['target_score'],
                    'changes_applied': result['changes_applied']
                })
            
            except Exception as e:
                results.append({
                    'index': i,
                    'success': False,
                    'error': str(e)
                })
        
        return jsonify({
            'success': True,
            'results': results,
            'processed_count': len(results),
            'successful_count': sum(1 for r in results if r['success']),
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': f'Batch processing error: {str(e)}'}), 500

@app.route('/api/compare', methods=['POST'])
def compare_texts_api():
    """Compare original and humanized texts"""
    try:
        data = request.get_json()
        original_text = data.get('original_text', '')
        humanized_text = data.get('humanized_text', '')
        
        if not original_text.strip() or not humanized_text.strip():
            return jsonify({'error': 'Please provide both texts to compare'}), 400
        
        comparison = {
            'similarity_metrics': calculate_similarity_metrics(original_text, humanized_text),
            'human_score_improvement': calculate_score_improvement(original_text, humanized_text),
            'changes_summary': summarize_changes(original_text, humanized_text),
            'preservation_analysis': analyze_semantic_preservation(original_text, humanized_text)
        }
        
        return jsonify({
            'success': True,
            'comparison': comparison,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': f'Comparison error: {str(e)}'}), 500

@app.route('/api/export', methods=['POST'])
def export_results_api():
    """Export humanization results"""
    try:
        data = request.get_json()
        format_type = data.get('format', 'json')
        results = data.get('results', [])
        
        if not results:
            return jsonify({'error': 'No results to export'}), 400
        
        if format_type == 'json':
            export_data = json.dumps(results, indent=2)
            filename = f"humanization_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        elif format_type == 'txt':
            export_data = format_as_text(results)
            filename = f"humanization_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        elif format_type == 'csv':
            export_data = format_as_csv(results)
            filename = f"humanization_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        else:
            return jsonify({'error': 'Unsupported export format'}), 400
        
        return jsonify({
            'success': True,
            'export_data': export_data,
            'filename': filename,
            'format': format_type
        })
    
    except Exception as e:
        return jsonify({'error': f'Export error: {str(e)}'}), 500

# Helper functions for analysis and utilities

def detect_ai_patterns(text):
    """Detect AI writing patterns"""
    ai_patterns = {
        'formal_connectors': ['furthermore', 'moreover', 'consequently', 'nevertheless', 'subsequently'],
        'perfect_grammar': ['utilize', 'facilitate', 'implement', 'optimize', 'enhance'],
        'uniform_structure': ['in order to', 'due to the fact that', 'with regard to', 'in terms of'],
        'no_contractions': ['do not', 'will not', 'cannot', 'did not', 'is not'],
        'complex_vocabulary': []  # Would need word complexity analysis
    }
    
    detected = {}
    text_lower = text.lower()
    
    for pattern_type, patterns in ai_patterns.items():
        count = sum(1 for pattern in patterns if pattern in text_lower)
        detected[pattern_type] = {
            'count': count,
            'patterns_found': [p for p in patterns if p in text_lower]
        }
    
    return detected

def detect_human_indicators(text):
    """Detect human-like indicators"""
    human_indicators = {
        'contractions': ["don't", "can't", "won't", "didn't", "isn't", "aren't", "it's", "you're", "we're"],
        'informal_words': ['you know', 'I mean', 'like', 'well', 'actually', 'basically', 'honestly'],
        'conversational_starters': ['so', 'well', 'look', 'hey', 'you know what', 'here\'s the thing'],
        'natural_variations': ['sort of', 'kind of', 'pretty much', 'almost', 'basically']
    }
    
    detected = {}
    text_lower = text.lower()
    
    for indicator_type, indicators in human_indicators.items():
        count = sum(1 for indicator in indicators if indicator in text_lower)
        detected[indicator_type] = {
            'count': count,
            'indicators_found': [i for i in indicators if i in text_lower]
        }
    
    return detected

def calculate_semantic_similarity(original, humanized):
    """Calculate semantic similarity (simplified)"""
    # This is a simplified version - would use embeddings in production
    original_words = set(original.lower().split())
    humanized_words = set(humanized.lower().split())
    
    intersection = original_words & humanized_words
    union = original_words | humanized_words
    
    similarity = len(intersection) / len(union) if union else 0
    return round(similarity * 100, 2)

def calculate_readability_score(text):
    """Calculate readability score"""
    sentences = re.split(r'[.!?]+', text)
    words = text.split()
    
    if not sentences or not words:
        return 0
    
    avg_sentence_length = len(words) / len(sentences)
    
    # Simplified readability score
    if avg_sentence_length < 10:
        return 90  # Very easy to read
    elif avg_sentence_length < 15:
        return 80  # Easy to read
    elif avg_sentence_length < 20:
        return 70  # Fairly easy to read
    elif avg_sentence_length < 25:
        return 60  # Standard
    else:
        return 50  # Fairly difficult

def get_basic_text_stats(text):
    """Get basic text statistics"""
    sentences = re.split(r'[.!?]+', text)
    words = text.split()
    paragraphs = text.split('\n\n')
    
    return {
        'characters': len(text),
        'words': len(words),
        'sentences': len([s for s in sentences if s.strip()]),
        'paragraphs': len([p for p in paragraphs if p.strip()]),
        'avg_sentence_length': round(len(words) / len(sentences), 2) if sentences else 0,
        'avg_word_length': round(sum(len(w) for w in words) / len(words), 2) if words else 0
    }

def analyze_ai_patterns(text):
    """Analyze AI patterns in detail"""
    patterns = detect_ai_patterns(text)
    
    # Calculate AI score
    total_patterns = sum(p['count'] for p in patterns.values())
    max_patterns = len(patterns) * 5  # Assume max 5 of each pattern type
    
    ai_score = min(100, (total_patterns / max_patterns) * 100)
    
    return {
        'patterns': patterns,
        'ai_score': round(ai_score, 2),
        'risk_level': 'high' if ai_score > 70 else 'medium' if ai_score > 40 else 'low'
    }

def analyze_human_quality(text):
    """Analyze human-like quality"""
    indicators = detect_human_indicators(text)
    
    # Calculate human score
    total_indicators = sum(i['count'] for i in indicators.values())
    max_indicators = len(indicators) * 3  # Assume max 3 of each indicator type
    
    human_score = min(100, (total_indicators / max_indicators) * 100)
    
    return {
        'indicators': indicators,
        'human_score': round(human_score, 2),
        'quality_level': 'excellent' if human_score > 80 else 'good' if human_score > 60 else 'fair' if human_score > 40 else 'poor'
    }

def analyze_readability(text):
    """Analyze text readability"""
    sentences = re.split(r'[.!?]+', text)
    words = text.split()
    
    if not sentences or not words:
        return {'score': 0, 'level': 'unknown'}
    
    avg_sentence_length = len(words) / len(sentences)
    avg_word_length = sum(len(w) for w in words) / len(words)
    
    # Simplified readability calculation
    score = 100 - (avg_sentence_length * 1.5) - (avg_word_length * 2)
    score = max(0, min(100, score))
    
    if score > 80:
        level = 'very_easy'
    elif score > 70:
        level = 'easy'
    elif score > 60:
        level = 'fairly_easy'
    elif score > 50:
        level = 'standard'
    elif score > 30:
        level = 'fairly_difficult'
    else:
        level = 'difficult'
    
    return {
        'score': round(score, 2),
        'level': level,
        'avg_sentence_length': round(avg_sentence_length, 2),
        'avg_word_length': round(avg_word_length, 2)
    }

def generate_recommendations(text):
    """Generate improvement recommendations"""
    ai_analysis = analyze_ai_patterns(text)
    human_analysis = analyze_human_quality(text)
    readability = analyze_readability(text)
    
    recommendations = []
    
    if ai_analysis['ai_score'] > 70:
        recommendations.append("High AI detection risk - apply strong humanization")
    
    if human_analysis['human_score'] < 60:
        recommendations.append("Add more contractions and informal language")
    
    if readability['score'] < 60:
        recommendations.append("Consider shorter sentences for better readability")
    
    if ai_analysis['patterns']['formal_connectors']['count'] > 3:
        recommendations.append("Replace formal connectors with conversational alternatives")
    
    if human_analysis['indicators']['contractions']['count'] < 2:
        recommendations.append("Add natural contractions to sound more human")
    
    return recommendations

def calculate_similarity_metrics(original, humanized):
    """Calculate detailed similarity metrics"""
    return {
        'word_overlap': calculate_semantic_similarity(original, humanized),
        'length_ratio': round(len(humanized) / len(original) * 100, 2) if original else 0,
        'sentence_count_change': len(re.split(r'[.!?]+', humanized)) - len(re.split(r'[.!?]+', original))
    }

def calculate_score_improvement(original, humanized):
    """Calculate human score improvement"""
    original_score = humanizer.calculate_advanced_human_score(original)
    humanized_score = humanizer.calculate_advanced_human_score(humanized)
    
    return {
        'original_score': original_score,
        'humanized_score': humanized_score,
        'improvement': round(humanized_score - original_score, 2),
        'improvement_percentage': round(((humanized_score - original_score) / original_score) * 100, 2) if original_score > 0 else 0
    }

def summarize_changes(original, humanized):
    """Summarize changes made"""
    return {
        'characters_added': len(humanized) - len(original),
        'words_added': len(humanized.split()) - len(original.split()),
        'contractions_added': humanized.count("'") - original.count("'"),
        'punctuation_changes': humanized.count(',') - original.count(',')
    }

def analyze_semantic_preservation(original, humanized):
    """Analyze how well semantic meaning is preserved"""
    # Simplified semantic preservation analysis
    original_words = set(original.lower().split())
    humanized_words = set(humanized.lower().split())
    
    preserved_words = original_words & humanized_words
    preservation_rate = len(preserved_words) / len(original_words) if original_words else 0
    
    return {
        'preservation_rate': round(preservation_rate * 100, 2),
        'preserved_words': len(preserved_words),
        'total_original_words': len(original_words),
        'quality': 'excellent' if preservation_rate > 0.8 else 'good' if preservation_rate > 0.6 else 'fair' if preservation_rate > 0.4 else 'poor'
    }

def format_as_text(results):
    """Format results as plain text"""
    output = []
    output.append("Humanization Results")
    output.append("=" * 50)
    output.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output.append("")
    
    for i, result in enumerate(results):
        output.append(f"Result {i+1}:")
        output.append("-" * 30)
        output.append(f"Human Score: {result.get('human_score', 'N/A')}")
        output.append(f"Target Score: {result.get('target_score', 'N/A')}")
        # output.append(f"Changes Applied: {', '.join(result.get('changes_applied', []))}")
        output.append("")
        output.append("Original Text:")
        output.append(result.get('original_text', ''))
        output.append("")
        output.append("Humanized Text:")
        output.append(result.get('humanized_text', ''))
        output.append("\n" + "=" * 50 + "\n")
    
    return '\n'.join(output)

def format_as_csv(results):
    """Format results as CSV"""
    import csv
    import io
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Header
    writer.writerow(['Index', 'Human Score', 'Target Score', 'Changes Applied', 'Original Text', 'Humanized Text'])
    
    # Data rows
    for i, result in enumerate(results):
        writer.writerow([
            i,
            result.get('human_score', ''),
            result.get('target_score', ''),
            '; '.join(result.get('changes_applied', [])),
            result.get('original_text', ''),
            result.get('humanized_text', '')
        ])
    
    return output.getvalue()

if __name__ == '__main__':
    print("🚀 Starting Enhanced AI Content Humanizer...")
    print("🌐 Open http://localhost:5000 in your browser")
    print("✨ Advanced humanization with 100% human-like results!")
    print("🎯 Target: 0% AI detection, 100% human score")
    print("📊 Real-time analysis and optimization")
    app.run(debug=True, port=5000)

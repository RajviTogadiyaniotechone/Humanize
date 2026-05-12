#!/usr/bin/env python3
"""
Production-ready Flask app for public deployment
"""

import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from word_replacement_humanizer import WordReplacementHumanizer
from enhanced_humanizer import AdvancedContentHumanizer
from structure_humanizer import StructureOnlyHumanizer
from linguistic_humanizer import LinguisticHumanizer
from clean_advanced_humanizer import CleanAdvancedRewritingHumanizer
from focused_rewriting_humanizer import FocusedRewritingHumanizer
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Initialize all humanizers
humanizer = AdvancedContentHumanizer()
structure_humanizer = StructureOnlyHumanizer()
linguistic_humanizer = LinguisticHumanizer()
rewriting_humanizer = CleanAdvancedRewritingHumanizer()
focused_humanizer = FocusedRewritingHumanizer()
word_replacement_humanizer = WordReplacementHumanizer()

# Production configuration
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    """Render the focused user-friendly web interface"""
    return render_template('focused_index.html')

@app.route('/api/enhanced-humanize', methods=['POST'])
def enhanced_humanize_api():
    """Enhanced humanization API with advanced features"""
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
        keywords = data.get('keywords', [])
        intensity = float(data.get('intensity', 0.7))
        target_score = float(data.get('target_score', 0.9))
        show_analysis = bool(data.get('show_analysis', False))
        preserve_words = bool(data.get('preserve_words', False))
        preserve_punctuation = bool(data.get('preserve_punctuation', False))
        rewriting_mode = bool(data.get('rewriting_mode', False))
        focused_mode = bool(data.get('focused_mode', False))
        
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
        
        # Select appropriate humanizer
        if rewriting_mode:
            result = rewriting_humanizer.advanced_rewriting_humanize(
                text=text,
                intensity=intensity
            )
        elif focused_mode:
            result = word_replacement_humanizer.word_replacement_humanize(
                text=text,
                intensity=intensity
            )
        else:
            result = humanizer.advanced_humanize(
                text=text,
                keywords=keywords,
                intensity=intensity,
                target_score=target_score
            )
        
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
        logger.error(f"API Error: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Internal server error'
        }), 500

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
    
    logger.info(f"Starting production server on {host}:{port}")
    app.run(host=host, port=port, debug=debug)

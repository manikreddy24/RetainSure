from flask import Flask, request, redirect, jsonify
import string
import random
from datetime import datetime
from typing import Dict

app = Flask(__name__)

# In-memory storage
url_db: Dict[str, dict] = {}

def generate_short_code(length: int = 6) -> str:
    """Generate random alphanumeric code"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    """Shorten URL endpoint"""
    data = request.get_json()
    
    # Validate input
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    
    url = data['url']
    if not url.startswith(('http://', 'https://')):
        return jsonify({'error': 'Invalid URL format'}), 400
    
    # Generate and store code
    short_code = generate_short_code()
    url_db[short_code] = {
        'original_url': url,
        'clicks': 0,
        'created_at': datetime.utcnow().isoformat()
    }
    
    return jsonify({
        'short_code': short_code,
        'short_url': f"{request.host_url}{short_code}"
    }), 201

@app.route('/<short_code>')
def redirect_to_url(short_code: str):
    """Redirect endpoint with click tracking"""
    if short_code not in url_db:
        return jsonify({'error': 'Short URL not found'}), 404
    
    url_db[short_code]['clicks'] += 1
    return redirect(url_db[short_code]['original_url'])

@app.route('/api/stats/<short_code>')
def get_stats(short_code: str):
    """Analytics endpoint"""
    if short_code not in url_db:
        return jsonify({'error': 'Short URL not found'}), 404
    
    return jsonify({
        'url': url_db[short_code]['original_url'],
        'clicks': url_db[short_code]['clicks'],
        'created_at': url_db[short_code]['created_at']
    })
@app.route('/')
def home():
    return {"message": "URL Shortener API"}, 200

import pytest
from app.main import app, url_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        url_db.clear()  # Cleanup after each test

def test_shorten_url(client):
    """Test URL shortening"""
    response = client.post(
        '/api/shorten',
        json={'url': 'https://example.com'}
    )
    assert response.status_code == 201
    assert 'short_code' in response.json

def test_redirect(client):
    """Test redirection and click tracking"""
    # First shorten
    shorten_resp = client.post(
        '/api/shorten',
        json={'url': 'https://example.com'}
    )
    code = shorten_resp.json['short_code']
    
    # Test redirect
    redirect_resp = client.get(f'/{code}')
    assert redirect_resp.status_code == 302
    assert url_db[code]['clicks'] == 1

def test_invalid_url(client):
    """Test invalid URL submission"""
    response = client.post(
        '/api/shorten',
        json={'url': 'invalid-url'}
    )
    assert response.status_code == 400

def test_nonexistent_code(client):
    """Test nonexistent short code"""
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_analytics(client):
    """Test analytics endpoint"""
    # Shorten URL
    shorten_resp = client.post(
        '/api/shorten',
        json={'url': 'https://example.com'}
    )
    code = shorten_resp.json['short_code']
    
    # Make 3 clicks
    for _ in range(3):
        client.get(f'/{code}')
    
    # Check stats
    stats_resp = client.get(f'/api/stats/{code}')
    assert stats_resp.status_code == 200
    assert stats_resp.json['clicks'] == 3
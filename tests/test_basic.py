import pytest
from app.main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.get_json()["status"] == "healthy"

def test_shorten_url_valid(client):
    res = client.post('/api/shorten', json={"url": "https://example.com"})
    assert res.status_code == 201
    data = res.get_json()
    assert "short_code" in data
    assert "short_url" in data

def test_shorten_url_invalid(client):
    res = client.post('/api/shorten', json={"url": "not-a-url"})
    assert res.status_code == 400
    assert "error" in res.get_json()

def test_shorten_url_missing(client):
    res = client.post('/api/shorten', json={})
    assert res.status_code == 400
    assert "error" in res.get_json()

def test_redirect_and_stats(client):
    res = client.post('/api/shorten', json={"url": "https://example.com"})
    short_code = res.get_json()["short_code"]

    # First redirect
    redirect_res = client.get(f"/{short_code}")
    assert redirect_res.status_code == 302

    # Stats
    stats_res = client.get(f"/api/stats/{short_code}")
    stats = stats_res.get_json()
    assert stats["url"] == "https://example.com"
    assert stats["clicks"] == 1
    assert "created_at" in stats

def test_stats_invalid_code(client):
    res = client.get("/api/stats/invalid123")
    assert res.status_code == 404

from flask import Flask, request, jsonify, redirect
from app.models import URLStore
from app.utils import generate_short_code, is_valid_url

app = Flask(__name__)
store = URLStore()

@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "Missing 'url' in request"}), 400

    original_url = data['url']
    if not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()
    while store.get_url(short_code):
        short_code = generate_short_code()

    store.add_url(short_code, original_url)
    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 201

@app.route('/<short_code>')
def redirect_to_original(short_code):
    url_data = store.get_url(short_code)
    if not url_data:
        return jsonify({"error": "Short code not found"}), 404

    store.increment_clicks(short_code)
    return redirect(url_data["original_url"], code=302)

@app.route('/api/stats/<short_code>')
def get_stats(short_code):
    stats = store.get_stats(short_code)
    if not stats:
        return jsonify({"error": "Short code not found"}), 404

    return jsonify({
        "url": stats["original_url"],
        "clicks": stats["clicks"],
        "created_at": stats["created_at"]
    })

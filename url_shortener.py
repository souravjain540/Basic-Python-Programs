import hashlib
import json
from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

# In-memory URL mapping (for demonstration purposes)
url_mapping = {}

def shorten_url(long_url):
    # Generate a unique short URL using hash
    hash_object = hashlib.md5(long_url.encode())
    short_url = hash_object.hexdigest()[:6]  # Use first 6 characters
    return short_url

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.json.get('long_url')
    if not long_url:
        return jsonify({"error": "No URL provided"}), 400
    short_url = shorten_url(long_url)
    url_mapping[short_url] = long_url
    return jsonify({"short_url": short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    return jsonify({"error": "URL not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    body = request.get_json()
    api_key = body.get('apiKey', '')
    payload = body.get('payload', {})

    if not api_key:
        return jsonify({'error': 'No API key provided'}), 400

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-2.0-flash-preview-image-generation:generateContent?key={api_key}"
    )

    try:
        res = requests.post(url, json=payload, timeout=120)
        return jsonify(res.json()), res.status_code
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timed out after 120 seconds. Try again.'}), 504
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"\n✅  Budget Barber running → http://localhost:{port}\n")
    app.run(host='0.0.0.0', port=port, debug=False)

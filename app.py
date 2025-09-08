from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static/frontend/build')
CORS(app)

# Define Q&A pairs directly in code
qa_pairs = {
    "What are your business hours?": "We operate from 9 AM to 6 PM, Monday to Saturday.",
    "Where are you located?": "Our headquarters are in Chennai, Tamil Nadu.",
    "Do you offer international shipping?": "Yes, we ship to over 50 countries worldwide.",
    "How can I apply for a job?": "Visit our Careers page and submit your resume.",
    "What products do you specialize in?": "We specialize in eco-friendly packaging solutions.",
    "Who is your CEO?" : "Aditya Nanda is our CEO."
}

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    question = data.get('question', '').strip()
    answer = qa_pairs.get(question, "A supervisor will contact you soon")
    return jsonify({'answer': answer})

# Serve React frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

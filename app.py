from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static/frontend/build')
CORS(app)

# Define Q&A pairs directly in code
qa_pairs = {
    "What are your business hours?": "Monday to Friday, 9:00 AM – 6:00 PM IST.",
    "Where are you located?": "Headquartered in India, with operations managed remotely.",
    "Do you offer international shipping?": "Not applicable. Kyzo AI is a SaaS company; its AI voice agent services are delivered digitally worldwide.",
    "How can I apply for a job?": "Applications can be submitted through the company’s website contact form or via LinkedIn.",
    "What products do you specialize in?": "AI-powered voice agents for outbound calling, mainly serving real estate, banking, and insurance industries.",
    "Who is your CEO?": "The CEO of Kyzo AI is Parwaan Virk."
}

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    question = data.get('question', '').strip()
    answer = qa_pairs.get(question, "A customer service executive will contact you soon")
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

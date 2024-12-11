# app.py
from flask import Flask, request, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return jsonify(message="Welcome to the Email Generator!")

    @app.route('/generate', methods=['POST'])
    def generate_email():
        data = request.get_json()
        to = data.get('to')
        subject = data.get('subject')
        body = data.get('body')

        if not to or not subject or not body:
            return jsonify(error="Missing required fields: 'to', 'subject', 'body'"), 400

        email_content = f"Subject: {subject}\nTo: {to}\n\n{body}"
        return jsonify(email=email_content)

    return app

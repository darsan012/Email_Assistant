from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Email Generator!")

@app.route('/generate', methods=['POST'])
def generate_email():
    # Simulate email generation
    return jsonify(email="Generated email content.")
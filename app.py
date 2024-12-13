# app.py
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Define responses for common questions
response_map = {
    "Track my order": "Your order is currently in transit and should arrive within the estimated delivery time.",
    "Update delivery address": "For security, please contact our customer service directly to update your delivery address.",
    "Cancel my order": "To cancel your order, please reach out to our support team at support@example.com.",
    "How long will delivery take?": "Delivery times vary by location but typically range between 30-60 minutes.",
    "Contact support": "You can reach our support team at support@example.com or call us at 1-800-555-5555."
}

# Default response if the question is not in the predefined set
default_response = "I'm sorry, I didn't understand that. Please try asking something like 'Track my order' or 'Contact support'."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    data = request.get_json()
    user_message = data["msg"]

    # Check if the message matches a predefined question
    response = response_map.get(user_message, default_response)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

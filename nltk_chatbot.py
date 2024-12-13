# nltk_chatbot.py
import nltk
from nltk.chat.util import Chat, reflections

# Conversation pairs for food order tracking chatbot
pairs = [
    ["hello|hi|hey", ["Hello! How can I assist you with your order today?", "Hi there! Need help with your order?"]],
    ["track order|where is my order|order status", [
        "Sure! Could you please provide your order ID?",
        "I'd be happy to help. What's your order number?"
    ]],
    ["my order id is (.*)", [
        "Thank you! I’m checking the status for order ID #%1...",
        "Got it! Let me look up the details for order ID #%1."
    ]],
    ["update delivery address|change address", [
        "Please provide the new delivery address.",
        "Of course! What is the updated delivery address?"
    ]],
    ["how long will it take|delivery time", [
        "Your order is on its way! It should arrive in approximately 30-45 minutes.",
        "Our delivery typically takes 30-45 minutes. You’ll receive a notification once it’s nearby!"
    ]],
    ["cancel my order", [
        "I'm sorry to hear that. Can you confirm your order ID for cancellation?",
        "To cancel, I need your order ID. Could you please provide it?"
    ]],
    ["contact support|speak to a representative|help from agent", [
        "Sure, please hold for a moment while I connect you to a representative.",
        "I'm transferring you to a customer support agent. They’ll assist you shortly."
    ]],
    ["thank you|thanks", ["You're welcome! Happy to help!", "Anytime! Let us know if you have more questions."]],
    ["bye|goodbye", ["Goodbye! Have a great day!", "Thank you for choosing our service! Take care."]],
]

# Initialize chatbot
def chatbot_response(user_input):
    chatbot = Chat(pairs, reflections)
    return chatbot.respond(user_input)

from flask import Flask, request, jsonify
from flask_cors import CORS
from nltk.chat.util import Chat, reflections
import nltk

# Download NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('wordnet')

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey! How can I assist you today?']),
    (r'how are you?', ['I\'m good, thank you!', 'I\'m doing well, thanks for asking. How can I help you today?']),
    (r'what can you do for me?', ['I can help you with product inquiries, order tracking, and more. Just ask!']),
    (r'can you help me with (.*)', ['Sure, I can assist you with %1. Please provide more details.']),
    (r'(.*) your name?', ['You can call me ChatGPT.', 'I go by the name ChatGPT.']),
    (r'(.*) products?', ['Our product catalog includes a variety of items. What are you looking for specifically?']),
    (r'(.*) buy (.*)', ['You can browse our products on our website and place an order there.']),
    (r'(.*) payment methods?(.*)', ['We accept major credit cards, PayPal, and other secure payment methods.']),
    (r'(.*) shipping options?(.*)', ['We offer standard and expedited shipping options.']),
    (r'how can I contact (.*)', ['You can reach our customer support team at support@example.com or call us at +123456789.']),
    (r'how can I return (.*)', ['Our return policy allows returns within 30 days of purchase.']),
    (r'how can I make a complaint(.*)', ['I apologize for any inconvenience. Please contact our support team for assistance.']),
    (r'how can I give feedback(.*)', ['Your feedback is valuable to us. Please share it through our website or contact our support team.']),
    (r'(.*) chatbot(.*)', ['Yes, I\'m a chatbot here to assist you with any questions you have about our products and services.']),
    (r'thank you', ['You\'re welcome!', 'No problem.']),
    (r'bye', ['Goodbye!', 'Have a great day!']),
    (r'(.*)', ['I\'m sorry, I\'m not sure how to respond to that. Could you please provide more details?']),
]

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

# Define Flask routes
@app.route('/')
def index():
    return 'Hello! This is a ChatGPT Web App.'

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = chatbot.respond(user_message)
    return jsonify({'response': response})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
import os
import logging
from flask import Flask, request, jsonify
from chatbot import ChatBot

logging.basicConfig(
    filename='chatbot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# Simple API key auth (for demo; use HTTPS in prod)
API_KEY = os.environ.get('CHATBOT_API_KEY', 'test-api-key')
app = Flask(__name__)
bot = ChatBot()

@app.route('/chat', methods=['POST'])
def chat():
    auth = request.headers.get('Authorization', None)
    if auth != f"Bearer {API_KEY}":
        logging.warning(f"Unauthorized request: {auth}")
        return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    user_input = data.get('message', '')
    logging.info(f"User message: {user_input}")
    bot_response = bot.get_response(user_input)
    logging.info(f"Bot response: {bot_response}")
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

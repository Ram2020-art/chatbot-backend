from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    conversation_history = request.json['history']

    conversation = conversation_history + [{'role': 'user', 'content': user_message}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    assistant_reply = response['choices'][0]['message']['content']

    return jsonify({'reply': assistant_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

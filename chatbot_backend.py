from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your OpenAI API key
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
    

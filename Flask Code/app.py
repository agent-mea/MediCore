from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = ''

# Initialize session state
messages = []

@app.route('/')
def index():
    return render_template('index.html', title="MediCore")

@app.route('/send_message', methods=['POST'])
@app.route('/send_message', methods=['POST'])
def send_message():
    global messages
    user_message = request.form.get('message')
    messages.append({"role": "user", "content": user_message})

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_message = response.choices[0].message['content']

    # Remove the trailing period if the message is a question
    if assistant_message.strip().endswith('?'):
        assistant_message = assistant_message.rstrip('.')

    messages.append({"role": "assistant", "content": assistant_message})

    return jsonify({"assistant_message": assistant_message})

if __name__ == '__main__':
    app.run(debug=True)

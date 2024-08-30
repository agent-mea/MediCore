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

    # Format the response into bullet points
    assistant_message = format_to_bullet_points(assistant_message)

    messages.append({"role": "assistant", "content": assistant_message})

    return jsonify({"assistant_message": assistant_message})

def format_to_bullet_points(text):
    """
    Formats a given text into bullet points, ignoring any initial numbering.
    Groups sentences that relate to each other in the same bullet point.
    """
    import re
    
    # Split the text by sentences using regex to keep punctuation marks
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    bullet_points = []
    current_bullet = ""

    for sentence in sentences:
        if len(sentence.strip()) == 0:
            continue
        
        # Remove any leading numbers or bullet points from the sentence
        sentence = re.sub(r'^\d+\.\s*', '', sentence).strip()

        # Append sentence to the current bullet
        if current_bullet:
            current_bullet += f" {sentence}"
        else:
            current_bullet = sentence

        # If the sentence ends with a period, question mark, or exclamation mark, finish the bullet point
        if re.search(r'[.!?]$', sentence):
            bullet_points.append(f" {current_bullet}")
            current_bullet = ""

    # Add any remaining text as the last bullet point
    if current_bullet:
        bullet_points.append(f" {current_bullet}")

    # Join all bullet points into a single string with newline characters
    return '\n'.join(bullet_points)



if __name__ == '__main__':
    app.run(debug=True)

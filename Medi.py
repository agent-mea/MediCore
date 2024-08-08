import streamlit as st
import pandas as pd
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from playsound import playsound

# Initialize the OpenAI model with your API key
# Replace 'your-api-key-here' with your actual API key for OpenAI
llm = OpenAI(api_key='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')

# Load the CSV file containing conversation data
# Ensure the encoding matches your CSV file's encoding
text_data = pd.read_csv('Conversation(Sheet1).csv', encoding='ISO-8859-1')

# Define the prompt template for the chatbot
prompt_template = PromptTemplate(
    input_variables=["symptoms", "question"],
    template="""
    You are a friendly, supportive, and professional mental health chatbot. Your job is to provide users with professional advice, credible sources, and support for their mental health needs.

    Here's what you should do:
    1. Based on the user's symptoms: {symptoms}, provide an accurate assessment of their mental health situation.
    2. Answer the user's question: {question}, using a friendly and understanding tone.
    3. Suggest practical solutions and personally tailored goals to help the user manage their symptoms.
    4. Provide credible sources where the user can find more information or get further help.

    Always remember to be supportive and professional in your responses.
    """
)

# Create a LangChain with the OpenAI model and the prompt template
chain = LLMChain(llm=llm, prompt=prompt_template)

# Function to get a response from the chatbot based on symptoms and a question
def get_response(symptoms, question):
    # Run the chain to get a response based on the symptoms and question
    response = chain.run(symptoms=symptoms, question=question)
    return response

# Streamlit app configuration
st.set_page_config(
    page_title="MediCore Chatbot",
    page_icon="💡",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling the Streamlit app
st.markdown(
    """
    <style>
    .main {
        background-color: #0077B6; /* Main background color */
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #BA324F; /* Button background color */
        color: white;
    }
    .stTextInput>div>div>input {
        color: black;
        padding: 10px;
        border-radius: 5px;
    }
    .centered-text {
        text-align: center; /* Center align text */
        font-size: 20px;
        margin: 20px 0;
    }
    /* Custom sidebar style */
    .css-1d391kg {
        background-color: #FFD60A; /* Sidebar background color */
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display motivational messages
st.markdown('<div class="centered-text">Daily Motivation 💬</div>', unsafe_allow_html=True)
st.markdown('<div class="centered-text">You are stronger than you think. Take it one step at a time.</div>', unsafe_allow_html=True)

# Title and welcome message
st.title("MediCore Chatbot 💡")
st.write("Welcome to MediCore! I’m Medi, your digital mental health companion — here to support you with empathetic conversations.")

# Sidebar for selecting symptoms
st.sidebar.subheader('Symptom Checker 🩺')
selected_symptom = st.sidebar.radio(
    "How do you feel today?",
    ('😔 Feeling Anxious', '😞 Feeling Depressed', '😓 Feeling Stressed', '🛌 Trouble Sleeping', '🤕 Physical Symptoms')
)

# Main content form for asking questions
with st.form(key='question_form'):
    question = st.text_input("How can I help you?")
    submit_button = st.form_submit_button(label='Send')

# Handle form submission
if submit_button:
    if question:
        # Get response from the chatbot based on the question and selected symptoms
        answer = get_response(selected_symptom, question)
        st.write("### Answer")
        st.write(answer)
        # Play a sound notification after getting the answer
        playsound('notification_sound.mp3')
    else:
        st.write("Please enter a question.")

# Footer with additional information
st.markdown(
    """
    <hr>
    <footer>
    <div class="centered-text">
    <p>Created by the Innovative Sparks. This chatbot does not replace human interaction. Seek help from nearby facilities.</p>
    </div>
    </footer>
    """,
    unsafe_allow_html=True
)

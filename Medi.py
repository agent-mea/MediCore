import streamlit as st
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from playsound import playsound

# Initialize the OpenAI model with your API key
llm = OpenAI(api_key='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')

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

# Create a LangChain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Example symptoms
symptoms = "The user is experiencing symptoms of anxiety and depression."

# Get a question from the user (for example purposes)
question = "What can I do to feel better?"

def get_response(data_description, question):
    # Running the chain to get a response based on the data description and a question
    response = chain.run(symptoms=data_symptoms, question=question)
    return response

# Streamlit app
st.set_page_config(
    page_title="MediCore Chatbot",
    page_icon="💡",
    layout="centered",
    initial_sidebar_state="expanded", 
)

st.markdown(
    """
    <style>
    .main {
        background-color: #0077B6;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #BA324F;
        color: white;
    }
    .stTextInput>div>div>input {
        color: black;
        padding: 10px;
        border-radius: 5px;
    }
    .centered-text {
        text-align: center;
        font-size: 20px;
        margin: 20px 0;
    }
    /*Custom sidebar style*/
    .css-1d391kg {
        background-color: #FFD60A;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="centered-text">Daily Motivation 💬</div>', unsafe_allow_html=True)
st.markdown('<div class="centered-text">You are stronger than you think. Take it one step at a time.</div>', unsafe_allow_html=True)

st.title("MediCore Chatbot 💡")
st.write("Welcome to MediCore! I’m Medi, your digital mental health companion — here to support you with empathetic conversations.")

st.sidebar.subheader('Symptom Checker 🩺')
selected_symptom = st.sidebar.radio(
    "# How do you feel today?",
    ('😔 Feeling Anxious', '😞 Feeling Depressed', '😓 Feeling Stressed', '🛌 Trouble Sleeping', '🤕 Physical Symptoms')
)

# Main content

with st.form(key='question_form'):
    question = st.text_input("How can I help you?")
    submit_button = st.form_submit_button(label='Send')

if submit_button:
    if question:
        answer = get_response(symptoms, question)
        st.write("### Answer")
        st.write(answer)
        playsound('notification_sound.mp3')  # Play a sound after getting the answer
    else:
        st.write("Please enter a question.")

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

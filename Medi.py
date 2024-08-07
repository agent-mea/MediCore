import streamlit as st
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from playsound import playsound

# Initialize the OpenAI model with your API key
llm = OpenAI(api_key='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')


# Define a prompt template for querying
prompt_template = PromptTemplate(
    input_variables=["data_description", "question"],
    template="""
    You are a data analyst. Here is the data you have:
    {data_description}

    Based on this data, answer the question: {question}
    """
)

# Create a LangChain
chain = LLMChain(llm=llm, prompt=prompt_template)

def get_response(data_description, question):
    # Running the chain to get a response based on the data description and a question
    response = chain.run(data_description=data_description, question=question)
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
        background-color: #03045E;
        color: white;
    }
    /*Custom sidebar style*/
    .css-1d391kg {
        background-color: #FFD60A;
        color: black;
    }
    </style>
    .stTextInput>div>div>input {
        color: white;
        padding: 10px;
        border-radius: 5px;
    }
    .centered-text {
        text-align: center;
        font-size: 20px;
        margin: 20px 0;
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
        answer = get_response(data_description, question)
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

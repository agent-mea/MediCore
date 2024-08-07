import streamlit as st
import openai
import pandas as pd
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Initialize the OpenAI model with your API key
llm = OpenAI(api_key='sk-None-CqwuxMIliksoBMbP99LHT3BlbkFJeSXBu9ElyhWvC9hg6TN0')
openai.api_key = 'api_key='sk-None-CqwuxMIliksoBMbP99LHT3BlbkFJeSXBu9ElyhWvC9hg6TN0'



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
st.title("MediCore Chatbot")

data_description = "Data includes various facts about countries, such as capitals and population sizes and hurricane data"
st.write("### Data Description")
st.write(data_description)

from playsound import playsound  # for playing audio

# Function to play peaceful sound
def play_peaceful_sound():
    playsound('peaceful_sound.mp3')

# Set page configuration
st.set_page_config(
    page_title="MediCore Chatbot",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for theme selection and other options
st.sidebar.title('Settings 🛠️')

# Theme selection
theme_mode = st.sidebar.radio(
    "Choose Theme:",
    ('Light', 'Dark')
)

# Toggle theme based on user selection
if theme_mode == 'Dark':
    st.markdown(
        """
        <style>
        body {
            color: white;
            background-color: #333;
        }
        .st-bb, .st-bc, .st-c5, .st-c6, .st-cz {
            color: white;
        }
        .st-d7, .st-dg, .st-dh {
            color: #d6d7d8;
        }
        .st-dt, .st-dx {
            background-color: #222;
        }
        .st-dw, .st-ef {
            background-color: #444;
        }
        .st-f6 {
            box-shadow: none;
        }
        .st-f9 {
            color: white;
            background-color: #444;
        }
        .st-e3 {
            background-color: #666;
        }
        .st-cc {
            color: #bbb;
        }
        .st-ej, .st-f7, .st-fe {
            color: #ddd;
        }
        .st-e7 {
            background-color: #555;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body {
            color: black;
            background-color: white;
        }
        .st-bb, .st-bc, .st-c5, .st-c6, .st-cz {
            color: black;
        }
        .st-d7, .st-dg, .st-dh {
            color: #333;
        }
        .st-dt, .st-dx {
            background-color: #f0f0f0;
        }
        .st-dw, .st-ef {
            background-color: #f5f5f5;
        }
        .st-f6 {
            box-shadow: none;
        }
        .st-f9 {
            color: black;
            background-color: #f5f5f5;
        }
        .st-e3 {
            background-color: #ddd;
        }
        .st-cc {
            color: #777;
        }
        .st-ej, .st-f7, .st-fe {
            color: #555;
        }
        .st-e7 {
            background-color: #eee;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Sidebar for symptom checker and daily motivation
st.sidebar.title('Symptom Checker 🩺')
selected_symptom = st.sidebar.radio(
    "Choose an option:",
    ('😔 Feeling Anxious', '😞 Feeling Depressed', '😓 Feeling Stressed', '🛌 Trouble Sleeping', '🤕 Physical Symptoms')
)

st.sidebar.title('Daily Motivation 💬')
motivation_quote = st.sidebar.text("You are stronger than you think. Take it one step at a time.")

# Main content
st.title('Welcome to MediCore 🌟')
st.write("Hello there! I'm Medi, here to support you. How are you feeling today?")

# Play peaceful sound
play_peaceful_sound()


question = st.text_input("Enter a question about the data:")
if st.button("Get Answer"):
    if question:
        answer = get_response(data_description, question)
        st.write("### Answer")
        st.write(answer)
    else:
        st.write("Please enter a question.")

if __name__ == "__main__":
    st.write("Run this script with Streamlit by using the command: `streamlit run Medi.py`")

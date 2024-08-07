import streamlit as st
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Initialize the OpenAI model with your API key
llm = OpenAI(api_key='sk-None-CqwuxMIliksoBMbP99LHT3BlbkFJeSXBu9ElyhWvC9hg6TN0')

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

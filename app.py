# Q&A Chatbot
from langchain.llms import GooglePalm
from dotenv import load_dotenv

load_dotenv() # takes environment variables from .env file

import streamlit as st
import os

## Function to load GooglePalm model and get responses

def get_googlepalm_response(question):
    llm = GooglePalm(google_api_key=os.getenv("GOOGLE_API_KEY"), model="text-bison@002", temperature=0.6)
    response = llm.predict(question)
    return response

# initialize our streamlit application
st.set_page_config(page_title="Q&A Demo")

st.header("Q&A Chatbot Application")

input = st.text_input("Input: ", key="input")
response=get_googlepalm_response(input)

submit=st.button("Ask the question")

# If Ask button is clicked

if submit:
    st.header("The Response is")
    st.write(response)


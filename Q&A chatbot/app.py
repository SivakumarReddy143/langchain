import streamlit as st
from langchain_groq import ChatGroq
# from groq import Groq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']="Q&A Chatbot with Groq"

## Prompt Template

prompt=ChatPromptTemplate.from_messages([
    ('system',"you are a helpful AI assistant. Please give response to the user queries"),
    ('user',"Question:{question}")
])
# client=Groq()

def generate_response(question,api_key,llm,temperature,max_token):
    # llm=client.chat.completions.create(model=llm)
    llm=ChatGroq(api_key=api_key,model=llm,temperature=temperature,max_tokens=max_token)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## Title of the app

st.title("Enhanced Q&A chatbot with Groq")

## sidebar for settings

st.sidebar.title('settings')
api_key=st.sidebar.text_input("Enter your api_key",type='password')
llm=st.sidebar.selectbox('select an groq model',["llama-3.1-70b-versatile","llama-3.1-8b-instant",
                                                 "llama3-70b-8192","gemma2-9b-it",
                                                 "llama-3.1-8b-instant",
                                                 "mixtral-8x7b-32768","gemma2-9b-it"])

## Adjust response parameter

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=1000,value=150)

## Main interface for user input

st.write("Go ahead and ask any question")
user_input=st.text_input("You:")
button=st.button("Get response")
if button:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)

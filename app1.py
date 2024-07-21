from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')

prompt=ChatPromptTemplate.from_messages([
    ('system','you are a helpful coding assistant. please provide optimized full python codes without any explanation'),
    ('user','Question:{question}')
])
st.title("Python Code Generator")
input=st.text_input('enter your query...')
llm=GoogleGenerativeAI(model="models/gemini-1.5-pro")
output_parser=StrOutputParser()

chain=prompt|llm|output_parser
button=st.button("click here to get response")

if button:
    response=chain.invoke({'question':input})
    st.write(response)
import streamlit as st
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

st.title("🦜🔗 Quickstart App")
def generate_response(input_text):
    model = ChatGroq(model="llama-3.1-8b-instant",api_key=GROQ_API_KEY)
    st.info(model.invoke(input_text).content)

with st.form("my_form"):
    text = st.text_area(
        "Enter text:"
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
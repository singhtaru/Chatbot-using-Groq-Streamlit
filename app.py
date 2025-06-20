import streamlit as st
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set page configuration
st.set_page_config(page_title="🦙 Chat with LLaMA", page_icon="🧠", layout="centered")

st.title("🦙 Chat with LLaMA 3.1 - Groq API")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.success("Chat history cleared!")

# Display chat history using chat bubbles
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your question here..."):
    # Add user message to session
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display bot "typing..." spinner
    with st.chat_message("assistant"):
        with st.spinner("LLaMA is thinking..."):
            try:
                # Invoke the model
                model = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
                response = model.invoke(prompt).content
            except Exception as e:
                response = f"⚠️ Error: {str(e)}"
            st.markdown(response)

    # Save assistant response to session
    st.session_state.messages.append({"role": "assistant", "content": response})

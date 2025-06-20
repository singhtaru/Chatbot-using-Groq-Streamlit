---

# 🧠 ChatGPT-Powered Chatbot with Groq & Streamlit

A simple and lightweight chatbot built using [Groq's llama-3.1-8b-instant](https://groq.com) and [Streamlit](https://streamlit.io/) for an interactive frontend. This chatbot can handle general queries and assist users through a conversational interface.

---

## 🚀 Features

* 🤖 Chat with Groq’s high-speed LLM (llama-3.1-8b-instant)
* ⚡ Fast, streaming responses
* 🌐 Simple and interactive UI with Streamlit
* 🧠 Maintains chat history in-session

---

## 🖼️ Preview

![img_1.png](img_1.png)

---

## 🧰 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM API:** Groq (llama-3.1-8b-instant)
* **Environment Variables:** `python-dotenv`

---

## 📦 Installation

```bash
git clone https://github.com/your-username/chatbot-groq-streamlit.git
cd chatbot-groq-streamlit
```

---

## 🔐 Setup Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📝 Usage

* Enter your query in the text box.
* The chatbot will respond using Groq's LLaMA model.

---

## 📁 File Structure

```
chatbot-groq-streamlit/
│
├── app.py                # Main Streamlit app
communication
└── .env                  # (Your API key goes here)
```

---

## 🧠 Powered By

* [Groq API](https://console.groq.com/)
* [Streamlit](https://streamlit.io/)

---

## 📌 Future Improvements

* Integrate other LLMs (Claude, Gemini, OpenRouter)
* Voice input/output support
* Deploy on Streamlit Cloud or Hugging Face Spaces

---

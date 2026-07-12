import streamlit as st
from google import genai
from google.genai import types
import os
# 1. Web Page Setup & Safety Disclaimers
st.set_page_config(page_title="MedGuard AI", page_icon="🛡️", layout="centered")
st.title("🛡️ MedGuard: Medical Info Assistant")
st.warning("⚠️ **Disclaimer:** This application is an AI educational prototype. It does not provide clinical diagnoses or replace professional medical advice.")

# 2. Securely Configure the Gemini Client
# Replace the text below with the actual key you copied from Google AI Studio
API_KEY = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))
client = genai.Client(api_key=API_KEY)
# 3. System Guardrails (Instructing the LLM how to behave)
SYSTEM_PROMPT = """
You are a helpful medical information assistant. Your job is ONLY to explain medical terms, drug purposes, and list known drug-to-drug interactions in plain, easy-to-understand text.
- Critical Rule 1: Do NOT diagnose the user's symptoms.
- Critical Rule 2: Do NOT prescribe or suggest new medications.
- Critical Rule 3: Always include a bold reminder to consult a registered healthcare professional at the absolute end of every response.
"""

# 4. Initialize Chat Session State (Keeps track of conversation history)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages if they exist
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 5. Capture and Process User Input
if user_query := st.chat_input("Ask about a medication (e.g., 'What is Paracetamol used for?')"):
    
    # Display the user's question instantly in the UI
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)
        
    # Query Gemini using the unified Google GenAI SDK
    with st.spinner("Analyzing medical context safely..."):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_query,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.3, # Low temperature ensures focused, factual, less creative responses
                )
            )
            ai_output = response.text
        except Exception as e:
            ai_output = f"An error occurred while connecting to the AI backend: {str(e)}"
    
    # Display the AI response in the UI
    with st.chat_message("assistant"):
        st.markdown(ai_output)
    st.session_state.messages.append({"role": "assistant", "content": ai_output})
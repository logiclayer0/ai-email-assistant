import os
import streamlit as st
from groq import Groq
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your_groq_api_key_here")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY is missing! Please set it in Streamlit Secrets.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

def summarize_email(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert email assistant. Summarize the user's email into concise bullet points with key action items."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

def generate_draft(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a professional email composer. Write a clear, well-structured, and polite email reply based on the user's instructions."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

st.set_page_config(page_title="AI Email Assistant", page_icon="📧", layout="centered")

st.title("📧 AI Email Assistant")
st.write("Summarize long emails or generate quick professional drafts in seconds!")

tab1, tab2 = st.tabs(["📌 Summarize Email", "✍️ Draft Generator"])

with tab1:
    st.subheader("Email Summarizer")
    email_input = st.text_area("Paste your email text here:", height=200, key="sum_input")
    
    if st.button("Summarize Email", type="primary"):
        if email_input.strip():
            with st.spinner("Processing summary with AI..."):
                try:
                    summary = summarize_email(email_input)
                    st.success("### Summary:")
                    st.write(summary)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please paste an email first!")

with tab2:
    st.subheader("Email Draft Generator")
    draft_prompt = st.text_area("Enter key points for your reply (e.g., 'Say yes to meeting tomorrow at 3 PM'):", height=150, key="draft_input")
    
    if st.button("Generate Reply Draft", type="primary"):
        if draft_prompt.strip():
            with st.spinner("Generating draft with AI..."):
                try:
                    draft = generate_draft(draft_prompt)
                    st.success("### Generated Draft:")
                    st.write(draft)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter some instructions first!")
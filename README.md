# AI Email Assistant 📧

An AI-powered tool that summarizes long emails into quick action points and generates ready-to-send professional email drafts — built for a hackathon MVP.

## 🚀 Features

- **Email Summarizer**: Paste a long email, get a clean 3-bullet-point summary with key action items.
- **Draft Generator**: Enter short instructions, get a ready-to-send professional email response.

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Backend AI**: Groq API (Llama 3 / Gemma models)
- **Language**: Python

## 🔗 Live Demo

[Try it here](https://ai-email-assistant-y6m87ssg5f5u5j2vscd3nk.streamlit.app/)

## 👥 Team

- Mahek Bajpai — UI & AI Integration
- Jaspreet Kaur — Testing & Deployment, Documentation

## ⚙️ How It Works

1. User pastes an email or types instructions into the Streamlit interface.
2. The input is sent to the Groq API with a tailored prompt.
3. Groq's Llama 3 model processes the request and returns a summary or draft.
4. The result is displayed instantly in the app.

## 🏃 Running Locally

```bash
pip install streamlit groq
streamlit run app.py
```

Note: To run this project on your own machine, you'll need your own Groq API key. Add it inside the `secrets.toml` file before running the app.

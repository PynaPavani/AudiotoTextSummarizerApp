import streamlit as st
import google.generativeai as genai
import os
import tempfile

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

st.title("Audio to Text Summarizer App")
file=st.file_uploader("Upload your audio file",type=['mp3','wav'])

def save_uploaded_file(uploaded_file):
    """Save uploaded file to a temporary file and return the path."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        st.error(f"Error handling uploaded file: {e}")
        return None

if file is not None:
    audio_path=save_uploaded_file(file)
    audio_file = genai.upload_file(path=audio_path)
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

            response = model.generate_content([
        "Please summarize the following audio.",
        audio_file
        ])
            st.info(response.text)    
    


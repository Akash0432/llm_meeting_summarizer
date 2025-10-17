# streamlit_app.py
"""
Streamlit Frontend for Meeting Summarizer
----------------------------------------
1. Upload meeting audio (.mp3 / .wav)
2. Transcribe using Whisper
3. Summarize using Gemini
4. Display & save outputs
"""

import streamlit as st
import os
from summarizer_utils import transcribe_audio, summarize_with_gemini, save_outputs

# ---------------------- PAGE SETUP ----------------------
st.set_page_config(page_title="Meeting Summarizer", page_icon="🎙️", layout="centered")
st.title("🎙️ AI Meeting Summarizer")
st.markdown("Upload your meeting audio and get a clear summary, key decisions, and action items.")

# ---------------------- SIDEBAR ----------------------
st.sidebar.header("⚙️ Settings")
st.sidebar.markdown("Choose options before summarization:")

# Prefix for file saving
file_prefix = st.sidebar.text_input("Enter Meeting Name (for saving files):", "meeting")

# ---------------------- MAIN APP ----------------------
uploaded_file = st.file_uploader("📂 Upload meeting audio", type=["mp3", "wav"])

if uploaded_file is not None:
    # Save temporarily
    temp_path = os.path.join("outputs", uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ File uploaded successfully!")

    if st.button("🚀 Start Summarization"):
        with st.spinner("Transcribing audio... ⏳"):
            transcript = transcribe_audio(temp_path)

        if "Error" not in transcript:
            st.text_area("📝 Transcript:", transcript, height=200)
        else:
            st.error("Transcription failed. Check console logs.")
            st.stop()

        with st.spinner("Generating summary with Gemini... 🧠"):
            summary = summarize_with_gemini(transcript)

        if "Error" not in summary:
            st.markdown("## 📋 Meeting Summary")
            st.write(summary)
        else:
            st.error("Summary generation failed.")
            st.stop()

        # Save outputs
        save_outputs(file_prefix, transcript, summary)

        st.success("✅ Process complete! Files saved in the 'outputs' folder.")
        st.download_button("⬇️ Download Transcript", data=transcript, file_name="transcript.txt")
        st.download_button("⬇️ Download Summary", data=summary, file_name="summary.txt")

else:
    st.info("Please upload a meeting audio file to begin.")

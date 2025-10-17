import streamlit as st
import os
import tempfile
from summarizer_utils import transcribe_audio, summarize_with_gemini, save_outputs

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="🎙️ AI Meeting Summarizer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------- HEADER ----------------------
st.title("🎙️ AI Meeting Summarizer")
st.caption("Convert meeting audio → transcript → summary using Whisper + Gemini 2.5")

# ---------------------- SIDEBAR ----------------------
st.sidebar.header("⚙️ Settings")
st.sidebar.markdown("Upload an audio file to get a transcript and summary of key points discussed.")
st.sidebar.info("Supported formats: `.mp3`, `.wav` (up to 25MB)")

# ---------------------- FILE UPLOAD ----------------------
uploaded_file = st.file_uploader("📤 Upload your meeting audio", type=["mp3", "wav"])

if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")

    # Create a temporary file safely (fix for Streamlit Cloud)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.audio(uploaded_file, format="audio/mp3")

    # ---------------------- CONTEXT INPUT ----------------------
    context = st.text_area(
        "🗒️ Optional context for better summarization",
        placeholder="Example: 'Team meeting about AI ethics and corporate responsibility.'"
    )

    # ---------------------- BUTTON ----------------------
    if st.button("🚀 Start Summarization"):
        with st.spinner("⏳ Transcribing audio... please wait"):
            transcript = transcribe_audio(temp_path)

        if "Error" in transcript:
            st.error("❌ Transcription failed. Check logs for details.")
        else:
            st.subheader("🧾 Transcript:")
            st.text_area("Full Transcript", transcript, height=200)

            with st.spinner("🧠 Generating summary using Gemini..."):
                summary = summarize_with_gemini(transcript)

            if "Error" in summary:
                st.error("❌ Summary generation failed. Check Gemini API key or quota.")
            else:
                st.subheader("🧠 Summary:")
                st.markdown(summary)

                # Save outputs locally (only runs on local/dev)
                save_outputs("meeting_summary", transcript, summary)
                st.success("💾 Results saved successfully in outputs/ folder (if running locally).")

    # Cleanup temp file safely
    try:
        os.remove(temp_path)
    except Exception:
        pass

else:
    st.info("👆 Upload an audio file to begin summarization.")

# ---------------------- FOOTER ----------------------
st.markdown("---")
st.caption(
    "Built with ❤️ using OpenAI Whisper + Google Gemini 2.5 + Streamlit"
)

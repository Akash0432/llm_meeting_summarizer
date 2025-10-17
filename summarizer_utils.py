"""
Backend logic for Meeting Summarizer
------------------------------------
Handles:
1. Audio transcription using Whisper (lazy-loaded for Streamlit Cloud)
2. Text summarization using Gemini API
3. Saving results locally
"""

import os
import datetime
import whisper
import google.generativeai as genai
from dotenv import load_dotenv

# ---------------------- SETUP ----------------------
# Load environment variables (Gemini API key)
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)
else:
    raise ValueError("❌ Gemini API key not found. Add it to your .env file or Streamlit Secrets.")

# ---------------------- LAZY MODEL SETUP ----------------------
# Do not load Whisper on startup to avoid Streamlit Cloud memory crash
whisper_model = None

def get_whisper_model():
    """Load the Whisper model only when needed (lazy loading)."""
    global whisper_model
    if whisper_model is None:
        print("⏳ Loading Whisper model (base)...")
        whisper_model = whisper.load_model("base")
        print("✅ Whisper model loaded successfully.")
    return whisper_model


# ---------------------- FUNCTION 1 ----------------------
def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe an audio file (mp3/wav) to text using Whisper.
    """
    try:
        model = get_whisper_model()  # Load only when user uploads file
        print(f"🎧 Transcribing: {audio_path}")
        result = model.transcribe(audio_path)
        transcript = result["text"].strip()
        print("✅ Transcription complete.")
        return transcript
    except Exception as e:
        print("❌ Error during transcription:", e)
        return "Error: Transcription failed."


# ---------------------- FUNCTION 2 ----------------------
def summarize_with_gemini(transcript: str) -> str:
    """
    Summarize meeting transcript using Gemini API.
    Returns a formatted text including Summary, Key Decisions, and Action Items.
    """
    if not transcript or transcript.strip() == "":
        return "No transcript text found."

    try:
        print("🧠 Sending transcript to Gemini for summarization...")

        prompt = f"""
        You are an expert meeting assistant. Analyze the following meeting transcript and produce:
        1. A concise **Summary** (4–6 lines)
        2. A clear list of **Key Decisions** made
        3. A structured list of **Action Items** (with responsible person and due date if mentioned)
        
        Format output with clear headings: SUMMARY, DECISIONS, ACTION ITEMS.

        Transcript:
        {transcript}
        """

        # ✅ Using stable Gemini 2.5 Flash model
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(prompt)

        summary = response.text.strip() if response.text else "Error: Empty summary received."
        print("✅ Summary generated successfully.")
        return summary

    except Exception as e:
        print("❌ Error during Gemini summarization:", e)
        return f"Error: {e}"


# ---------------------- FUNCTION 3 ----------------------
def save_outputs(prefix: str, transcript: str, summary: str):
    """
    Save transcript and summary to outputs/ folder with timestamped filenames.
    """
    os.makedirs("outputs", exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    transcript_path = os.path.join("outputs", f"{prefix}_{timestamp}_transcript.txt")
    summary_path = os.path.join("outputs", f"{prefix}_{timestamp}_summary.txt")

    try:
        with open(transcript_path, "w", encoding="utf-8") as t:
            t.write(transcript)
        with open(summary_path, "w", encoding="utf-8") as s:
            s.write(summary)
        print(f"💾 Files saved:\n  - {transcript_path}\n  - {summary_path}")
    except Exception as e:
        print("❌ Error saving files:", e)

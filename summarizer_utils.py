"""
Backend logic for Meeting Summarizer
------------------------------------
Handles:
1. Audio transcription using Whisper
2. Text summarization using Gemini 2.5 API
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
    raise ValueError("❌ Gemini API key not found. Add it to your .env file.")

# Optional: if low space on C:, store Whisper models in D:
# os.environ["XDG_CACHE_HOME"] = "D:/whisper_cache"

# Load Whisper model once at startup
# Use "base" (~142MB) if disk space is low
print("⏳ Loading Whisper model (small)...")
whisper_model = whisper.load_model("base")
print("✅ Whisper model loaded successfully.")


# ---------------------- FUNCTION 1 ----------------------
def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe an audio file (mp3/wav) to text using Whisper.
    """
    try:
        print(f"🎧 Transcribing: {audio_path}")
        result = whisper_model.transcribe(audio_path)
        transcript = result["text"].strip()
        print("✅ Transcription complete.")
        return transcript
    except Exception as e:
        print("❌ Error during transcription:", e)
        return "Error: Transcription failed."


# ---------------------- FUNCTION 2 ----------------------
def summarize_with_gemini(transcript: str) -> str:
    """
    Summarize meeting transcript using Gemini 2.5 API.
    Returns a formatted text including Summary, Key Decisions, and Action Items.
    """
    if not transcript or transcript.strip() == "":
        return "No transcript text found."

    try:
        print("🧠 Sending transcript to Gemini 2.5 for summarization...")

        prompt = f"""
        You are an expert meeting assistant. Analyze the following meeting transcript and produce:
        1. A concise **Summary** (4–6 lines)
        2. A clear list of **Key Decisions** made
        3. A structured list of **Action Items** (with responsible person and due date if mentioned)

        Format output with clear headings: SUMMARY, DECISIONS, ACTION ITEMS.

        Transcript:
        {transcript}
        """

        # ✅ Using Gemini 2.5 Flash (verified available for your key)
        model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")

        response = model.generate_content(
            contents=prompt,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 1024,
            },
        )

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

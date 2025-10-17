# 🎙️ AI Meeting Summarizer  
> Transcribe meeting audio → Generate summary, key decisions, and action items using Whisper + Gemini 2.5  

---

## 📘 Overview
**AI Meeting Summarizer** is an intelligent web application that automatically converts spoken meeting audio into structured text summaries.  
It uses:
- **Whisper** (OpenAI) for speech-to-text transcription  
- **Gemini 2.5** (Google Generative AI) for meeting summarization and insights  
- **Streamlit** for an easy-to-use web interface  

This project demonstrates seamless integration of a local ML model with a cloud-based LLM API.

---

## 🚀 Features
✅ Upload meeting audio (.mp3 / .wav)  
✅ Real-time transcription using Whisper  
✅ Summary generation using Gemini 2.5  
✅ Extracts **Summary**, **Key Decisions**, and **Action Items**  
✅ Download transcript & summary as text files  
✅ Clean, interactive Streamlit interface  

---

## 🧱 Tech Stack

| Layer | Tool / Library |
|:--|:--|
| Frontend | Streamlit |
| Backend | Python (Flask-style within Streamlit) |
| Speech-to-Text | `openai-whisper` |
| Summarization | `google-generativeai` (Gemini 2.5 Flash) |
| Config | `python-dotenv` |
| Deployment | Streamlit Cloud |

---

## 🗂️ Folder Structure


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
meeting_summarizer/
│
├── streamlit_app.py # 🎯 Main Streamlit application file
├── summarizer_utils.py # 🧠 Backend logic (Whisper + Gemini)
├── requirements.txt # 📦 Dependencies list
├── .gitignore # 🚫 Ignore unnecessary / sensitive files
├── README.md # 📘 Project documentation
│
├── .env # 🔑 Local file containing GEMINI_API_KEY (not pushed)
│
├── .streamlit/ # ⚙️ Streamlit configuration folder
│ └── config.toml # Custom UI + server settings
│
├── outputs/ # 💾 Auto-saved transcripts and summaries (local only)
│ ├── sample_20251017_summary.txt
│ └── sample_20251017_transcript.txt
│
└── samples/ # 🎧 Optional: test audio samples (<1 MB)
└── meeting_sample.mp3
---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the Repository
git clone https://github.com/<your-username>/meeting-summarizer-ai.git
cd meeting-summarizer-ai


### 2️⃣ Create and Activate Virtual Environment
python -m venv .venv
.venv\Scripts\Activate.ps1 # (Windows PowerShell)


### 3️⃣ Install Dependencies
pip install -r requirements.txt


### 4️⃣ Add Environment Variable
Create a file named `.env` in your project root and add:
GEMINI_API_KEY=your_api_key_here


### 5️⃣ Run the Application

Then open your browser and go to → [http://localhost:8501](http://localhost:8501)

---

## ☁️ Deployment (Streamlit Cloud)

### 🔹 Step 1: Push Project to GitHub
Include:
- streamlit_app.py  
- summarizer_utils.py  
- requirements.txt  
- .gitignore  
- README.md  
- .streamlit/config.toml  

Exclude:
- .env  
- outputs/  
- whisper_cache/  
- .venv/  

### 🔹 Step 2: Deploy
1. Go to [https://share.streamlit.io]()  
2. Click **“New app”** → select your repo and `streamlit_app.py`  
3. Add your Gemini API Key in **Secrets**:

4. Click **Deploy 🚀**

Your app will be live at:  
`https://<your-username>-meeting-summarizer-ai.streamlit.app`

---

## 🧠 Example Output
**Sample Input:**  
🎧 Audio: “The team discussed the app launch. Akash will handle the UI updates, and Priya will prepare the report by Monday.”

**Sample Output:**

📝 **SUMMARY**  
The meeting focused on the upcoming app launch.  
Akash is assigned to update the UI, while Priya will prepare the client report.  
The deadline for both tasks is Monday.

📌 **KEY DECISIONS**  
- App launch preparation continues on schedule.  
- UI updates assigned to Akash.  
- Report assigned to Priya (due Monday).  

✅ **ACTION ITEMS**  
- [Akash] Finalize UI improvements  
- [Priya] Draft and send report by Monday  

---

## 🧩 Requirements

| Requirement | Description |
|:--|:--|
| Python | Version 3.10 or higher |
| FFmpeg | Installed and added to PATH |
| Whisper | Automatically downloads model (~150–400 MB) |
| Gemini | Active API key from Google AI Studio |
| OS | Windows / macOS / Linux |

---

## 🧰 Troubleshooting

| Issue | Fix |
|:--|:--|
| ❌ ValueError: Gemini API key not found | Ensure `.env` contains `GEMINI_API_KEY` |
| ❌ No space left on device | Switch Whisper model to `"base"` or use D: drive cache |
| ❌ 404 model not found | Use `"models/gemini-2.5-flash"` or `"models/gemini-pro"` |
| ❌ ffmpeg not found | Install from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) |

---

## 🏁 Credits
Developed by **P. Akash**  
AI-Based Meeting Summarization System using Whisper + Gemini

---

## 📜 License
This project is for academic and demonstration purposes only.  
© 2025 Akash — All Rights Reserved.



# Studdy Buddy
AI-powered study focus tracker that detects your emotional state in real-time via webcam and coaches you to study smarter.

## What it does

Studdy Buddy uses your webcam to detect your emotional state while you study and maps it to one of three focus states:

-  **Focused** — you're in the zone
-  **Confused** — you've been struggling for a while
-  **Distracted** — your attention has drifted

At the end of each session it saves your stats, visualises your focus trends over time, and an AI study coach gives you personalised feedback based on your performance.

## Tech Stack


 - Frontend: Streamlit 
 - Computer Vision: OpenCV, FER (Facial Expression Recognition) 
 - LLM Coach : Ollama (llama3.2:1b — runs locally, privacy-first) 
 - Database : SQLite 
 - Charts : Plotly 
 - Language : Python 3.9 

##  Features

-  Real-time webcam face detection
-  Emotion-to-focus state mapping (Focused / Confused / Distracted)
-  Live session timer
-  Confusion alerts after 30 seconds of continuous confusion
-  Session history dashboard with focus trend charts
-  AI study coach powered by a local LLM (no data leaves your machine)
-  Session stats persisted to SQLite

##  How to Run

### Prerequisites
- Python 3.9+
- [Ollama](https://ollama.com/download) installed

### Setup
```bash
# Clone the repo
git clone https://github.com/AdelabuAderonke/studdy_buddy.git
cd studdy_buddy

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Pull the LLM model
ollama pull llama3.2:1b
```

### Run
```bash
# Start Ollama in one terminal tab
ollama serve

# Start the app in another terminal tab
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

##  Project Structure
```
studdy_buddy/
├── app.py            # Main Streamlit app
├── face_detector.py  # Webcam + emotion detection logic
├── coach.py          # LLM study coach
├── dashboard.py      # Session history + charts
├── database.py       # SQLite storage layer
└── requirements.txt  # Dependencies
```

##  Future Improvements

-  Adaptive Pomodoro timer based on focus patterns
-  Export session history to CSV
-  Email summary report after each session
-  Support for multiple users

##  What I Learned

- Building real-time computer vision pipelines with OpenCV and FER
- Managing Streamlit session state for stateful applications
- Integrating local LLMs with Ollama for privacy-first AI features
- Designing a lightweight data pipeline with SQLite

##  Author

**Aderonke Adelabu**  
[GitHub](https://github.com/AdelabuAderonke) · [LinkedIn](https://www.linkedin.com/in/aderonke-kausar-adelabu/)

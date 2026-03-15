import streamlit as st
import cv2
import time
from face_detector import FaceDetector
from database import init_db, save_session
from dashboard import show_dashboard
#title color to white
st.title("Studdy Buddy")
st.subheader("Stay on track, stay focused")

st.caption("Your AI-powered focus companion")

init_db()
# Initialise session state
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "state_counts" not in st.session_state:
    st.session_state.state_counts = {"Focused": 0, "Confused": 0, "Distracted": 0}
if "session_saved" not in st.session_state:
    st.session_state.session_saved = False
run = st.toggle("Start Session")
FRAME_WINDOW = st.image([])
status = st.empty()
timer_display = st.empty()
alert_display = st.empty() 

cap = cv2.VideoCapture(0)
start_time = time.time()
confused_since = None
state_counts = {"Focused": 0, "Confused": 0, "Distracted": 0}

if run:
    st.session_state.start_time = st.session_state.start_time or time.time()
    st.session_state.session_saved = False
    while run:
        frame = FaceDetector.get_frame(cap)
        if frame is None:
            st.error("Webcam not accessible")
            break
        #frame, face_detected = FaceDetector().detect_faces(frame)
        frame, state = FaceDetector.detect_state(frame)
        if state:
            for key in st.session_state.state_counts:
                if key in state:
                    st.session_state.state_counts[key] += 1
                    break
        if frame is None:
            status.warning("No face detected! please adjust your position or lighting")
            continue
    
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame_rgb)
        status.info(f"State: {state}")
        # Timer
        elapsed = int(time.time() - st.session_state.start_time)
        mins, secs = divmod(elapsed, 60)
        timer_display.metric("Session Time", f"{mins:02d}:{secs:02d}")
        # Confusion alert
        if "Confused" in str(state):
            if confused_since is None:
                confused_since = time.time()
            elif time.time() - confused_since > 30:
                alert_display.warning("You've been confused for a while — take a breath or re-read the last section!")
        else:
            confused_since = None
            alert_display.empty()
        time.sleep(0.1)
else:
    total = sum(st.session_state.state_counts.values())
    if total > 0:
        save_session(duration = int(time.time() - st.session_state.start_time),
                    focused = round(st.session_state.state_counts["Focused"] / total * 100, 2),
                    confused = round(st.session_state.state_counts["Confused"] / total * 100, 2),
                    distracted = round(st.session_state.state_counts["Distracted"] / total * 100, 2))   
        st.success("Session ended! Your focus data has been saved.")    

cap.release()
st.divider()
show_dashboard()

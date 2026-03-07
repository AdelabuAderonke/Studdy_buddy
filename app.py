import streamlit as st
import cv2
from face_detector import FaceDetector

st.title("📚 Study Buddy")
st.caption("Your AI-powered focus companion")

run = st.toggle("Start Session")
FRAME_WINDOW = st.image([])
status = st.empty()

cap = cv2.VideoCapture(0)

while run:
    frame = FaceDetector.get_frame(cap)
    if frame is None:
        st.error("Webcam not accessible")
        break

    #frame, face_detected = FaceDetector().detect_faces(frame)
    frame, state = FaceDetector.detect_state(frame)
    if frame is None:
        status.warning("No face detected 👀")
        continue
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame_rgb)
    status.info(f"State: {state}")
        
cap.release()

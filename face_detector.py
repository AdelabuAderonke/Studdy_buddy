import cv2
from fer import FER
detector = FER(mtcnn=False)
EMOTION_TO_STATE = {
    "happy": "Focused",
    "neutral": "Focused",
    "sad": "Confused",
    "fear": "Confused",
    "surprise": "Confused",
    "angry": "Distracted",
    "disgust": "Distracted"
}
STATE_COLOUR = {
    "Focused": (0, 255, 0),
    "Confused": (0, 165, 255),
    "Distracted": (0, 0, 255)
}
STATE_EMOJI = {
    "Focused": "Focused",
    "Confused": "Confused",
    "Distracted": "Distracted"
}
class FaceDetector:
    @staticmethod
    def get_frame(cap):
        ret, frame = cap.read()
        if not ret:
            return None
        return frame
    
    @staticmethod
    def detect_faces(frame):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        if frame is None:
            print("Error: Could not retrieve frame.")
            return
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        face_detected = len(faces) > 0
        return  frame, face_detected
    @staticmethod
    def detect_state(frame):
        result = detector.detect_emotions(frame)
        if not result:
            return None, None
        emotions = result[0]["emotions"]
        dominant_emotion = max(emotions, key=emotions.get)
        state = EMOTION_TO_STATE.get(dominant_emotion, "Focused")
        colour = STATE_COLOUR[state]
        
        # Draw box and label
        box = result[0]["box"]
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x + w, y + h), colour, 2)
        cv2.putText(frame, state, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, colour, 2)

        return frame, STATE_EMOJI[state]
if __name__ == "__main__":
    detector = FaceDetector()
    detector.detect_faces()
    
    
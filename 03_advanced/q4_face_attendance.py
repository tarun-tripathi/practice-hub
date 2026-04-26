# Q4: Face Recognition Attendance System
# Task: Register faces and mark attendance using webcam
# Library: face_recognition by ageitgey
# Install: pip install face_recognition opencv-python
# Note: Requires cmake and dlib installed first
# Docs: https://github.com/ageitgey/face_recognition

import face_recognition
import cv2
import csv
import os
from datetime import datetime

KNOWN_FACES_DIR = "known_faces"
ATTENDANCE_FILE = "attendance.csv"
os.makedirs(KNOWN_FACES_DIR, exist_ok=True)

known_encodings = []
known_names = []

def load_known_faces():
    for filename in os.listdir(KNOWN_FACES_DIR):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = face_recognition.load_image_file(
                os.path.join(KNOWN_FACES_DIR, filename)
            )
            encodings = face_recognition.face_encodings(img)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])
                print(f"Loaded: {filename}")

def mark_attendance(name):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ATTENDANCE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, now])
    print(f"Attendance marked: {name} at {now}")

def run_attendance():
    load_known_faces()
    video = cv2.VideoCapture(0)
    marked = set()

    print("Starting webcam. Press Q to quit.")
    while True:
        ret, frame = video.read()
        if not ret:
            break

        small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

        locations = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, locations)

        for encoding, location in zip(encodings, locations):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"

            if True in matches:
                name = known_names[matches.index(True)]
                if name not in marked:
                    mark_attendance(name)
                    marked.add(name)

            top, right, bottom, left = [v * 4 for v in location]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Attendance System", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()

# Add your face: save your photo as "YourName.jpg" in known_faces/ folder
# Then run: run_attendance()
run_attendance()
import os

files = {
"03_advanced/q1_student_ml_model.py": '''
# Q1: Student Performance Prediction Model
# Task: Train a ML model to predict if a student will pass or fail
# Models: Logistic Regression + Random Forest
# Dataset: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
# Install: pip install scikit-learn pandas

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("students_performance.csv")

# Create pass/fail column (pass if math score >= 40)
df["result"] = df["math score"].apply(lambda x: 1 if x >= 40 else 0)

# Encode categorical columns
le = LabelEncoder()
for col in ["gender", "race/ethnicity", "parental level of education",
            "lunch", "test preparation course"]:
    df[col] = le.fit_transform(df[col])

# Features and target
X = df.drop(["math score", "reading score", "writing score", "result"], axis=1)
y = df["result"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
print("=== Logistic Regression ===")
print(f"Accuracy: {accuracy_score(y_test, lr_pred):.2f}")
print(classification_report(y_test, lr_pred))

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
print("=== Random Forest ===")
print(f"Accuracy: {accuracy_score(y_test, rf_pred):.2f}")
print(classification_report(y_test, rf_pred))

print("=== Confusion Matrix (Random Forest) ===")
print(confusion_matrix(y_test, rf_pred))
''',

"03_advanced/q2_nlp_classifier.py": '''
# Q2: NLP Job Description Classifier
# Task: Classify job descriptions as tech / non-tech / management
# Tools: TfidfVectorizer + SVM
# Dataset: https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset
# Install: pip install scikit-learn pandas

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Sample dataset (replace with Kaggle dataset)
data = {
    "description": [
        "Python developer with Django and REST API experience",
        "Machine learning engineer with TensorFlow and PyTorch",
        "Marketing manager with social media and branding skills",
        "HR executive with recruitment and payroll experience",
        "Data scientist with pandas numpy and scikit-learn",
        "React developer with JavaScript and Node.js experience",
        "Sales manager with B2B enterprise sales experience",
        "DevOps engineer with Docker Kubernetes and CI/CD",
        "Content writer with SEO and copywriting skills",
        "Backend engineer with Java Spring Boot and microservices"
    ],
    "category": [
        "tech", "tech", "management", "management",
        "tech", "tech", "management", "tech",
        "non-tech", "tech"
    ]
}

df = pd.DataFrame(data)

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words="english", max_features=500)
X = tfidf.fit_transform(df["description"])
y = df["category"]

# Train SVM
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LinearSVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("=== Job Description Classifier ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred))

# Test new prediction
new_jobs = ["Full stack developer with React and Node", "Finance manager with budgeting skills"]
new_X = tfidf.transform(new_jobs)
predictions = model.predict(new_X)
for job, pred in zip(new_jobs, predictions):
    print(f"Job: {job[:40]}... -> Category: {pred}")
''',

"03_advanced/q3_resume_parser.py": '''
# Q3: Resume Parser
# Task: Extract name, email, phone, skills, education, experience from resume text
# Tools: spaCy for NER + regex for structured fields
# Install: pip install spacy && python -m spacy download en_core_web_sm
# Docs: https://spacy.io/usage/linguistic-features#named-entities

import re
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_LIST = [
    "python", "java", "javascript", "react", "node", "flask", "django",
    "machine learning", "deep learning", "sql", "mongodb", "docker",
    "kubernetes", "aws", "git", "tensorflow", "keras", "pandas", "numpy"
]

def extract_email(text):
    match = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
    return match[0] if match else None

def extract_phone(text):
    match = re.findall(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]", text)
    return match[0] if match else None

def extract_name(text):
    doc = nlp(text[:200])
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text):
    text_lower = text.lower()
    return [skill for skill in SKILLS_LIST if skill in text_lower]

def parse_resume(text):
    print("=== Resume Parser ===")
    print(f"Name:   {extract_name(text)}")
    print(f"Email:  {extract_email(text)}")
    print(f"Phone:  {extract_phone(text)}")
    print(f"Skills: {extract_skills(text)}")

# Sample resume text
sample_resume = """
Tarun Tripathi
tarun@email.com | +91 9999999999

Education:
B.Tech CSE-AIML, LNCT Bhopal, 2025

Experience:
Data Science Intern at Motherson Technology, 2024
- Built data cleaning pipeline using Python and Pandas
- Developed chatbot using LangChain and Flask

Skills:
Python, Machine Learning, Flask, Pandas, NumPy, SQL, Git, Docker
"""

parse_resume(sample_resume)
''',

"03_advanced/q4_face_attendance.py": '''
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
''',

"03_advanced/q5_rag_chatbot.py": '''
# Q5: RAG Chatbot from PDF
# Task: Build a chatbot that answers questions from a PDF document
# Stack: LangChain + ChromaDB + Ollama (local LLM)
# Install: pip install langchain chromadb pypdf sentence-transformers
# Ollama: https://ollama.ai -> ollama pull mistral
# Docs: https://python.langchain.com/docs/use_cases/question_answering/

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

PDF_PATH = "document.pdf"
DB_PATH = "chroma_db"

def load_and_index(pdf_path):
    print("Loading PDF...")
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(pages)
    print(f"Created {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(chunks, embeddings, persist_directory=DB_PATH)
    db.persist()
    print("Indexed and saved to ChromaDB")
    return db

def create_qa_chain(db):
    llm = Ollama(model="mistral")
    retriever = db.as_retriever(search_kwargs={"k": 3})
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa

def chat(qa_chain):
    print("RAG Chatbot ready. Type quit to exit.")
    while True:
        query = input("You: ")
        if query.lower() == "quit":
            break
        answer = qa_chain.run(query)
        print(f"Bot: {answer}\n")

db = load_and_index(PDF_PATH)
qa_chain = create_qa_chain(db)
chat(qa_chain)
''',

"03_advanced/q6_lstm_stock.py": '''
# Q6: Stock Price Prediction using LSTM
# Task: Predict future stock prices using LSTM neural network
# Data source: Yahoo Finance via yfinance library
# Install: pip install yfinance tensorflow keras scikit-learn matplotlib
# Docs: https://keras.io/api/layers/recurrent_layers/lstm/

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

STOCK = "TCS.NS"
START = "2020-01-01"
END = "2024-01-01"
LOOKBACK = 60

# Download data
print(f"Downloading {STOCK} data...")
df = yf.download(STOCK, start=START, end=END)
data = df["Close"].values.reshape(-1, 1)

# Scale data
scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)

# Create sequences
X, y = [], []
for i in range(LOOKBACK, len(scaled)):
    X.append(scaled[i - LOOKBACK:i, 0])
    y.append(scaled[i, 0])

X, y = np.array(X), np.array(y)
X = X.reshape(X.shape[0], X.shape[1], 1)

# Split
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Build LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(LOOKBACK, 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer="adam", loss="mean_squared_error")
model.summary()

print("Training model...")
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Predict
predictions = scaler.inverse_transform(model.predict(X_test))
actual = scaler.inverse_transform(y_test.reshape(-1, 1))

# Plot
plt.figure(figsize=(12, 6))
plt.plot(actual, label="Actual Price")
plt.plot(predictions, label="Predicted Price")
plt.title(f"{STOCK} Stock Price Prediction (LSTM)")
plt.xlabel("Days")
plt.ylabel("Price (INR)")
plt.legend()
plt.savefig("stock_prediction.png")
print("Plot saved as stock_prediction.png")
''',

"03_advanced/q7_cnn_classifier.py": '''
# Q7: CNN Image Classifier
# Task: Classify handwritten digits using a Convolutional Neural Network
# Dataset: MNIST (built into Keras, no download needed)
# Model: Conv2D -> MaxPool -> Dense
# Install: pip install tensorflow keras matplotlib
# Docs: https://keras.io

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocess
X_train = X_train.reshape(-1, 28, 28, 1) / 255.0
X_test = X_test.reshape(-1, 28, 28, 1) / 255.0
y_train = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# Build CNN
model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation="relu"),
    Dropout(0.3),
    Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()

print("Training CNN...")
history = model.fit(X_train, y_train, epochs=5, batch_size=64,
                    validation_split=0.1, verbose=1)

loss, acc = model.evaluate(X_test, y_test_cat)
print(f"\nTest Accuracy: {acc:.4f}")

# Plot sample predictions
predictions = model.predict(X_test[:10])
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flatten()):
    ax.imshow(X_test[i].reshape(28, 28), cmap="gray")
    ax.set_title(f"Pred: {np.argmax(predictions[i])} | True: {y_test[i]}")
    ax.axis("off")
plt.tight_layout()
plt.savefig("cnn_predictions.png")
print("Predictions saved as cnn_predictions.png")
''',

"03_advanced/q8_data_pipeline.py": '''
# Q8: Real-time Data Pipeline
# Task: Scrape data -> clean with pandas -> store in SQLite -> visualize on dashboard
# Tools: BeautifulSoup, pandas, SQLite, Plotly Dash
# Install: pip install requests beautifulsoup4 pandas plotly dash
# Dash Docs: https://dash.plotly.com/

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime
import dash
from dash import dcc, html
import plotly.express as px

DB = "pipeline.db"

def scrape_data():
    url = "https://news.ycombinator.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    stories = []
    for item in soup.select(".athing")[:20]:
        title_tag = item.select_one(".titleline a")
        score_tag = item.find_next_sibling("tr").select_one(".score")
        if title_tag:
            stories.append({
                "title": title_tag.text.strip()[:80],
                "score": int(score_tag.text.replace(" points", "")) if score_tag else 0,
                "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return stories

def clean_and_store(stories):
    df = pd.DataFrame(stories)
    df.drop_duplicates(subset=["title"], inplace=True)
    df = df[df["score"] > 0]
    df.sort_values("score", ascending=False, inplace=True)

    conn = sqlite3.connect(DB)
    df.to_sql("stories", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Stored {len(df)} stories in database")
    return df

def load_from_db():
    conn = sqlite3.connect(DB)
    df = pd.read_sql("SELECT * FROM stories ORDER BY score DESC", conn)
    conn.close()
    return df

# Run pipeline
print("Running pipeline...")
stories = scrape_data()
df = clean_and_store(stories)

# Dashboard
app = dash.Dash(__name__)
df = load_from_db()

app.layout = html.Div([
    html.H1("Hacker News Dashboard", style={"textAlign": "center"}),
    dcc.Graph(
        figure=px.bar(
            df.head(10), x="score", y="title",
            orientation="h", title="Top 10 Stories by Score",
            color="score", color_continuous_scale="blues"
        )
    )
])

if __name__ == "__main__":
    print("Dashboard running at http://127.0.0.1:8050")
    app.run(debug=True)
''',

"03_advanced/q9_semantic_search.py": '''
# Q9: Semantic Search over Google Drive Documents
# Task: Search your Google Drive docs using semantic similarity
# Tools: LangChain + ChromaDB + Google Drive API
# Install: pip install langchain chromadb sentence-transformers google-api-python-client
# Auth setup: https://developers.google.com/drive/api/quickstart/python

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
DB_PATH = "semantic_search_db"

def authenticate_google():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as f:
            f.write(creds.to_json())
    return build("drive", "v3", credentials=creds)

def fetch_docs(service):
    results = service.files().list(
        q="mimeType='application/vnd.google-apps.document'",
        fields="files(id, name)"
    ).execute()
    return results.get("files", [])

def index_documents(docs_text):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    documents = [Document(page_content=text["content"], metadata={"name": text["name"]})
                 for text in docs_text]
    db = Chroma.from_documents(documents, embeddings, persist_directory=DB_PATH)
    db.persist()
    print(f"Indexed {len(documents)} documents")
    return db

def search(db, query, k=3):
    results = db.similarity_search(query, k=k)
    print(f"\nResults for: {query}")
    for i, doc in enumerate(results):
        print(f"\n{i+1}. {doc.metadata.get('name', 'Unknown')}")
        print(f"   {doc.page_content[:200]}...")

# Note: Set up Google Drive API credentials first
# Download credentials.json from Google Cloud Console
# Then uncomment and run:
# service = authenticate_google()
# files = fetch_docs(service)
# print(f"Found {len(files)} Google Docs")
print("Setup Google Drive API credentials to use this feature.")
print("Guide: https://developers.google.com/drive/api/quickstart/python")
''',

"03_advanced/q10_ml_pipeline.py": '''
# Q10: Complete ML Pipeline
# Task: Build end-to-end ML pipeline: collect -> clean -> train -> evaluate -> Flask API
# Steps: data loading, preprocessing, training, evaluation, API deployment
# Deploy: https://render.com (free tier)
# Install: pip install scikit-learn pandas flask gunicorn

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from flask import Flask, request, jsonify

# Step 1: Load data
print("Step 1: Loading data...")
df = pd.read_csv("students_performance.csv")

# Step 2: Clean and preprocess
print("Step 2: Preprocessing...")
df["result"] = df["math score"].apply(lambda x: 1 if x >= 40 else 0)
le = LabelEncoder()
for col in ["gender", "race/ethnicity", "parental level of education",
            "lunch", "test preparation course"]:
    df[col] = le.fit_transform(df[col])

X = df.drop(["math score", "reading score", "writing score", "result"], axis=1)
y = df["result"]

# Step 3: Train
print("Step 3: Training model...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 4: Evaluate
print("Step 4: Evaluating...")
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred))

# Step 5: Save model
print("Step 5: Saving model...")
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)
print("Model saved as model.pkl")

# Step 6: Flask API
print("Step 6: Starting Flask API...")
app = Flask(__name__)

with open("model.pkl", "rb") as f:
    loaded_model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    loaded_scaler = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = pd.DataFrame([data])
    scaled = loaded_scaler.transform(features)
    prediction = loaded_model.predict(scaled)[0]
    result = "Pass" if prediction == 1 else "Fail"
    return jsonify({"prediction": result})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"})

if __name__ == "__main__":
    app.run(debug=True)

# To deploy on Render:
# 1. Add requirements.txt: pip freeze > requirements.txt
# 2. Add Procfile: web: gunicorn q10_ml_pipeline:app
# 3. Push to GitHub
# 4. Connect repo on render.com
'''
}

for filepath, content in files.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content.strip())
    print(f"Updated: {filepath}")

print("\nAll advanced files ready! Q1-Q10 complete.")

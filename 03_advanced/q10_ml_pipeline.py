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
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
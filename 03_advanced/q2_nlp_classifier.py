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
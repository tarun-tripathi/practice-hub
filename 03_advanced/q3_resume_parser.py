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
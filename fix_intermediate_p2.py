import os

files = {
"02_intermediate/q6_flask_api.py": '''
# Q6: Flask REST API
# Task: Build a REST API with endpoints to add and get students
# Framework: Flask (pip install flask)
# Endpoints:
#   POST /students     -> add a student
#   GET  /students     -> get all students
#   GET  /students/<id> -> get one student

from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}
counter = 1

@app.route("/students", methods=["POST"])
def add_student():
    global counter
    data = request.get_json()
    students[counter] = {
        "id": counter,
        "name": data["name"],
        "branch": data["branch"],
        "marks": data["marks"]
    }
    counter += 1
    return jsonify({"message": "Student added", "id": counter - 1}), 201

@app.route("/students", methods=["GET"])
def get_all_students():
    return jsonify(list(students.values())), 200

@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student = students.get(id)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

# To test:
# Run: python3 q6_flask_api.py
# POST: curl -X POST http://127.0.0.1:5000/students -H "Content-Type: application/json" -d "{\"name\":\"Tarun\",\"branch\":\"CSE\",\"marks\":95}"
# GET all: curl http://127.0.0.1:5000/students
# GET one: curl http://127.0.0.1:5000/students/1
''',

"02_intermediate/q7_currency_converter.py": '''
# Q7: Currency Converter
# Task: Convert currency using live exchange rates from ExchangeRate-API
# API: https://www.exchangerate-api.com (1500 free requests/month)
# Sign up to get free API key

import requests

API_KEY = "your_api_key_here"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest"

def get_rates(base_currency):
    response = requests.get(f"{BASE_URL}/{base_currency}")
    if response.status_code == 200:
        return response.json()["conversion_rates"]
    else:
        print(f"Error: {response.status_code}")
        return None

def convert(amount, from_currency, to_currency):
    rates = get_rates(from_currency)
    if rates and to_currency in rates:
        result = amount * rates[to_currency]
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        return result
    else:
        print(f"Currency {to_currency} not found.")
        return None

# Test
convert(100, "USD", "INR")
convert(500, "INR", "USD")
convert(100, "USD", "EUR")
''',

"02_intermediate/q8a_numpy_circuit.py": '''
# Q8a: NumPy Matrix Operations and Circuit Solver
# Task: Perform matrix operations and solve an electrical circuit using Ohm's law
# Concept: V = IR, solve system of equations using numpy.linalg.solve
# Docs: https://numpy.org/doc/stable/reference/routines.linalg.html

import numpy as np

print("=== Matrix Operations ===")

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nA + B:")
print(A + B)
print("\nA * B (element-wise):")
print(A * B)
print("\nA dot B (matrix multiply):")
print(np.dot(A, B))
print("\nTranspose of A:")
print(A.T)

print("\n=== Circuit Solver (Ohm's Law) ===")
# Two loop circuit:
# Loop 1: R1*I1 + R2*(I1-I2) = V1
# Loop 2: R2*(I2-I1) + R3*I2 = V2
# Rearranged:
# (R1+R2)*I1 - R2*I2 = V1
# -R2*I1 + (R2+R3)*I2 = V2

R1, R2, R3 = 5, 10, 15
V1, V2 = 20, 10

R = np.array([[R1 + R2, -R2],
              [-R2, R2 + R3]])
V = np.array([V1, V2])

I = np.linalg.solve(R, V)
print(f"R1={R1}, R2={R2}, R3={R3}")
print(f"V1={V1}V, V2={V2}V")
print(f"Current I1 = {I[0]:.4f} A")
print(f"Current I2 = {I[1]:.4f} A")
''',

"02_intermediate/q8b_pandas_cleaning.py": '''
# Q8b: Pandas Data Cleaning
# Task: Clean a messy real-world dataset
# Operations: handle nulls, remove duplicates, fix data types, strip junk strings
# This is similar to the Motherson project data cleaning work

import pandas as pd
import numpy as np

# Create a messy sample dataset
data = {
    "name":   ["Tarun", "Raj", None, "Priya", "Raj", "  Amit  ", "Sneha"],
    "age":    [21, 22, 23, None, 22, 25, "N/A"],
    "marks":  [95, 78, 88, 65, 78, None, 92],
    "branch": ["CSE", "IT", "CSE", "ECE", "IT", "cse", "  IT  "]
}

df = pd.DataFrame(data)

print("=== Original Messy Data ===")
print(df)
print(f"\nNull values:\n{df.isnull().sum()}")
print(f"\nDuplicates: {df.duplicated().sum()}")

# Step 1: Strip whitespace from strings
df["name"] = df["name"].str.strip()
df["branch"] = df["branch"].str.strip().str.upper()

# Step 2: Replace invalid values with NaN
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# Step 3: Fill nulls
df["name"].fillna("Unknown", inplace=True)
df["marks"].fillna(df["marks"].mean(), inplace=True)
df["age"].fillna(df["age"].median(), inplace=True)

# Step 4: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 5: Fix data types
df["age"] = df["age"].astype(int)
df["marks"] = df["marks"].round(2)

print("\n=== Cleaned Data ===")
print(df)
print(f"\nNull values after cleaning:\n{df.isnull().sum()}")
print(f"Duplicates after cleaning: {df.duplicated().sum()}")

df.to_csv("cleaned_data.csv", index=False)
print("\nSaved cleaned data to cleaned_data.csv")
''',

"02_intermediate/q10_file_downloader.py": '''
# Q10: Multi-threaded File Downloader
# Task: Download multiple files in parallel using threads
# Concept: concurrent.futures.ThreadPoolExecutor
# Docs: https://docs.python.org/3/library/concurrent.futures.html

import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Sample files to download (public domain images)
FILES = [
    ("https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table-word.jpg", "file1.jpg"),
    ("https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table-word.jpg", "file2.jpg"),
    ("https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table-word.jpg", "file3.jpg"),
    ("https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table-word.jpg", "file4.jpg"),
    ("https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table-word.jpg", "file5.jpg"),
]

os.makedirs("downloads", exist_ok=True)

def download_file(url, filename):
    try:
        response = requests.get(url, timeout=10)
        filepath = os.path.join("downloads", filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename} ({len(response.content)} bytes)")
        return filename
    except Exception as e:
        print(f"Failed: {filename} - {e}")
        return None

print("=== Single-threaded Download ===")
start = time.time()
for url, filename in FILES:
    download_file(url, f"single_{filename}")
print(f"Time taken: {time.time() - start:.2f}s")

print("\n=== Multi-threaded Download ===")
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {
        executor.submit(download_file, url, f"multi_{filename}"): filename
        for url, filename in FILES
    }
    for future in as_completed(futures):
        future.result()
print(f"Time taken: {time.time() - start:.2f}s")

print("\nAll files saved in downloads/ folder")
'''
}

for filepath, content in files.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content.strip())
    print(f"Updated: {filepath}")

print("\nPart 2 complete! Q6-Q10 files ready.")
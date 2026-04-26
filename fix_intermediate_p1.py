import os

files = {
"02_intermediate/q1_pandas_dashboard.py": '''
# Q1: Pandas Student Marks Dashboard
# Task: Analyze a student marks dataset using pandas
# Find top 5 students, failing students, average per subject, plot bar chart
# Dataset: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students_performance.csv")

print("=== Dataset Info ===")
print(df.head())
print(f"Shape: {df.shape}")

print("\n=== Top 5 Students by Math Score ===")
top5 = df.nlargest(5, "math score")[["math score", "reading score", "writing score"]]
print(top5)

print("\n=== Failing Students (Math < 40) ===")
failing = df[df["math score"] < 40]
print(f"Total failing: {len(failing)}")
print(failing[["math score", "reading score", "writing score"]])

print("\n=== Average Per Subject ===")
avg = df[["math score", "reading score", "writing score"]].mean()
print(avg)

# Bar chart
avg.plot(kind="bar", color=["steelblue", "orange", "green"])
plt.title("Average Score Per Subject")
plt.ylabel("Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("avg_scores.png")
print("\nChart saved as avg_scores.png")
''',

"02_intermediate/q2_weather_app.py": '''
# Q2: Live Weather App
# Task: Fetch live weather data using OpenWeatherMap API for any city
# API Docs: https://openweathermap.org/api
# Sign up at openweathermap.org to get a free API key

import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"\nCity: {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']} C")
        print(f"Feels Like: {data['main']['feels_like']} C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print(f"Error: {response.status_code} - City not found")

city = input("Enter city name: ")
get_weather(city)
''',

"02_intermediate/q3_sqlite_system.py": '''
# Q3: SQLite Student Registration System
# Task: Build a student registration system with full CRUD operations
# Database: SQLite (built-in Python, no install needed)
# Table: students(id, name, roll, branch, marks)

import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll TEXT UNIQUE NOT NULL,
        branch TEXT NOT NULL,
        marks REAL NOT NULL
    )
""")
conn.commit()

def add_student(name, roll, branch, marks):
    try:
        cursor.execute(
            "INSERT INTO students (name, roll, branch, marks) VALUES (?, ?, ?, ?)",
            (name, roll, branch, marks)
        )
        conn.commit()
        print(f"Added: {name}")
    except sqlite3.IntegrityError:
        print(f"Roll {roll} already exists.")

def get_all_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\nAll Students:")
    for s in students:
        print(s)

def search_student(roll):
    cursor.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    student = cursor.fetchone()
    if student:
        print(f"Found: {student}")
    else:
        print("Student not found.")

def update_marks(roll, marks):
    cursor.execute("UPDATE students SET marks = ? WHERE roll = ?", (marks, roll))
    conn.commit()
    print(f"Marks updated for roll {roll}")

def delete_student(roll):
    cursor.execute("DELETE FROM students WHERE roll = ?", (roll,))
    conn.commit()
    print(f"Deleted roll {roll}")

# Test
add_student("Tarun", "CS101", "CSE", 92)
add_student("Raj", "CS102", "CSE", 78)
add_student("Priya", "CS103", "IT", 88)
get_all_students()
search_student("CS101")
update_marks("CS101", 95)
search_student("CS101")
delete_student("CS102")
get_all_students()

conn.close()
''',

"02_intermediate/q4_job_scraper.py": '''
# Q4: Job Listings Scraper
# Task: Scrape job listings from a website and save to CSV
# Tools: BeautifulSoup + requests
# Target: TimesJobs (https://www.timesjobs.com)
# Note: Always check robots.txt before scraping any website

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_jobs(keyword="python"):
    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keyword}&txtLocation="

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    job_cards = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for card in job_cards[:10]:
        try:
            title = card.find("h2").text.strip()
            company = card.find("h3", class_="joblist-comp-name").text.strip()
            skills = card.find("span", class_="srp-skills").text.strip()
            posted = card.find("span", class_="sim-posted").text.strip()
            jobs.append({
                "title": title,
                "company": company,
                "skills": skills,
                "posted": posted
            })
            print(f"Title: {title}")
            print(f"Company: {company}")
            print(f"Skills: {skills}")
            print(f"Posted: {posted}")
            print("-" * 40)
        except AttributeError:
            continue

    # Save to CSV
    with open("jobs.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "company", "skills", "posted"])
        writer.writeheader()
        writer.writerows(jobs)

    print(f"\nSaved {len(jobs)} jobs to jobs.csv")

scrape_jobs("python developer")
''',

"02_intermediate/q5_data_viz.py": '''
# Q5: Data Visualization Dashboard
# Task: Create multiple chart types using matplotlib and seaborn
# Charts: heatmap, pie chart, line graph
# Dataset: Titanic from Kaggle (https://www.kaggle.com/c/titanic/data)
# Install: pip install seaborn matplotlib pandas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (download titanic.csv from Kaggle)
df = pd.read_csv("titanic.csv")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Titanic Dataset Dashboard", fontsize=16)

# 1. Survival count bar chart
df["Survived"].value_counts().plot(
    kind="bar", ax=axes[0, 0], color=["steelblue", "orange"]
)
axes[0, 0].set_title("Survival Count")
axes[0, 0].set_xticklabels(["Died", "Survived"], rotation=0)

# 2. Passenger class pie chart
df["Pclass"].value_counts().plot(
    kind="pie", ax=axes[0, 1], autopct="%1.1f%%",
    labels=["Class 3", "Class 1", "Class 2"]
)
axes[0, 1].set_title("Passenger Class Distribution")

# 3. Age distribution line graph
df["Age"].dropna().sort_values().reset_index(drop=True).plot(
    ax=axes[1, 0], color="green"
)
axes[1, 0].set_title("Age Distribution")
axes[1, 0].set_xlabel("Passenger Index")
axes[1, 0].set_ylabel("Age")

# 4. Correlation heatmap
numeric_df = df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]].dropna()
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", ax=axes[1, 1], cmap="coolwarm")
axes[1, 1].set_title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("titanic_dashboard.png")
print("Dashboard saved as titanic_dashboard.png")
'''
}

for filepath, content in files.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content.strip())
    print(f"Updated: {filepath}")

print("\nPart 1 complete! Q1-Q5 files ready.")
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

print("
=== Top 5 Students by Math Score ===")
top5 = df.nlargest(5, "math score")[["math score", "reading score", "writing score"]]
print(top5)

print("
=== Failing Students (Math < 40) ===")
failing = df[df["math score"] < 40]
print(f"Total failing: {len(failing)}")
print(failing[["math score", "reading score", "writing score"]])

print("
=== Average Per Subject ===")
avg = df[["math score", "reading score", "writing score"]].mean()
print(avg)

# Bar chart
avg.plot(kind="bar", color=["steelblue", "orange", "green"])
plt.title("Average Score Per Subject")
plt.ylabel("Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("avg_scores.png")
print("
Chart saved as avg_scores.png")
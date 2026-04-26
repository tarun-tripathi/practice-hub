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
print(f"
Null values:
{df.isnull().sum()}")
print(f"
Duplicates: {df.duplicated().sum()}")

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

print("
=== Cleaned Data ===")
print(df)
print(f"
Null values after cleaning:
{df.isnull().sum()}")
print(f"Duplicates after cleaning: {df.duplicated().sum()}")

df.to_csv("cleaned_data.csv", index=False)
print("
Saved cleaned data to cleaned_data.csv")
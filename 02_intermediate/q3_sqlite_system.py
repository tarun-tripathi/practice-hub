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
    print("
All Students:")
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
# Q4: CSV Student Sorter
# Task: Read a CSV file of students, sort by marks (highest first), save to new CSV
# Concepts: csv module, file I/O, sorting with lambda

import csv

def sort_students_by_marks(input_file, output_file):
    students = []

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append(row)

    students.sort(key=lambda x: int(x["marks"]), reverse=True)

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "marks"])
        writer.writeheader()
        writer.writerows(students)

    print("Sorted Results:")
    for s in students:
        print(f"{s['name']}: {s['marks']}")

sort_students_by_marks("students.csv", "students_sorted.csv")
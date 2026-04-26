# Q4 - CSV Student Sorter
import csv

def sort_students_by_marks(input_file, output_file):
    students = []
    
    # Read CSV
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append(row)
    
    # Sort by marks (highest first)
    students.sort(key=lambda x: int(x['marks']), reverse=True)
    
    # Write to new CSV
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'marks'])
        writer.writeheader()
        writer.writerows(students)
    
    print("Sorted Results:")
    for s in students:
        print(f"{s['name']}: {s['marks']}")

# Test
sort_students_by_marks('students.csv', 'students_sorted.csv')
# Q2 - Student Record System
students = {}

def add_student(roll, name, marks):
    students[roll] = {"name": name, "marks": marks}
    print(f"Student {name} added!")

def update_student(roll, name=None, marks=None):
    if roll in students:
        if name: students[roll]["name"] = name
        if marks: students[roll]["marks"] = marks
        print(f"Roll {roll} updated!")
    else:
        print("Student not found!")

def delete_student(roll):
    if roll in students:
        del students[roll]
        print(f"Roll {roll} deleted!")
    else:
        print("Student not found!")

def search_student(roll):
    if roll in students:
        print(f"Found: {students[roll]}")
    else:
        print("Student not found!")

# Test
add_student(101, "Tarun", 95)
add_student(102, "Raj", 78)
search_student(101)
update_student(101, marks=99)
search_student(101)
delete_student(102)
search_student(102)

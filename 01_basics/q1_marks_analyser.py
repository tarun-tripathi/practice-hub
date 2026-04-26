def analyse_marks(marks):
    avg = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    results = ["Pass" if m >= 40 else "Fail" for m in marks]
    return avg, highest, lowest, results

# Test
marks = [45, 78, 32, 90, 55]
print(analyse_marks(marks))

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


# Q3 - Calculator Class
from collections import deque

class Calculator:
    def __init__(self):
        self.history = deque(maxlen=5)  # last 5 operations only

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def sub(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def mul(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def div(self, a, b):
        if b == 0:
            print("Error: Division by zero!")
            return None
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def show_history(self):
        print("\n--- Last 5 Operations ---")
        for h in self.history:
            print(h)

# Test
calc = Calculator()
print(calc.add(10, 5))
print(calc.sub(20, 8))
print(calc.mul(4, 6))
print(calc.div(15, 3))
print(calc.div(10, 0))
calc.show_history()
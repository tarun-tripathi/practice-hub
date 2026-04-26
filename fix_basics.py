import os

files = {
"01_basics/q1_marks_analyser.py": '''
# Q1: Student Marks Analyser
# Task: Take a list of student marks and return average, highest, lowest, pass/fail status
# Pass criteria: marks >= 40

def analyse_marks(marks):
    avg = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    results = ["Pass" if m >= 40 else "Fail" for m in marks]
    return avg, highest, lowest, results

marks = [45, 78, 32, 90, 55]
avg, highest, lowest, results = analyse_marks(marks)
print(f"Average: {avg}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Results: {results}")
''',

"01_basics/q2_student_record.py": '''
# Q2: Student Record System
# Task: Build a dictionary based system with add, update, delete, search operations
# Key = roll number, Value = student details

students = {}

def add_student(roll, name, marks):
    students[roll] = {"name": name, "marks": marks}
    print(f"Student {name} added.")

def update_student(roll, name=None, marks=None):
    if roll in students:
        if name: students[roll]["name"] = name
        if marks: students[roll]["marks"] = marks
        print(f"Roll {roll} updated.")
    else:
        print("Student not found.")

def delete_student(roll):
    if roll in students:
        del students[roll]
        print(f"Roll {roll} deleted.")
    else:
        print("Student not found.")

def search_student(roll):
    if roll in students:
        print(f"Found: {students[roll]}")
    else:
        print("Student not found.")

add_student(101, "Tarun", 95)
add_student(102, "Raj", 78)
search_student(101)
update_student(101, marks=99)
search_student(101)
delete_student(102)
search_student(102)
''',

"01_basics/q3_calculator.py": '''
# Q3: Calculator Class
# Task: Build a Calculator class with add, sub, mul, div operations
# Extra: Store history of last 5 operations using deque

from collections import deque

class Calculator:
    def __init__(self):
        self.history = deque(maxlen=5)

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
            print("Error: Division by zero")
            return None
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def show_history(self):
        print("Last 5 Operations:")
        for h in self.history:
            print(h)

calc = Calculator()
print(calc.add(10, 5))
print(calc.sub(20, 8))
print(calc.mul(4, 6))
print(calc.div(15, 3))
print(calc.div(10, 0))
calc.show_history()
''',

"01_basics/q4_csv_sorter.py": '''
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
''',

"01_basics/q5_bank_account.py": '''
# Q5: BankAccount Class
# Task: Create a BankAccount class with deposit, withdraw, balance check
# Extra: Raise custom InsufficientFundsError when balance is not enough

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}. Available balance: {self.balance}"
            )
        self.balance -= amount
        print(f"Withdrew {amount}. Balance: {self.balance}")

    def check_balance(self):
        print(f"{self.owner} Balance: {self.balance}")

acc = BankAccount("Tarun", 1000)
acc.check_balance()
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()

try:
    acc.withdraw(5000)
except InsufficientFundsError as e:
    print(e)
''',

"01_basics/q6_file_logger.py": '''
# Q6: File Logger System
# Task: Create a logger that saves errors, warnings, and info with timestamps to a .log file
# Concepts: logging module, exception handling

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def divide(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"Division by zero: {a} / {b}")
        print("Error: Division by zero")
        return None

def login(username, password):
    if password == "tarun123":
        logging.info(f"User '{username}' logged in successfully")
        print(f"Welcome {username}")
    else:
        logging.warning(f"Failed login for '{username}'")
        print(f"Wrong password for {username}")

divide(10, 2)
divide(5, 0)
login("Tarun", "tarun123")
login("Tarun", "wrongpass")
print("Check app.log for logs")
''',

"01_basics/q7_guessing_game.py": '''
# Q7: Number Guessing Game
# Task: Build a guessing game with 3 difficulty levels
# Easy: 1-50, 10 tries | Medium: 1-100, 7 tries | Hard: 1-200, 5 tries
# Extra: Track score across rounds

import random

def play_game(difficulty):
    levels = {
        "easy": (1, 50, 10),
        "medium": (1, 100, 7),
        "hard": (1, 200, 5)
    }

    low, high, tries = levels[difficulty]
    number = random.randint(low, high)

    print(f"{difficulty.upper()} mode | Range: {low}-{high} | Tries: {tries}")

    for attempt in range(1, tries + 1):
        guess = int(input(f"Attempt {attempt}/{tries}: "))

        if guess == number:
            score = tries - attempt + 1
            print(f"Correct! Score: {score}")
            return score
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Game over. Number was {number}")
    return 0

total_score = 0
while True:
    diff = input("Choose difficulty (easy/medium/hard) or quit: ").lower()
    if diff == "quit":
        print(f"Final Score: {total_score}")
        break
    if diff in ["easy", "medium", "hard"]:
        total_score += play_game(diff)
    else:
        print("Invalid choice.")
''',

"01_basics/q8_contact_book.py": '''
# Q8: Contact Book
# Task: Build a contact book that saves and reads from a JSON file
# Operations: add, view, search, delete contacts

import json
import os

FILE = "contacts.json"

def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"{name} added.")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"{name} | {info['phone']} | {info['email']}")

def search_contact(name):
    contacts = load_contacts()
    if name in contacts:
        print(f"Found: {name} -> {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(name):
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name} deleted.")
    else:
        print("Contact not found.")

add_contact("Tarun", "9999999999", "tarun@email.com")
add_contact("Raj", "8888888888", "raj@email.com")
view_contacts()
search_contact("Tarun")
delete_contact("Raj")
view_contacts()
''',

"01_basics/q9_password_generator.py": '''
# Q9: Password Generator
# Task: Create a PasswordGenerator class with options for length,
# uppercase, lowercase, digits, and symbols
# Use secrets module instead of random for cryptographic safety

import secrets
import string

class PasswordGenerator:
    def __init__(self, length=12, uppercase=True, lowercase=True,
                 digits=True, symbols=True):
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.digits = digits
        self.symbols = symbols

    def generate(self):
        chars = ""
        if self.uppercase: chars += string.ascii_uppercase
        if self.lowercase: chars += string.ascii_lowercase
        if self.digits:    chars += string.digits
        if self.symbols:   chars += string.punctuation

        if not chars:
            print("Enable at least one character type.")
            return None

        password = "".join(secrets.choice(chars) for _ in range(self.length))
        print(f"Password: {password}")
        return password

gen1 = PasswordGenerator(length=8)
gen1.generate()

gen2 = PasswordGenerator(length=16, symbols=False)
gen2.generate()

gen3 = PasswordGenerator(length=20)
gen3.generate()
''',

"01_basics/q10_todo_app.py": '''
# Q10: TODO App
# Task: Build a TODO app using OOP with add, delete, mark complete operations
# Extra: Save and load tasks from a JSON file so data persists

import json
import os

FILE = "todos.json"

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

class TodoManager:
    def __init__(self):
        self.tasks = []
        self.load_from_json()

    def add(self, title):
        id = len(self.tasks) + 1
        task = Task(id, title)
        self.tasks.append(task)
        self.save_to_json()
        print(f"Added: {title}")

    def delete(self, id):
        task = self._find(id)
        if task:
            self.tasks.remove(task)
            self.save_to_json()
            print(f"Deleted task {id}")
        else:
            print("Task not found.")

    def mark_complete(self, id):
        task = self._find(id)
        if task:
            task.completed = True
            self.save_to_json()
            print(f"Task {id} marked complete.")
        else:
            print("Task not found.")

    def view(self):
        if not self.tasks:
            print("No tasks.")
            return
        print("TODO List:")
        for t in self.tasks:
            status = "[Done]" if t.completed else "[    ]"
            print(f"{status} {t.id}. {t.title}")

    def _find(self, id):
        for t in self.tasks:
            if t.id == id:
                return t
        return None

    def save_to_json(self):
        with open(FILE, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def load_from_json(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**t) for t in data]

todo = TodoManager()
todo.add("Complete Q10")
todo.add("Push to GitHub")
todo.add("Start Intermediate")
todo.view()
todo.mark_complete(1)
todo.delete(2)
todo.view()
'''
}

for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content.strip())
    print(f"Updated: {filepath}")

print("\nAll files updated successfully!")
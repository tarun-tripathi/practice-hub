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
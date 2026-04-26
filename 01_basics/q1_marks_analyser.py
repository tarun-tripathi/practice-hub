def analyse_marks(marks):
    avg = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    results = ["Pass" if m >= 40 else "Fail" for m in marks]
    return avg, highest, lowest, results

# Test
marks = [45, 78, 32, 90, 55]
print(analyse_marks(marks))



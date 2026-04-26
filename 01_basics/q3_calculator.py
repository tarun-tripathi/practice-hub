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
# Q6 - File Logger System
import logging
from datetime import datetime

# Logger setup
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def divide(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"Division by zero attempted: {a} / {b}")
        print("❌ Error: Division by zero!")
        return None

def login(username, password):
    if password == "tarun123":
        logging.info(f"User '{username}' logged in successfully")
        print(f"✅ Welcome {username}!")
    else:
        logging.warning(f"Failed login attempt for user '{username}'")
        print(f"❌ Wrong password for {username}!")

# Test
print("Running tests...\n")
divide(10, 2)
divide(5, 0)
login("Tarun", "tarun123")
login("Tarun", "wrongpass")

print("\n✅ Check app.log file for logs!")

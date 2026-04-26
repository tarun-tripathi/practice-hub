# Q5 - BankAccount Class
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        self.balance += amount
        print(f"✅ Deposited ₹{amount} | Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        if amount > self.balance:
            raise InsufficientFundsError(
                f"❌ Cannot withdraw ₹{amount}! Available: ₹{self.balance}"
            )
        self.balance -= amount
        print(f"✅ Withdrew ₹{amount} | Balance: ₹{self.balance}")

    def check_balance(self):
        print(f"💰 {self.owner}'s Balance: ₹{self.balance}")

# Test
acc = BankAccount("Tarun", 1000)
acc.check_balance()
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()

try:
    acc.withdraw(5000)
except InsufficientFundsError as e:
    print(e)
# Q9 - Password Generator
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
            print("❌ Enable at least one character type!")
            return None

        password = ''.join(secrets.choice(chars) for _ in range(self.length))
        print(f"🔐 Generated Password: {password}")
        return password

# Test
print("=== Password Generator ===\n")

gen1 = PasswordGenerator(length=8)
gen1.generate()

gen2 = PasswordGenerator(length=16, symbols=False)
gen2.generate()

gen3 = PasswordGenerator(length=20, uppercase=True, 
                          lowercase=True, digits=True, symbols=True)
gen3.generate()
# Q8 - Contact Book
import json
import os

FILE = "contacts.json"

def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"✅ {name} added!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📭 No contacts found!")
        return
    print("\n📒 All Contacts:")
    for name, info in contacts.items():
        print(f"👤 {name} | 📞 {info['phone']} | ✉️ {info['email']}")

def search_contact(name):
    contacts = load_contacts()
    if name in contacts:
        print(f"Found: {name} → {contacts[name]}")
    else:
        print("❌ Contact not found!")

def delete_contact(name):
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️ {name} deleted!")
    else:
        print("❌ Contact not found!")

# Test
add_contact("Tarun", "9999999999", "tarun@email.com")
add_contact("Raj", "8888888888", "raj@email.com")
view_contacts()
search_contact("Tarun")
delete_contact("Raj")
view_contacts()
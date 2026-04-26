# Q10 - TODO App
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
        print(f"✅ Added: '{title}'")

    def delete(self, id):
        task = self._find(id)
        if task:
            self.tasks.remove(task)
            self.save_to_json()
            print(f"🗑️ Deleted task {id}")
        else:
            print("❌ Task not found!")

    def mark_complete(self, id):
        task = self._find(id)
        if task:
            task.completed = True
            self.save_to_json()
            print(f"🎉 Task {id} marked complete!")
        else:
            print("❌ Task not found!")

    def view(self):
        if not self.tasks:
            print("📭 No tasks!")
            return
        print("\n📋 TODO List:")
        for t in self.tasks:
            status = "✅" if t.completed else "⬜"
            print(f"{status} [{t.id}] {t.title}")

    def _find(self, id):
        for t in self.tasks:
            if t.id == id:
                return t
        return None

    def save_to_json(self):
        with open(FILE, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def load_from_json(self):
        if os.path.exists(FILE):
            with open(FILE, 'r') as f:
                data = json.load(f)
                self.tasks = [Task(**t) for t in data]

# Test
todo = TodoManager()
todo.add("Complete Q10")
todo.add("Push to GitHub")
todo.add("Start Q Intermediate")
todo.view()
todo.mark_complete(1)
todo.delete(2)
todo.view()
# Q6: Flask REST API
# Task: Build a REST API with endpoints to add and get students
# Framework: Flask (pip install flask)
# Endpoints:
#   POST /students     -> add a student
#   GET  /students     -> get all students
#   GET  /students/<id> -> get one student

from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}
counter = 1

@app.route("/students", methods=["POST"])
def add_student():
    global counter
    data = request.get_json()
    students[counter] = {
        "id": counter,
        "name": data["name"],
        "branch": data["branch"],
        "marks": data["marks"]
    }
    counter += 1
    return jsonify({"message": "Student added", "id": counter - 1}), 201

@app.route("/students", methods=["GET"])
def get_all_students():
    return jsonify(list(students.values())), 200

@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student = students.get(id)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

# To test:
# Run: python3 q6_flask_api.py
# POST: curl -X POST http://127.0.0.1:5000/students -H "Content-Type: application/json" -d "{"name":"Tarun","branch":"CSE","marks":95}"
# GET all: curl http://127.0.0.1:5000/students
# GET one: curl http://127.0.0.1:5000/students/1
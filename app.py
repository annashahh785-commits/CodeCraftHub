
from flask import Flask, request, jsonify
import json
import os
from datetime import datetime, date

app = Flask(__name__)

# JSON file used for storing course information
DATA_FILE = "courses.json"

# Allowed course statuses
VALID_STATUSES = ["Not Started", "In Progress", "Completed"]


# -----------------------------
# CUSTOM ERROR HANDLER
# -----------------------------

@app.errorhandler(RuntimeError)
def handle_runtime_error(error):
    return jsonify({
        "error": str(error)
    }), 500


# -----------------------------
# FILE HANDLING FUNCTIONS
# -----------------------------

# Read courses from JSON file
def load_courses():
    try:
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w", encoding="utf-8") as file:
                json.dump([], file)
            return []

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            courses = json.load(file)

            if not isinstance(courses, list):
                raise RuntimeError("Invalid course data format")

            return courses

    except json.JSONDecodeError:
        raise RuntimeError("Course data file contains invalid JSON")

    except OSError:
        raise RuntimeError("Unable to read course data")


# Save courses into JSON file
def save_courses(courses):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(courses, file, indent=4)

    except OSError:
        raise RuntimeError("Unable to save course data")


# -----------------------------
# INPUT VALIDATION
# -----------------------------

def validate_course(data):

    if not isinstance(data, dict):
        return "Request body must be a JSON object"

    required_fields = [
        "course_name",
        "description",
        "target_completion_date",
        "status"
    ]

    for field in required_fields:
        if field not in data:
            return f"{field} is required"

        if not isinstance(data[field], str) or not data[field].strip():
            return f"{field} must be a non-empty string"

    if data["status"] not in VALID_STATUSES:
        return "Invalid course status"

    try:
        parsed_date = date.fromisoformat(
            data["target_completion_date"]
        )

        if parsed_date.isoformat() != data["target_completion_date"]:
            return "Date must be in YYYY-MM-DD format"

    except ValueError:
        return "Date must be in YYYY-MM-DD format"

    return None


# -----------------------------
# HOME ROUTE
# -----------------------------

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to CodeCraftHub API"
    }), 200


# -----------------------------
# GET ALL COURSES
# -----------------------------

@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = load_courses()

    return jsonify(courses), 200


# -----------------------------
# GET A SPECIFIC COURSE
# -----------------------------

@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    courses = load_courses()

    for course in courses:
        if course["id"] == course_id:
            return jsonify(course), 200

    return jsonify({
        "error": "Course not found"
    }), 404


# -----------------------------
# CREATE A COURSE
# -----------------------------

@app.route("/api/courses", methods=["POST"])
def create_course():
    data = request.get_json(silent=True)

    error = validate_course(data)

    if error:
        return jsonify({"error": error}), 400

    courses = load_courses()

    new_course = {
        "id": max(
            (course["id"] for course in courses),
            default=0
        ) + 1,

        "course_name": data["course_name"].strip(),
        "description": data["description"].strip(),
        "target_completion_date": data["target_completion_date"],
        "status": data["status"],
        "created_at": datetime.now().isoformat(timespec="seconds")
    }

    courses.append(new_course)

    save_courses(courses)

    return jsonify(new_course), 201


# -----------------------------
# UPDATE A COURSE
# -----------------------------

@app.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    data = request.get_json(silent=True)

    error = validate_course(data)

    if error:
        return jsonify({"error": error}), 400

    courses = load_courses()

    for course in courses:
        if course["id"] == course_id:

            course["course_name"] = data["course_name"].strip()
            course["description"] = data["description"].strip()
            course["target_completion_date"] = data["target_completion_date"]
            course["status"] = data["status"]

            save_courses(courses)

            return jsonify(course), 200

    return jsonify({
        "error": "Course not found"
    }), 404


# -----------------------------
# DELETE A COURSE
# -----------------------------

@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    courses = load_courses()

    for course in courses:
        if course["id"] == course_id:

            courses.remove(course)

            save_courses(courses)

            return jsonify({
                "message": "Course deleted successfully"
            }), 200

    return jsonify({
        "error": "Course not found"
    }), 404


# -----------------------------
# RUN FLASK APPLICATION
# -----------------------------

if __name__ == "__main__":
    print("CodeCraftHub API is starting...")
    app.run(debug=True)

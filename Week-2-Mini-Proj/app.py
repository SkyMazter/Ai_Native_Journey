from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})
"""Example Data"""
projects = [
    {
        "id": "proj-1", # Unique ID for the project
        "name": "Website Redesign",
        "tasks": ["Conduct user research", "Design new UI mockups", "Develop front-end"],
        "completion_percentage": 60
    },
    {
        "id": "proj-2",
        "name": "Mobile App Launch",
        "tasks": ["Define app features", "Create UI/UX wireframes", "Develop iOS version"],
        "completion_percentage": 25
    }
]

@app.route('/')
def home():
    return "Welcome to my app"


@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    Handles GET requests to /api/projects.
    Returns a JSON list of all projects.
    """
    # jsonify converts Python dictionaries/lists into JSON format.
    return jsonify(projects)

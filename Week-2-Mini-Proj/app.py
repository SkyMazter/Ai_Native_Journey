from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

# Example Data
projects = [
    {
        "id": 0, # Unique ID for the project
        "name": "Website Redesign",
        "tasks": ["Conduct user research", "Design new UI mockups", "Develop front-end"],
        "completion_percentage": 60
    },
    {
        "id": 1,
        "name": "Mobile App Launch",
        "tasks": ["Define app features", "Create UI/UX wireframes", "Develop iOS version"],
        "completion_percentage": 25
    },
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


@app.route('/api/projects/new', methods=["POST"])
def new_project():
    new_proj_data = request.json
    if not new_proj_data or 'name' not in new_proj_data:
        return "Invalid project data", 400
    # projects.append(new_proj_data)

    new_project = {
        "id": len(projects),
        "name": new_proj_data["name"],
        "tasks": new_proj_data.get("tasks", []),
        "completion_percentage": new_proj_data.get("completion_percentage", 0)
    }
    projects.append(new_project)
    return  jsonify(new_project), 201

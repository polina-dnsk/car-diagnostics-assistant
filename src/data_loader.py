import json


def load_car_problems(file_path):
    """Load car problem data from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)
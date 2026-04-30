import json


def load_data(file_location):
    with open(file_location, 'r') as f:
        data = json.load(f)
    return data
import json


def load_data(file_location):
    with open(file_location, 'r') as f:
        data = json.load(f)
    return data

#Saving data for order management
def save_data(file_location, data):
    with open(file_location, 'w') as f:
        json.dump(data, f, indent=4)
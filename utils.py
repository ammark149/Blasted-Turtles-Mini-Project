import json
import csv 

#Loading our json menu
def load_json(file_location):
    try:
        with open(file_location, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_location} not found.")
        return {}
    
#Reading files
def load_data(file_location):
    data = []
    try:
        with open(file_location,'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Sorry {file_location} not found.")
    return data

#Writing to files
def save_data(file_location, data_list):
    if not data_list:
        return
    column_headers = data_list[0].keys() #Headers for top row
    with open(file_location, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=column_headers)
        writer.writeheader()
        writer.writerows(data_list)

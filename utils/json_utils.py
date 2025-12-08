import json

# Dump a dictionary into a JSON file
def write_json(data, path: str):
    with open(path, 'w') as f: 
        json.dump(data, f, indent =2)

# Read a JSON file and load into a dictionary
def read_json(path: str): 
    with open(path, 'r') as f:
        data = json.load(f)
    return data   

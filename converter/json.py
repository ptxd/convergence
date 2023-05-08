import json
import numpy as np

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return np.array(data)

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data.tolist(), file, indent=4)

# Keep the existing read_json function


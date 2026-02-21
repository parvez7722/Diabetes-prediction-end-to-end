import json

def load_data():
    with open('src/data/patient_data.json', 'r') as f:
        data = json.load(f)
        return data

def save_data(data):
    with open('src/data/patient_data.json', 'w') as f:
        json.dump(data, f, indent=4)

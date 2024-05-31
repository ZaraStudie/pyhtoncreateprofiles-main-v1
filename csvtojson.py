import csv
import json

csv_file = 'profiles1.csv'
json_file = 'data.json'

def convert_csv_to_json(csv_file, json_file):
    data = []

  
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        print("Error reading CSV file:", e)

 
    try:
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print("Error writing JSON file:", e)

if __name__ == '__main__':
    convert_csv_to_json(csv_file, json_file)

import argparse
import json
import csv
import os

def read_csv(csv_path):
    data = {}
    with open(csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key, value in row.items():
                data[key] = value
    return data

def update_json(json_path, csv_data, env):
    with open(json_path, 'r') as file:
        json_data = json.load(file)
    
    if env in json_data:
        json_data[env].update(csv_data)
    else:
        print(f"Environment '{env}' not found in the JSON file.")

    with open(json_path, 'w') as file:
        json.dump(json_data, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Update JSON file based on CSV input.')
    parser.add_argument('--env', required=True, help='Environment to update in the JSON file.')
    parser.add_argument('--json', required=True, help='Path to the JSON file.')
    parser.add_argument('--csv', required=True, help='Path to the CSV file.')

    args = parser.parse_args()

    # Read CSV data
    csv_data = read_csv(args.csv)
    
    # Update JSON file
    update_json(args.json, csv_data, args.env)

if __name__ == '__main__':
    main()

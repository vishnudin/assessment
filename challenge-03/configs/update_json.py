import csv
import json
import argparse  
import os

def update_json_file(env, csv_data, json_file_path):
    # Load the existing JSON data
    try:
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        json_data = {}
    
    # Ensure the specific environment key exists in the JSON data
    if env not in json_data:
        json_data[env] = []
    
    # Update the specific environment section in the JSON data
    json_data[env] = csv_data
    
    # Write the updated JSON data back to the file
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Update JSON file with CSV data based on environment.')
    parser.add_argument('--env', required=True, help='Environment key to update in the JSON file.')
    parser.add_argument('--csv', required=True, help='Path to the CSV file.')
    parser.add_argument('--json', required=True, help='Path to the JSON file.')

    args = parser.parse_args()

    # Read CSV file into a list of dictionaries
    csv_file_path = args.csv
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        csv_data = list(reader)
    
    # Update the JSON file
    update_json_file(args.env, csv_data, args.json)
    print(f"JSON file '{args.json}' updated successfully for environment '{args.env}'.")

if __name__ == "__main__":
    main()

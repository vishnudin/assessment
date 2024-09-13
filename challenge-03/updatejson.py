import json
import csv
import argparse

def update_json(env, json_file, csv_file):
    # Load JSON data
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Load CSV data
    csv_data = {}
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Use the 'env' column in CSV to identify the relevant data to update
            if row['env'] == env:
                csv_data = row
                break

    # Update only the parts of JSON that match the ENV
    for key, value in csv_data.items():
        if key != 'env':  # Ignore the 'env' key itself
            json_data[key] = value

    # Write the updated JSON back to the file
    with open(json_file, 'w') as f:
        json.dump(json_data, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update JSON file based on ENV and CSV")
    
    # Command-line arguments for env, json, and csv file paths
    parser.add_argument('-env', required=True, help='Environment to update (e.g., DEV, PROD)')
    parser.add_argument('-json', required=True, help='Path to the JSON file')
    parser.add_argument('-csv', required=True, help='Path to the CSV file')
    
    args = parser.parse_args()
    
    # Call the function to update JSON
    update_json(args.env, args.json, args.csv)

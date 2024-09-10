import argparse
import json
import csv

def update_json(env, json_file, csv_file):
    # Load JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Load CSV data
    csv_data = {}
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_data[row['ENV']] = row

    # Update JSON data based on CSV data
    if env in csv_data:
        env_data = csv_data[env]
        for key in ['host', 'port', 'dbname', 'user', 'password']:
            if key in env_data:
                data[env][key] = env_data[key]

    # Save updated JSON data
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Update JSON file based on CSV data.')
    parser.add_argument('--env', required=True, help='Environment to update in JSON file.')
    parser.add_argument('--json', required=True, help='Path to the JSON file.')
    parser.add_argument('--csv', required=True, help='Path to the CSV file.')

    args = parser.parse_args()

    update_json(args.env, args.json, args.csv)

if __name__ == '__main__':
    main()
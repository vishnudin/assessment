import json
import csv
import argparse

# Function to read CSV file and return a dictionary with environment as the key
def read_csv(csv_file):
    csv_data = {}
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            env = row['ENV']
            csv_data[env] = {
                'host': row['host'],
                'port': int(row['port']),
                'dbname': row['dbname'],
                'user': row['user'],
                'password': row['password']
            }
    return csv_data

# Function to update the JSON file based on the environment and CSV data
def update_json(env, json_file, csv_data):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Update only the given environment
    if env in data:
        data[env].update(csv_data[env])
    else:
        print(f"Environment '{env}' not found in JSON.")
        return

    # Write the updated data back to the JSON file
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

# Main function to run the script
def main():
    parser = argparse.ArgumentParser(description="Update JSON file based on CSV input and environment.")
    parser.add_argument('--env', required=True, help='Environment to update (e.g., DEV, PROD)')
    parser.add_argument('--json', required=True, help='Path to the JSON file to update')
    parser.add_argument('--csv', required=True, help='Path to the CSV file to read data from')

    args = parser.parse_args()
    csv_data = read_csv(args.csv)  # Read data from CSV
    update_json(args.env, args.json, csv_data)  # Update the JSON file

if __name__ == "__main__":
    main()

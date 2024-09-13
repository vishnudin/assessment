import argparse
import json
import csv

def update_json(env, json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    updates = {}
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ENV'] == env:
               
                updates = {
                    'host': row['host'].strip('"'),
                    'port': int(row['port']),
                    'dbname': row['dbname'],
                    'user': row['user'],
                    'password': row['password']
                }
                break

    if env in data:
        data[env].update(updates)
    else:
        print(f"Environment '{env}' not found in JSON file.")
        return

    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', required=True)
    parser.add_argument('--json', required=True)
    parser.add_argument('--csv', required=True)

    args = parser.parse_args()
    update_json(args.env, args.json, args.csv)

if __name__ == "__main__":
    main()

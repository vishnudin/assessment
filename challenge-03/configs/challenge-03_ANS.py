import argparse
import json
import pandas as pd

def read_csv(file_path):
    """read the CSV file and return a dictionary of environment settings."""
    df = pd.read_csv(file_path)
    return df.set_index('ENV').to_dict(orient='index')

def update_json(file_path, env, settings):
    """update the JSON file with the settings for the specified environment."""
    with open(file_path, 'r') as json_file:
        config = json.load(json_file)

    # updating the JSON for the specified environment
    if env in config:
        config[env].update(settings[env])
    
    with open(file_path, 'w') as json_file:
        json.dump(config, json_file, indent=4)

def main():
    # setting up command-line arguments
    parser = argparse.ArgumentParser(description='Update JSON config from CSV file.')
    parser.add_argument('--env', required=True, help='Environment to update (e.g., DEV, PROD)')
    parser.add_argument('--json', required=True, help='Path to the JSON file')
    parser.add_argument('--csv', required=True, help='Path to the CSV file')
    
    args = parser.parse_args()

    # reading the settings from CSV and update the JSON file
    settings = read_csv(args.csv)
    update_json(args.json, args.env, settings)

if __name__ == '__main__':
    main()

# Challenge 03: Update JSON Based on CSV Data

This project provides a Python script to update a JSON configuration file based on data from a CSV file. The script allows you to specify an environment and update only the relevant part of the JSON file, leaving other elements untouched.

## Files Provided

- `updatejson.py`: The Python script for updating the JSON file.
- `configs/config.json`: The JSON file to be updated.
- `configs/input.csv`: The CSV file containing the update data.

## Prerequisites

- Python 3.x installed on your system.

## Instructions

1. Run the Script

    a. For DEV:
    ```bash
    python3 updatejson.py --env DEV --json ./configs/config.json --csv ./configs/input.csv
    ```

    b. For PROD:
    ```bash
    python3 updatejson.py --env PROD --json ./configs/config.json --csv ./configs/input.csv
    ```

2. Verify the update

    After running the script, open config.json to check if it has been updated correctly. The updated JSON file should reflect the changes from the CSV data only for the specified environment.
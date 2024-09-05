How to Run the Script

1.Navigate to the challenge-03 Directory:

cd challenge-03


2. Run the Python Script:

To update the DEV section of the JSON file based on input.csv, execute:

python3 updatejson.py --env DEV --json ./configs/config.json --csv ./configs/input.csv

To update the PROD section, change the --env argument:

python3 updatejson.py --env PROD --json ./configs/config.json --csv ./configs/input.csv



Summary

1.Script: "updatejson.py" reads data from input.csv and updates the specified section in "config.json".

2.Command: Use the CLI command python3 "updatejson.py" "--env ENV --json ./configs/config.json --csv" "./configs/input.csv" to run the script.

3.Example Files: Provide a sample "config.json" and "input.csv" to test the functionality.
import pandas as pd

def read_table(file_path, sheet_name):
    """
    Reads a table from an Excel file and returns it as a DataFrame.
    """
    return pd.read_excel(file_path, sheet_name=sheet_name)

def find_employees_without_devices(employee_df, device_df):
    """
    Identifies employees who do not have a recorded device.
    """
    # Replace these with the actual column names
    employee_id_column = 'id'  # Update based on your data
    device_id_column = 'employee_id'    # Update based on your data
    
    # Get a list of EmployeeIDs from the device DataFrame
    employees_with_devices = device_df[device_id_column].unique()
    
    # Identify employees without devices
    employees_without_devices = employee_df[~employee_df[employee_id_column].isin(employees_with_devices)]
    
    return employees_without_devices

def main():
    file_path = 'table_data.xlsx'  # Replace with the path to your XLSX file

    # Read the Employee and Device tables
    employee_df = read_table(file_path, 'Employees')
    device_df = read_table(file_path, 'Devices')
    
    # Debugging prints to check column names
    print("Employee DataFrame columns:", employee_df.columns)
    print("Device DataFrame columns:", device_df.columns)
    
    # Find employees without devices
    employees_without_devices = find_employees_without_devices(employee_df, device_df)
    
    # Output the names of employees without devices
    if not employees_without_devices.empty:
        print("Employees without recorded devices:")
        print(employees_without_devices[['first_name','last_name']])  # Adjust based on actual column names
    else:
        print("All employees have their devices recorded.")

if __name__ == "__main__":
    main()


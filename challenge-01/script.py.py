import pandas as pd

# Load the data from the Excel file
employee_data = pd.read_excel("table_data.xlsx", sheet_name="Employees")
device_data = pd.read_excel("table_data.xlsx", sheet_name="Devices")

# Merge the tables on 'Employee ID' to find employees without devices
merged_data = pd.merge(employee_data, device_data, how='left', on='employee_id')

# Filter the employees without a device record
employees_without_device = merged_data[merged_data['type'].isna()]

# Output the result
print("Employees without recorded devices:")
print(employees_without_device[['first_name', 'last_name']])

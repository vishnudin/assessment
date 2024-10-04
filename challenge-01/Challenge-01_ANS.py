import pandas as pd

# give the Excel file_path
file_path = r'D:\Users\NRethinasamy\Downloads\table_data.xlsx'
# reading the Employees and Devices sheets
employees_df = pd.read_excel(file_path, sheet_name='Employees')
devices_df = pd.read_excel(file_path, sheet_name='Devices')
# finding employees without a device
no_device_employees = employees_df[~employees_df['id'].isin(devices_df['employee_id'])]
# giving the output names of employees without a device record
print("Employees without a device record:")
for index, row in no_device_employees.iterrows():
    print(f"{row['first_name']} {row['last_name']}")

import pandas as pd

file_path = 'C:/Users/pgade/Desktop/table_data.xlsx'

employees_df = pd.read_excel(file_path, sheet_name='Employees')
devices_df = pd.read_excel(file_path, sheet_name='Devices')

employees_with_devices = devices_df['employee_id'].unique()

employees_without_devices = employees_df[~employees_df['id'].isin(employees_with_devices)]

print("Employees without company-issued devices:")
for index, row in employees_without_devices.iterrows():
    print(f"{row['first_name']} {row['last_name']}")

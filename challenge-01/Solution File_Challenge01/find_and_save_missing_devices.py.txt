import pandas as pd

file_path = 'table_data.xlsx'

employees_df = pd.read_excel(file_path, sheet_name='Employees')
devices_df = pd.read_excel(file_path, sheet_name='Devices')

merged_df = pd.merge(employees_df, devices_df, left_on='id', right_on='employee_id', how='left', indicator=True)

no_device_df = merged_df[merged_df['_merge'] == 'left_only']

no_device_df_output = no_device_df[['id', 'first_name', 'last_name', 'department', 'location', 'employee_type']]

output_file_path = 'employees_without_devices.xlsx'

no_device_df_output.to_excel(output_file_path, index=False)

print(f"The list of employees without a recorded device has been saved to {output_file_path}.")

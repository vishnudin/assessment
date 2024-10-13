import pandas as pd
sheet1_url = 'https://docs.google.com/spreadsheets/d/1xooGpzt6IyQMzLH676_Grzs3mzu0pXnp/export?format=csv&gid=1579824616'
sheet2_url = 'https://docs.google.com/spreadsheets/d/1xooGpzt6IyQMzLH676_Grzs3mzu0pXnp/export?format=csv&gid=438115826'
table1 = pd.read_csv(sheet1_url)
table2 = pd.read_csv(sheet2_url)
absent_employees = []
for index, row in table1.iterrows():
    adjusted_index = index + 1
    if row['id'] not in table2['employee_id'].values:
        absent_employees.append((adjusted_index, row['first_name'], row['last_name']))

absent_employees_df = pd.DataFrame(absent_employees, columns=['Id', 'First Name', 'Last Name'])
print(absent_employees_df)



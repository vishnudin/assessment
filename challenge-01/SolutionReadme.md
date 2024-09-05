Explanation

1.Load Excel File:

Load both the employees and devices sheets into Data Frames.

2.Merge Data Frames:

Merge the employee and device DataFrames as before, using id from "employees_df" and "employee_id" from "devices_df".

3.Filter Employees Without Devices:

Extract rows where "_merge" is "left_only" to find employees who do not have devices recorded.

4.Prepare Data for Output:

Select relevant columns from "no_device_df" for the output. Here, you retain only "employee-related columns".

5.Write to Excel:

Use "to_excel" to write the "no_device_df_output DataFrame" to a new Excel file named "employees_without_devices.xlsx".
The "index=False" argument ensures that row indices are not included in the output file.

6.Print Confirmation:

Inform the user where the output file has been saved.

7.Running the Script:

Save this script to a file, such as "find_and_save_missing_devices.py", and run it with:

python find_and_save_missing_devices.py

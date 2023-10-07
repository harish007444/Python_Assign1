import csv
from datetime import datetime, timedelta

csv_file_path = r"C:\Users\MicroApt\Desktop\Python_Assign\Assignment_Timecard.csv"

def parse_datetime(time_str):
    try:
        if time_str:
            return datetime.strptime(time_str, "%m/%d/%Y %I:%M %p")
        else:
            return None
    except ValueError:
        # Handle incorrectly formatted date/time values
        print(f"Error: Incorrectly formatted date/time - '{time_str}'")
        return None

def analyze_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            employee_name = row['Employee Name']
            position_id = row['Position ID']
            time_in = parse_datetime(row['Time'])
            time_out = parse_datetime(row['Time Out'])
            
            if time_in is not None and time_out is not None:
                if (time_out - time_in).days >= 7:
                    print(f"Employee Name: {employee_name}, Position ID: {position_id}, Worked for 7 consecutive days.")
                if 1 < (time_in - time_out).seconds // 3600 < 10:
                    print(f"Employee Name: {employee_name}, Position ID: {position_id}, Less than 10 hours between shifts.")
                if (time_out - time_in).seconds // 3600 > 14:
                    print(f"Employee Name: {employee_name}, Position ID: {position_id}, Worked more than 14 hours in a single shift.")
            else:
                print(f"Employee Name: {employee_name}, Position ID: {position_id}, Invalid time format.")

analyze_csv(csv_file_path)

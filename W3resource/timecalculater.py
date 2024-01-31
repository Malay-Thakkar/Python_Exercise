from datetime import datetime, timedelta

def count_office_hr():
    flag = 1
    office_hours_list = []

    company_hr = int(input("Enter total hours of the company: "))
    
    while flag == 1:
        start_time = input("Enter entry time (HH:MM:SS): ")
        end_time = input("Enter exit time (HH:MM:SS): ")
        office_hours_list.append({'start_time': start_time, 'end_time': end_time})
        flag = int(input("Enter 1 to continue entering times, 0 to exit: "))

    total_hr = sum_of_count(office_hours_list)
    return sub_time(company_hr, total_hr)

def sum_of_count(office_hours_list):
    total_hr = 0
    for entry in office_hours_list:
        start_datetime = datetime.strptime(entry['start_time'], "%H:%M:%S")
        end_datetime = datetime.strptime(entry['end_time'], "%H:%M:%S")
        total_hr += (end_datetime - start_datetime).total_seconds() / 3600
    return total_hr

def sub_time(company_hr, total_hr):
    return company_hr - total_hr

# Test the function
remaining_hr = count_office_hr()
print("Remaining office hours for the company:", round(remaining_hr, 2), "hours")

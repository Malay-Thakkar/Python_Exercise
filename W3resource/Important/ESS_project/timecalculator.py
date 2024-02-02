from datetime import datetime, timedelta

def count_office_hr():
    flag = 1
    office_hours_list = []

    # 1. Take total hours of the company as a time using timedelta
    company_hr = input("Enter total hours of the company (e.g., 9.3 for 9 hours and 30 minutes): ")
    company_hr = company_hr.split('.')
    company_hr = timedelta(hours=int(company_hr[0]), minutes=int(company_hr[1]))

    while flag == 1:
        # 2. Take input for start_time and end_time as (HH:MM)
        start_time = input("Enter entry time (HH:MM): ")
        end_time = input("Enter exit time (HH:MM): ")
        office_hours_list.append({'start_time': start_time, 'end_time': end_time})
        flag = int(input("Enter 1 to continue entering times, 0 to exit: "))

    total_hr = sum_of_count(office_hours_list)
    remaining_hr, break_time = sub_time(company_hr, total_hr)
    expected_exit_time = calculate_expected_exit_time(total_hr, break_time)
    return remaining_hr, break_time, expected_exit_time

def sum_of_count(office_hours_list):
    total_hr = timedelta()
    for entry in office_hours_list:
        start_time = entry['start_time'].split(':')
        end_time = entry['end_time'].split(':')
        start_datetime = datetime.now().replace(hour=int(start_time[0]), minute=int(start_time[1]), second=0, microsecond=0)
        end_datetime = datetime.now().replace(hour=int(end_time[0]), minute=int(end_time[1]), second=0, microsecond=0)
        total_hr += end_datetime - start_datetime
    return total_hr

def sub_time(company_hr, total_hr):
    remaining_hr = company_hr - total_hr
    return remaining_hr.days, remaining_hr.seconds // 3600

def calculate_break_time(office_hours_list):
    total_break_time = timedelta()
    for entry in office_hours_list:
        start_time = entry['start_time'].split(':')
        end_time = entry['end_time'].split(':')
        start_datetime = datetime.now().replace(hour=int(start_time[0]), minute=int(start_time[1]), second=0, microsecond=0)
        end_datetime = datetime.now().replace(hour=int(end_time[0]), minute=int(end_time[1]), second=0, microsecond=0)
        total_break_time += (start_datetime - end_datetime)
    return total_break_time.days, total_break_time.seconds // 3600

def calculate_expected_exit_time(total_hr, break_time):
    expected_exit_time = datetime.now() + total_hr + timedelta(hours=break_time)
    return expected_exit_time.strftime("%Y-%m-%d %H:%M")

# Test the function
remaining_hr, break_time, expected_exit_time = count_office_hr()
print("Remaining office hours for the company:", remaining_hr, "days", break_time, "hours")
print("Expected Exit Time:", expected_exit_time)

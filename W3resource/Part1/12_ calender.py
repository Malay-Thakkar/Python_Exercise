import calendar
from datetime import date
# from dateutil.relativedelta import relativedelta
print(calendar.month(2024,10))
day_difference = (date(2024, 10, 31) - date(2002, 10, 31)).days
# year_difference = (date(2024, 10, 31) - date(2002, 10, 31)).years
print("day diff ",day_difference)
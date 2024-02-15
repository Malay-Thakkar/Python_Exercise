# ==========================using calender ==========================
import calendar

def date_print_module(no_of_month,year):
    my_list = []
    for i in range(1,no_of_month+1):    
        days_in_month = calendar.monthrange(year,i)[1]
        my_list.append([days_in_month]) 
        #my_list.append([x for x in range(1,days_in_month+1)])
    print("using calender: ", my_list)
 
 
 #==========================using recursion ==========================
def date_print_recursion(no_of_month, year, month=1, result=[]):
    if month > no_of_month:
        print("using recursion: ", result)
        return
    days_in_month = calendar.monthrange(year, month)[1]
    result.append([days_in_month])
    
    date_print_recursion(no_of_month, year, month + 1, result)
 
#==========================using if else ==========================
def is_leap_year(year):
    if(year%4==0 and year%100!=0 or year%400==0): 
        return True
    else: 
        return False
    
def date_print_if_else(no_of_month,year):
    my_list = []
    for i in range(1,no_of_month+1):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            my_list.append([31])
        elif i == 2 and is_leap_year(year):
            my_list.append([29])  #x for x in range(1,30)
        elif i == 2 and is_leap_year(year)==False:
            my_list.append([28])      
        else:
            my_list.append([30])
    print("using if else: ", my_list)
    



#==========================if month >12 #==========================
def  date_print_gt12(month,year):
    result = []
    # if month>12:
    full_year = month//12
    result = full_year_date(full_year,original_year=year)
    extra_month = month%12
    if extra_month != 0:
        for i in range(1,extra_month+1):    
            days_in_month = calendar.monthrange(year,i)[1]
            result.append([days_in_month]) 
    print("for gt12 month: ", result)
    print(len(result))
        
def full_year_date(year,original_year,temp_year = 1,my_list = None):
    if my_list is None:
        my_list = []
    
    if temp_year > year:
        return my_list
    
    for i in range(1, 13):
        days_in_month = calendar.monthrange(original_year+temp_year-1, i)[1]
        my_list.append([days_in_month])
    
    return full_year_date(year,original_year,temp_year + 1, my_list)
    
no_of_month = int(input("Enter no of montths: "))
year = int(input("Enter year: "))

if no_of_month <= 12 and no_of_month >= 1:
    date_print_if_else(no_of_month,year)
    date_print_module(no_of_month,year)
    date_print_recursion(no_of_month,year)
else:
    print("Your Month is not valid")

date_print_gt12(50,2024)




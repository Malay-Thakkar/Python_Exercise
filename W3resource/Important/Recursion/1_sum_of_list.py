def sum_of_list(my_list):
    if len(my_list)==1:
        return my_list[0]
    else:
        return my_list[0] + sum_of_list(my_list[1:])      

my_list = [5,9,6,33,6]
print(sum_of_list(my_list))

# #__1__ print list content in new line
# for fruit in my_list:
#     print(fruit)

# #make usin list comprehension
# [print(fruit) for fruit in my_list]    

##__2__ make a upper case
# my_list = ["apple","bananas","mango"]
# print(my_list)

# new_uppercase_list = [fruit.upper() for fruit in my_list]
# print(new_uppercase_list)

##__3__ make a binary list according boolyan list
# bool_list = ["True","False","True","True","False","False"]
# binary_list = []
# for i in bool_list:
#     if i == "True":
#         binary_list.append(1)
#     else:
#         binary_list.append(0)
# binary_list_2 =[1 if i =="True" else 0 for i in bool_list]
# print(bool_list)
# print(binary_list)
# print(binary_list_2)


##__4__ string comprehension
my_string = "ThisIsCamelCaseExample"
print(id(my_string) ,  my_string)
my_string = "".join([i if i.islower() else " " + i for i in my_string])
print(id(my_string) , my_string)

#new_srtring = "".join([i if i.islower() else " " + "@" if i == "C" else " " + i for i in my_string])[1:]
#print(new_srtring) 
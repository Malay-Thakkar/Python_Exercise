my_list = [9,6,3,2,4,5,8,7,1,2,3,6,9,99,6,3,5,5,65,65,6,6,3,698,6,0,2,3,56]
max = -96985698569856
min = 0
if len(my_list):
    for i in my_list:
        if min > i:
            min = i
        elif max < i:
            max = i
print(f"max number in list {max} and minimum number is {min}")
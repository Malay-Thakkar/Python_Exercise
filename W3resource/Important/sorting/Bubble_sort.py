def bubblesort(my_list):
    for i in range(0,len(my_list)-1):
        for j in range(0,len(my_list)-i-1):
            if my_list[j]>my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
            
    return my_list


my_list = [5,9,3,1,2,7]
print(bubblesort(my_list))
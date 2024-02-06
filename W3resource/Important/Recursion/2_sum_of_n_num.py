def sum_of_postive_int(num):
    if num == 0:
        return 0
    else:
        return num + sum_of_postive_int(num-1)
print(sum_of_postive_int(9))

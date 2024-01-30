def isunique(num):
    if len(num) == len(set(num)):
        return True
    else:
        return False
print(isunique([1,2,3,4,6]))
print(isunique([]))
print(isunique([1,2,3,1,5,6]))


#map number using map
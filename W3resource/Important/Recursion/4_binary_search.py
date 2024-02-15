def binary_search(my_list, num, l, r):
    while r >= l:
        mid = (l + r) // 2
        if num == my_list[mid]:
            return mid
        if my_list[mid] < num:
            return binary_search(my_list, num, mid + 1, r)
        elif my_list[mid] > num:
            return binary_search(my_list, num, l, mid - 1)
    return -1  # Element not found

my_list = [6, 3, 2, 5, 8, 9, 7, 4, 1, 2]
my_list.sort()
print(my_list)
print("index: ", binary_search(my_list, 5, 0, len(my_list) - 1))

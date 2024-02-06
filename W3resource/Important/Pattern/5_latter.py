def print_M(n):
    for i in range(n):
        for j in range(n*2-1):
            if i == n-1 or i + j == n-1 or j - i == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


rows = 5
print_M(rows)

def print_A(rows):
    pass
def print_L(rows):
    pass
def print_Y(rows):
    pass


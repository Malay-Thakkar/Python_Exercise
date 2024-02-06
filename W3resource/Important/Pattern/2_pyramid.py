def pattern(n):
    for i in range(1,n+1):
        for k in range(0,n-i):
            print(" " ,end="")
        for j in range(0,i):
            print("* ", end="")
        print("")
pattern(5)
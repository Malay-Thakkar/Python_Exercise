inputlist = input("Enter list coma seprated: ")
finallist = [int(x) for x in inputlist.split(",")]

print(finallist)
count = 0
for i in finallist:
    if i==4:
        count+=1
print(count)
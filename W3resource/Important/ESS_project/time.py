from datetime import timedelta
import datetime
# tt = input("Enter total time (HH.MM):").split('.')
# tt = timedelta(hours=int(tt[0]),minutes=int(tt[1]))
tt = timedelta(hours=7,minutes=30)

current_time = datetime.datetime.now().time()
current_time_delta = datetime.timedelta(hours=current_time.hour, minutes=current_time.minute)

flag = 0
c = 0
timeseries = []
timelist = []
while True:
    if flag==0:
        intime = input("In time (HH.MM):").split('.')
        intime = timedelta(hours=int(intime[0]),minutes=int(intime[1]))
        timeseries.append(intime)
        flag = 1
    elif flag==1:
        outtime = input("Out time (HH.MM):").split('.')
        outtime = timedelta(hours=int(outtime[0]),minutes=int(outtime[1]))
        timeseries.append(outtime)
        flag = 0
    c += 1
    if c%2==0:
        timelist.append(outtime-intime)
    ch = input("Enter more?(y=1/n=0): ")
    if int(ch)==0:
        break

entrytime = timeseries[0]
sumtime = timedelta(hours=0,minutes=0)
for i in timelist:
    sumtime += i

if c==1:
    averagebreak = timedelta(minutes=45)
    print("\nExit time: ",entrytime + averagebreak + tt)
elif c%2==1:
    print("\nRemaining Hours: ",tt-sumtime-(current_time_delta-timeseries[-1]))
    # print("Break taken: ",(timeseries[-1]-entrytime)-sumtime)
    print("Exit time: ",timeseries[-1]+(tt-sumtime))
else:
    print("\nExit time: ",entrytime+tt)
    print("Break taken: ",(timeseries[-1]-entrytime)-sumtime)
    print("Total hours spent: ",sumtime)
    
    
# print('timelist:')
# for i in timelist:
#     print(i)

# print('timeseries:')
# for i in timeseries:
#     print(i)





# from datetime import timedelta

# tt = input("Enter total time (HH.MM):").split('.')
# tt = timedelta(hours=int(tt[0]),minutes=int(tt[1]))

# flag = 0
# c = 0
# timeseries = []
# timelist = []
# while True:
#     if flag==0:
#         intime = input("In time (HH.MM):").split('.')
#         intime = timedelta(hours=int(intime[0]),minutes=int(intime[1]))
#         timeseries.append(intime)
#         flag = 1
#     elif flag==1:
#         outtime = input("Out time (HH.MM):").split('.')
#         outtime = timedelta(hours=int(outtime[0]),minutes=int(outtime[1]))
#         timeseries.append(outtime)
#         flag = 0
#     c += 1
#     if c%2==0:
#         timelist.append(outtime-intime)
#     ch = input("Enter more?(y=1/n=0): ")
#     if int(ch)==0:
#         break

# entrytime = timeseries[0]
# sumtime = timedelta(hours=0,minutes=0)
# for i in timelist:
#     sumtime += i

# if c==1:
#     print("\nExit time: ",entrytime + tt)
# elif c%2==1: 
#     print("\nRemaining Hours: ",tt-sumtime)
#     print("Break taken: ",(timeseries[-2]-entrytime)-sumtime)
#     print("Exit time: ",timeseries[-1]+(tt-sumtime))
# else:
#     print("\nExit time: ",entrytime+sumtime)
#     print("Break taken: ",tt-sumtime)
#     print("Total hours spent: ",sumtime)
    
    

from datetime import timedelta
import datetime
import pytz

tt = input("Enter total time (HH.MM):").split('.')
tt = timedelta(hours=int(tt[0]),minutes=int(tt[1]))

india_timezone = pytz.timezone('Asia/Kolkata')
current_time = datetime.datetime.now(india_timezone).time()
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
    print("\nExit time: ",entrytime + tt)
    print("Remaining Hours: ",tt-(current_time_delta))
elif c%2==1:
    print("\nRemaining Hours: ",tt-sumtime-(current_time_delta-timeseries[-1]))
    # print("Break taken: ",(timeseries[-1]-entrytime)-sumtime)
    print("Exit time: ",timeseries[-1]+(tt-sumtime))
    print("Total hours spent: ",sumtime)
else:
    print("\nExit time: ",entrytime+tt)
    print("Break taken: ",(timeseries[-1]-entrytime)-sumtime)
    print("Total hours spent: ",sumtime)

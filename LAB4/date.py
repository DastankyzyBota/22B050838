#task1
from datetime import *
a = date.today() - timedelta(5)
print("Today: ", date.today())
print("Before 5 days: ", a)
#Today:  2024-02-20
# Before 5 days:  2024-02-15

#task2
import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday: ", yesterday )
print("Today: ", today)
print("Tomorrow: ", tomorrow)

#Yesterday:  2024-02-19
# Today:  2024-02-20
# Tomorrow:  2024-02-21

#task3
import datetime
a = datetime.datetime.today().replace(microsecond=0)
print()
print(a)
print()
#2024-02-19 14:55:27

#task4
from datetime import datetime, time
def second(a,b):
    timedelta = b-a
    return timedelta.days*24*3600 + timedelta.seconds
c= datetime.strptime()
d = datetime.now()
print("seconds" %(second(d, c)))
print()
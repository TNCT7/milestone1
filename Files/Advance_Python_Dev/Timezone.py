import timeit
from datetime import timezone, datetime, timedelta

today = datetime.now(timezone.utc)
print(today)
tomorrow = today+timedelta(days=1)
print(tomorrow)

print(today.strftime('%Y-%m-%d')) #String fromating

# userinput = input("Enter date")
# userinput = datetime.strptime(userinput,'%Y-%m-%d') # date parsing converting to date object
# print(userinput)

import time

def Power(val):
    return [i**2 for i in range(val)]

def measure(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

measure(lambda : Power(50000))

val = [5,6,7]

print(timeit.timeit("[i**2 for i in range(100)]"))
print(timeit.timeit("list(map(lambda i : i**2,range(100)))"))
x = map(Power,val)
print(list(x))
# print(timeit.timeit("list(map(Power,val))"))
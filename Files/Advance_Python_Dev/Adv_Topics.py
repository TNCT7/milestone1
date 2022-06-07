from collections import Counter
from collections import defaultdict
from collections import deque

tempreture = [2.34,3.45,7.54,9.11,4.21,3.45]

tempreture_Counter = Counter(tempreture)

print(tempreture_Counter[3.45])


coworkers = [('Jen','MIT'),('Rolf','Oxford'),('Tejas','ACPCE'),('Amruta','Pune MIT'),('John','Apple'),('Tejas','Apple')]


# coworker_Dict = {}
# almater = {}
almater = defaultdict(list)

for name,place in coworkers:
    # if name not in almater:
    #     almater[name] = []
    almater[name].append(place)

print(almater['Rolf'])
print(almater['Tejas'])


aldict = {}
allist = []




for name,place in coworkers:
    # aldict['name'] = name
    # aldict['place'] = place
    # allist.append(aldict.copy())

    #alternative method
    aldict['name'] = name
    aldict['place'] = place
    allist.append(aldict)
    aldict = {}

print(allist)

my_company = 'My Teclado'
worker1 = ['Jen','Tejas','Amruta','Rolf']
worker2 = [('abc','Apple'),('xyz','Google'),('pqr','Facebook')]

coworkers_companoes = defaultdict(lambda : my_company)

for name,place in worker2:
    coworkers_companoes[name] = place
# for name in worker1:
#     coworkers_companoes[name] = 'My Teclado'

print(coworkers_companoes[worker1[0]])
print(coworkers_companoes)


friends = deque(('Tejas','David','Sunil','Dange'))
friends.append('Vivek')
friends.appendleft('Jairaman')

print(friends)
friends.popleft()
friends.pop()
print(friends)


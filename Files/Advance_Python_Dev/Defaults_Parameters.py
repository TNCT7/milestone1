accounts = {
    'Savings' : 198.02,
    'Checking' : 177.00
}

def addBalance(amount : float,name : str = "Checking"):
    accounts[name]=accounts[name]+ amount
    return accounts[name]

a1= addBalance(200.0,'Savings')
print(a1)
a2= addBalance(200.0)
print(a2)

transactions = [
    (201.00,'Savings'),
    (-100.01,'Savings'),
    (245.21,'Checking'),
    (674.11,'Checking'),
    (786.10,'Savings')
]

for t in transactions:
    # addBalance(name = t[1],amount=t[0])
    # addBalance(t[0], t[1])
    #data unpacking method
    addBalance(*t)

print(accounts['Savings'])
print(accounts['Checking'])

class Users:
    def __init__(self, username,password):
        self.username = username,
        self.password = password
        print(f"username = {self.username} , password = {self.password}")


users =[
    {'username' :'tejas7', 'password':'Password@123'},
    {'username' :'Amruta10', 'password':'Password@1234'}
]

# listuserdetails=[Users(username = u['username'],password = u['password']) for u in users]
#Dictionay unpacking
listuserdetails=[Users(**u) for u in users]
# print((listuserdetails))


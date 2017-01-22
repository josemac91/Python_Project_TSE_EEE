import random
random.seed(3456)

class Customer(object):
    def __init__(self, name):
        self.name = name

    def description(self):
        print(self.name)

class Returner(Customer):
    @property
    def asschips(self):
        chips = random.randint(100, 300)
        return(chips)

class New(Customer):
    @property
    def asschips(self):
        chips = random.randint(200,300)
        return(chips)

class Bachelor(Customer):
    @property
    def asschips(self):
        chips = random.randint(200,500)+freebudget
        return(chips)

class Casino(object):
    def __init__(self,id):
        self.id = id
    '''def money(self):
        if day == 1:
            casinomoney=casinostartcash
        else:
            casinomoney += casinowinnings'''

class Employee(object):
    def __init__(self,name):
        self.name = name
class Bartender(Employee):

    def fixed_wage(self):
        self.fixed_wage=bartender_wage
        return(bartender_wage)
    #def tips(self):

class Dealer(Employee):

    """def dealerwage(self):
        self.dealerwage"""




'''george = Returner("george")
george.description()
print(george.chips())'''

'''customers=[]
for i in range(0,ncust):
    numero=random.randint(1,10)
    if numero==1:
        customers.append(Bachelor(str(i)))
    elif numero>1 and numero<6:
        customers.append(New(str(i)))
    else:
        customers.append(Returner(str(i)))
'''

playerlist=[]
ptype=[]
for i in range(0,10):
    playerlist.append("Player"+str(i+1))

print(playerlist)

for i in range(ncust):
    rando=random.randint(1,10)

    if rando<6:
        playerlist[i]=Returner(str(playerlist[i]))
        ptype.append("R")
    elif rando==7:
        playerlist[i] = Bachelor(str(playerlist[i]))
        ptype.append("B")
    else:
        playerlist[i] = New(str(playerlist[i]))
        ptype.append("N")

cashcash=[]
for i in range(0,10):
    cashcash.append(playerlist[i].asschips)

print(cashcash)
print(ptype)

"""
from random import randint

class Customer(object):

    def __init__(self, chips, bet):
        self.chips = chips
        self.bet = bet

class Returner(Customer):
    chips = randint(100, 300)
    if chips > tablemin
        bet = tablemin
    else:
        bet = 0

    def customer_exp(self):
        return 'Returning Customer'

class OneTimer(Customer):
    chips = randint(200, 300)
    bet = randint(0, (chips/3))

    def customer_exp(self):
        return 'One-Time Customer'

class Bachelor(Customer):
    chips = randint(200, 500)
    bet = randint(0, chips)

    def customer_exp(self):
        return 'Bachelor'
"""
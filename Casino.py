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


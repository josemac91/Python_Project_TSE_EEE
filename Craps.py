import random
from random import randint
random.seed(3456)

def AboveMinimum(betted_amounts):
    min_amount = 10
    boolist = []
    for i in range(0, len(betted_amounts)):
        if betted_amounts[i] < min_amount:
            boolist.append(False)
        else:
            boolist.append(True)
    return(boolist)

#another approach...
#import Roulette
#Roulette.AboveMinimum()

def Dices():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    sum_dices = dice1 + dice2
    return(sum_dices)

def TheHouseAlwaysWins(dicedice):
    if dicedice == 2 or dicedice == 12:
        payoff = 36*0.9
    elif dicedice == 3 or dicedice == 11:
        payoff = 18*0.9
    elif dicedice == 4 or dicedice == 10:
        payoff = 12*0.9
    elif dicedice == 5 or dicedice == 9:
        payoff = 9*0.9
    elif dicedice == 6 or dicedice == 8:
        payoff = 7.2*0.9
    else:
        payoff = 6*0.9
    return(payoff)

def RollTheDices(ba, gn, boolist):
    print('Rolling the dices...')
    sd = Dices()
    ngn = []
    for i in range(0, len(ba)):
        if boolist[i] == True:
            ngn.append(gn[i])
        else:
            ngn.append(13)
    print('And we have ' + str(sd))
    numwin = ngn.count(sd)
    if numwin == 0:
        print('No winners this round')
        casino_wins = sum(ba)
        players_lose = []
        for i in range(0, len(ba)):
            players_lose.append(0)
        outcome1 = [casino_wins, players_lose]
        print(outcome1)
    else:
        print('We have ' + str(numwin) + ' winner(s)')
        casino_wins = []
        player_wilo = []
        for i in range(0, len(ba)):
            if ngn[i] == sd:
                casino_wins.append(0)
                player_wilo.append(ba[i]*TheHouseAlwaysWins(sd))
            else:
                casino_wins.append(ba[i])
                player_wilo.append(0)
        t_casino_wins = sum(casino_wins)
        outcome2 = [t_casino_wins, player_wilo]
        print(outcome2)

def SimulateGame(guess, money):
    bl = AboveMinimum(money)
    RollTheDices(money, guess, bl)
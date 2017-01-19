import random
from random import randint
random.seed(3456)

def AboveMinimum(betted_amounts):
    min_amount = 90
    boolist = []
    for i in range(0, len(betted_amounts)):
        if betted_amounts[i] < min_amount:
            boolist.append(False)
        else:
            boolist.append(True)
    return(boolist)

def SpinTheWheel(ba, gn, boolist):
    print('Spinning the wheel...')
    landed = randint(0, 36)
    ngn = []
    for i in range(0, len(boolist)):
        if boolist[i] == True:
            ngn.append(gn[i])
        else:
            ngn.append(37)
    print('Ball lands on ' + str(landed))
    numwin = ngn.count(landed)
    if numwin == 0:
        print('No winners this round')
        casino_wins = sum(ba)
        player_lost = []
        for i in range(0, len(ba)):
            player_lost.append(0)
        outcome1 = [casino_wins, player_lost]
        print(outcome1)
    else:
        print('We have ' + str(numwin) + ' winner(s)')
        casino_wins = []
        player_wilo = []
        for i in range(0, len(ba)):
            if ngn[i] == landed:
                casino_wins.append(0)
                player_wilo.append(30*ba[i])
            else:
                casino_wins.append(ba[i])
                player_wilo.append(0)
        t_casino_wins = sum(casino_wins)
        outcome2 = [t_casino_wins, player_wilo]
        print(outcome2)

def SimulateGame(guess, money):
    bl = AboveMinimum(money)
    SpinTheWheel(money, guess, bl)

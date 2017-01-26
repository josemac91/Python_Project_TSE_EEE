import random
from random import randint
# This is used to fixed the random generator so we can test the output
random.seed(3456)

"""
Keep in mind the following:
- As in the Roulette, we need to ensure that players who bet below the table minimum lose
- Players still have to decide on an amount to bet and on which outcome from 2 to 12 they bet money on
- Similarly, we only care about the sum of the two dices; no colors are associated to the random outcome
- The trick is that we need to account for the fact that not all outcomes have the same likelihood
- We have to rescale the payoffs so that we don't have everybody betting on 7
- We also have to ensure that the house wins, on average, 10% of the total amounts bet
"""

def AboveMinimum(betted_amounts):
    min_amount = 10
    boolist = []
    for i in range(0, len(betted_amounts)):
        if betted_amounts[i] < min_amount:
            boolist.append(False)
        else:
            boolist.append(True)
    return(boolist)

# AboveMinimum is the same as the one in Roulette
# Note that minimum amount is arbitrarily chosen (we had no example to guide our decision)

def Dices():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    sum_dices = dice1 + dice2
    return(sum_dices)

# Function Dices defines our outcome, which is the sum of two random variable
# Clearly, not all outcomes has the same probability
# For example, the probability of getting 12 is 1/36
# Out of 36 possible combinations, there's only one that gives you 12, which is 6 + 6
# This is only the case when the dice rolls are independent events

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

# The probability that the sum of the dice equal 2 or 12 is 1/36
# And the probability for getting 3 or 11 is 2/36
    # For 3: Prob(dice1 = 1) x Prob(dice2 = 2) + Prob(dice1 = 2) x Prob(dice2 = 1) = 1/36 + 1/36 = 2/36
# And the probability of getting: 4 or 10 is 3/36; 5 or 9 is 4/36; 6 or 8 is 5/36; and 7 9s 6/36
# To rescale the game each outcome is multiplied by the reciprocal of its probability
# Now players who bet on 2 (one of the less probably outcomes) receives 36 times his bet amount
# While players who bet on 7 (the most probable outcome) receives 6 times his bet amount
# We insure Casino's on average 10% profit by making players only receive 90% of their total earnings

# RollTheDices gives the structure of the Craps
# It's a function of the players: bet amounts (ba), the guess numbers (gn), the eligibility (boolist)
# As with the Roulette, we first insure those below the minimum always lose

def RollTheDices(ba, gn, boolist):
    print('Rolling the dices...')
    sd = Dices()
    ngn = []
    # ngn stands for new guess numbers
    for i in range(0, len(ba)):
        if boolist[i] == True:
            ngn.append(gn[i])
        else:
            ngn.append(13)
        # those not eligible to win are assigned the ngn 13 and thus always lose
    print('And we have ' + str(sd))
    numwin = ngn.count(sd)
    # here we know the sum of the dices and the number of winners
    # either nobody wins or at least one player wins
    if numwin == 0:
        print('No winners this round')
        casino_wins = sum(ba)
        # the casino takes it all
        players_lose = []
        for i in range(0, len(ba)):
            players_lose.append(0)
        # all players lose and are assigned a 0 as their earnings
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
            # when a player wins, the casino loses that player's bet amount
            # winning player gets his ba times the rescaling of payoffs proposed previously
            # sd gives the random sum of the two dices
            # and allocates the correct payoff to that number as defined in TheHouseAlwaysWins
            else:
                casino_wins.append(ba[i])
                player_wilo.append(0)
            # losing players get 0
            # the casino keeps their amounts bet
        t_casino_wins = sum(casino_wins)
        outcome2 = [t_casino_wins, player_wilo]
        print(outcome2)

# The simulation is based on the above functions
# Note that guess numbers (guess) and amount bet (money) of the players have to be given

def SimulateGame(guess, money):
    min_min = AboveMinimum(money)
    RollTheDices(money, guess, min_min)
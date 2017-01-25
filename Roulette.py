import random
from random import randint
# This is used to fixed the random generator so we can test the output
random.seed(3456)

"""
Keep in mind the following:
- Players have two defining characteristics: how much money they bet and which number they bet money on
- We create a simple roulette, i.e. we only care for the numbers and thus do not assign colors (black/red)
- There are 37 outcomes since zero is a possibility; each player has probability 1/37 of winning
- Winner gets 30 times his money bet
- Those who bet below the minimum allowed on the table always lose
- Total money bet is distributed at the end of a round between the house and, if any, the winner(s)
"""

# We first need to determine which players are eligible to win at Roulette
# Picture players reporting how much money they're going to bet
# There's a table minimum, but some players don't bother to inform themselves
# Because these player lose instantly, the house has no incentives to inform them

def AboveMinimum(bet_amounts):
    min_amount = 90
    boolist = []
    for i in range(0, len(bet_amounts)):
        if bet_amounts[i] < min_amount:
            boolist.append(False)
        else:
            boolist.append(True)
    return(boolist)

# AboveMinimum filters out one-by-one the players that bet money below the allowed minimum
# It's a function only of how much money they bet; here we don't care about which number they bet on
# min_amount is arbitrary, we pick 90 in order to match with the results presented in homework slides
# boolist is a vector of booleans where we record the eligibility to win of players
# i.e. it's False that a player who bet below the minimum amount can win the game
# append() adds to boolist whether it's True or False that given i is eligible to win

# SpinTheWheel gives the structure of the Roulette
# It's a function of the players: bet amounts (ba), the guess numbers (gn), the eligibility (boolist)
# The house only has to spin the wheel...
# By construction, ba and gn have a 1-to-1 correspondence
# We first have to ensure that those who bet incorrectly are punished
# Then we have to know where the ball lands, count the winners, and determine the distribution of the money

def SpinTheWheel(ba, gn, boolist):
    print('Spinning the wheel...')
    landed = randint(0, 36)
    # the ball falls randomly between 0 and 36 (a random integer, or randint)
    ngn = []
    # ngn stands for new guess numbers
    for i in range(0, len(boolist)):
        if boolist[i] == True:
            ngn.append(gn[i])
        else:
            ngn.append(37)
    # we want to ensure that those who bet below the minimum amount never win
    # players with True chances of winning keep their original guess number
    # players with False chances are assigned the guess number 37 and thus always lose
    print('Ball lands on ' + str(landed))
    numwin = ngn.count(landed)
    # so far we know where the ball lands (landed) and how many winners we have (numwin)
    # two main scenarios: either nobody wins (outcome1) or at least one person wins (outcome2)
    if numwin == 0:
        print('No winners this round')
        casino_wins = sum(ba)
        # casino takes it all
        player_lost = []
        for i in range(0, len(ba)):
            player_lost.append(0)
        # all players are assigned 0 as their profits
        outcome1 = [casino_wins, player_lost]
        print(outcome1)
    else:
        print('We have ' + str(numwin) + ' winner(s)')
        casino_wins = []
        player_wilo = []
        for i in range(0, len(ba)):
            if ngn[i] == landed:
                casino_wins.append(0)
                # for each player that wins, the casino makes 0 profits
                player_wilo.append(30*ba[i])
                # each winner earns 30 times their beat amount (ba)
            else:
                casino_wins.append(ba[i])
                # casino wins the bet amount of each player who lost
                player_wilo.append(0)
                # losers are assigned 0 to their profits
        t_casino_wins = sum(casino_wins)
        outcome2 = [t_casino_wins, player_wilo]
        print(outcome2)

# Outcomes, following the example in slides, are presented by casino and by each player
# Now we can simulate our game
# The simulation is based on the above functions
# Note that guess numbers (guess) and amount bet (money) of the players have to be given

def SimulateGame(guess, money):
    min_min = AboveMinimum(money)
    SpinTheWheel(money, guess, min_min)

import Roulette
allbets = [10, 24, 36, 0, 11, 24]
allamounts = [10, 85, 120, 65, 150, 122]
Roulette.SimulateGame(allbets, allamounts)
Roulette.SimulateGame(allbets, allamounts)

import Craps
crapsguesses = [7, 9, 2, 10, 3]
crapsbets = [50, 70, 30, 40, 50]
Craps.SimulateGame(crapsguesses, crapsbets)
Craps.SimulateGame(crapsguesses, crapsbets)

"""
Using random.seed(3456) and the corresponding minimum amounts, you should get for the above inputs...

For Roulette:

Spinning the wheel...
Ball lands on 24
We have 1 winner(s)
[430, [0, 0, 0, 0, 0, 3660]]

Spinning the wheel...
Ball lands on 30
No winners this round
[552, [0, 0, 0, 0, 0, 0]]

For Craps:

Rolling the dices...
And we have 10
We have 1 winner(s)
[200, [0, 0, 0, 432.0, 0]]

Rolling the dices...
And we have 7
We have 1 winner(s)
[190, [270.0, 0, 0, 0, 0]]
"""


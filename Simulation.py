import Roulette
import Craps

#The guesses
allbets = [10, 24, 36, 0, 11, 24]
#The wagers
allamounts = [10, 85, 120, 65, 150, 122]
#Running the roulette game twice
Roulette.SimulateGame(allbets, allamounts)
Roulette.SimulateGame(allbets, allamounts)

#Craps guesses
crapguesses = [7, 9, 2, 11, 3]
#The wagers for craps
crapbets = [50, 70, 30, 40, 50]
#Simulating a game of craps
Craps.SimulateGame(crapguesses, crapbets)
Craps.SimulateGame(crapguesses, crapbets)

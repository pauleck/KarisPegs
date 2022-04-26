from Classes.Game import Game
from Classes.Results import Results

results = Results()

attemptsPerStartingPosition = 50000

print ("---------- PLAYING GAMES ------------")
for n in range(attemptsPerStartingPosition):
    for startingPosition in range(1,16):
        result = Game.playGame(startingPosition)
        results.addResult(result)

results.printResults()
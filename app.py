# Pegs - Program to play the "Peg game" popular in the "Cracker Barrel" chain of resturants
# Karis Eccleston - 3/15/2022

# This is our main class that will play the Peg game over and over again and will pause when a game is won
# We also keep statistics on how many pegs are left for each starting position so that a player will then no where the best starting position
# should be to win the game
import random
from time import sleep
from Classes.Game import Game
from Classes.Results import Results
from Classes.Statistics import Statistics
from graphics import *
from Classes.Statistics import *
from Classes.Ui import *

# Thie is where we start all the results so that we can show a statistics window
results = Results()
statistics = Statistics()

# This class controls all the UI on the screen
Ui = Ui()

# How many games we have played
numGames = 0

# Delay between each move of the game so that you can see each move being made, buttons on on the screen can be used to speed up or slow down the game
delayTimeMS = 100

# Keep going forever and ever and ever until the user closes the window
while True:
    # Pick a random position to remove a peg (the "starting position")
    startingPosition = random.randint(1,16)

    # Go play a game!
    result = Game.playGame(startingPosition, True, Ui.win, Ui.board, delayTimeMS)

    # Display whether this game won or lost
    Ui.SetWinLoseText(result.won)

    # Add 1 to the number of games and send that back to our UI class to display on the screen
    numGames = numGames + 1
    Ui.AddGame(numGames)

    # Take a break!
    sleep(delayTimeMS/1000)

    # Check to see if any of our buttons have been clicked
    clicked = Ui.checkMouseInputs()
    if (clicked == "SPEEDUP"):
        delayTimeMS = delayTimeMS / 2

    if (clicked == "SLOWDOWN"):
        delayTimeMS = delayTimeMS * 2

    if (clicked == "STATS"):
        statistics.drawChart()

    # Add this game to our statistics to show later    
    statistics.addResult(startingPosition, result.pegsLeft, False)
    results.addResult(result)

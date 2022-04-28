from asyncio.windows_events import NULL
import random
from time import sleep
from Classes.Board import Board
from Classes.Game import Game
from Classes.Results import Results
from Classes.Statistics import Statistics
from graphics import *
from Classes.Statistics import *
from Classes.Ui import *

results = Results()

attemptsPerStartingPosition = 1
statistics = Statistics()

# win = GraphWin("Peg", 640, 520)
# win.setBackground("white")

# board = Board()
# board.setupBoard(win)

Ui = Ui()

numGames = 0
delayTimeMS = 100

# textWinLose = Text(Point(310,380),"")
# textWinLose.setSize(30)
# textWinLose.draw(win)
# textGamesPlayed = Text(Point(305,425), "")
# textGamesPlayed.setSize(18)
# textGamesPlayed.draw(win)

# speedUp = Rectangle(Point(50,410), Point(160,440))
# speedUp.setFill("GRAY")
# speedUp.draw(win)

# textSpeedUp = Text(Point(104,425), "SPEED UP")
# textSpeedUp.setSize(15)
# textSpeedUp.setTextColor("WHITE")
# textSpeedUp.draw(win)

# slowDown = Rectangle(Point(450,410), Point(592,440))
# slowDown.setFill("GRAY")
# slowDown.draw(win)

# textSlowDown = Text(Point(520,425), "SLOW DOWN")
# textSlowDown.setSize(15)
# textSlowDown.setTextColor("WHITE")
# textSlowDown.draw(win)

# showStats = Rectangle(Point(180,470), Point(440,510))
# showStats.setFill("CYAN")
# showStats.draw(win)

# showStatsText = Text(Point(310,490), "SHOW STATISTICS")
# showStatsText.setSize(19)
# showStatsText.setTextColor("BLACK")
# showStatsText.draw(win)

while True:
    startingPosition = random.randint(1,16)

    result = Game.playGame(startingPosition, True, Ui.win, Ui.board)
    Ui.SetWinLoseText(result.won)
    # if (result.won):
    #     textWinLose.setText(" WIN - CLICK TO CONTINUE ")
    #     textWinLose.setTextColor("green")
    #     win.getMouse() # Pause to view result

    # else:
    #     textWinLose.setText(" LOSE ")
    #     textWinLose.setTextColor("RED")

    numGames = numGames + 1
    Ui.AddGame(numGames)

    # textGamesPlayed.setText (str(numGames) + " GAMES PLAYED")
    sleep(delayTimeMS/1000)

    clicked = Ui.checkMouseInputs()
    if (clicked == "SPEEDUP"):
        delayTimeMS = delayTimeMS / 2

    if (clicked == "SLOWDOWN"):
        delayTimeMS = delayTimeMS * 2

    if (clicked == "STATS"):
        statistics.drawChart()
    
    statistics.addResult(startingPosition, result.pegsLeft, False)
    results.addResult(result)

#results.printResults()
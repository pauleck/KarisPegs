from asyncio.windows_events import NULL
import random
from time import sleep
from Classes.Board import Board
from Classes.Game import Game
from Classes.Results import Results
from Classes.Statistics import Statistics
from graphics import *
from Classes.Statistics import *

class Ui:
    def __init__(self):
        self.win = GraphWin("Peg", 640, 520)
        self.win.setBackground("white")

        self.board = Board()
        self.board.setupBoard(self.win)

        self.textWinLose = Text(Point(310, 380), "")
        self.textWinLose.setSize(30)
        self.textWinLose.draw(self.win)

        self.textGamesPlayed = Text(Point(305, 425), "")
        self.textGamesPlayed.setSize(18)
        self.textGamesPlayed.draw(self.win)

        speedUp = Rectangle(Point(50, 410), Point(160, 440))
        speedUp.setFill("GRAY")
        speedUp.draw(self.win)

        textSpeedUp = Text(Point(104, 425), "SPEED UP")
        textSpeedUp.setSize(15)
        textSpeedUp.setTextColor("WHITE")
        textSpeedUp.draw(self.win)

        slowDown = Rectangle(Point(450, 410), Point(592, 440))
        slowDown.setFill("GRAY")
        slowDown.draw(self.win)

        textSlowDown = Text(Point(520, 425), "SLOW DOWN")
        textSlowDown.setSize(15)
        textSlowDown.setTextColor("WHITE")
        textSlowDown.draw(self.win)

        showStats = Rectangle(Point(180, 470), Point(440, 510))
        showStats.setFill("CYAN")
        showStats.draw(self.win)

        showStatsText = Text(Point(310, 490), "SHOW STATISTICS")
        showStatsText.setSize(19)
        showStatsText.setTextColor("BLACK")
        showStatsText.draw(self.win)

    def AddGame(self, numGames):
        self.textGamesPlayed.setText (str(numGames) + " GAMES PLAYED")

    def SetWinLoseText(self, didWin):
        if (didWin == True):
            self.textWinLose.setText(" WIN - CLICK TO CONTINUE ")
            self.textWinLose.setTextColor("green")
            self.win.getMouse() # Pause to view result
        else:
            self.textWinLose.setText(" LOSE ")
            self.textWinLose.setTextColor("RED")

    def checkMouseInputs(self):
        click = self.win.checkMouse()
        if (click != None):
            # Speed up
            if (click.x >45 and click.x < 158 and click.y > 408 and click.y < 441):
                return "SPEEDUP"

            # Slow down
            if (click.x >457 and click.x < 589 and click.y > 411 and click.y < 441):
                return "SLOWDOWN"

            if (click.x >182 and click.x < 439 and click.y > 470 and click.y < 506):
                return "STATS"

            return ""
            #     delayTimeMS = delayTimeMS * 2

            # # Show statistics
            # if (click.x >182 and click.x < 439 and click.y > 470 and click.y < 506):
            #     statistics.drawChart()

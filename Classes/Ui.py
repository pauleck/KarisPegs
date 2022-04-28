# Pegs - Program to play the "Peg game" popular in the "Cracker Barrel" chain of resturants
# Karis Eccleston - 3/15/2022

# This class is used to display the UI, which includes the board, the speed up/slow down buttons and show statistics
from asyncio.windows_events import NULL
from Classes.Board import Board
from graphics import *
from Classes.Statistics import *

class Ui:
    def __init__(self):
        # Using graphics library imported above create a window with resolution of 640 by 520, white background and label it Peg Game by Karis Eccleston   
        self.win = GraphWin("Peg Game by Karis Eccleston", 640, 520)
        self.win.setBackground("white")

        # Using the board class setup the board (the triangle will all the pegs)
        self.board = Board()
        self.board.setupBoard(self.win)

        # Text to show whether you win or lose in each round
        self.textWinLose = Text(Point(310, 380), "")
        self.textWinLose.setSize(30)
        self.textWinLose.draw(self.win)

        # Text to show number of games played
        self.textGamesPlayed = Text(Point(305, 425), "")
        self.textGamesPlayed.setSize(18)
        self.textGamesPlayed.draw(self.win)

        # Button to show "speed up" to play games faster
        speedUp = Rectangle(Point(50, 410), Point(160, 440))
        speedUp.setFill("GRAY")
        speedUp.draw(self.win)
        textSpeedUp = Text(Point(104, 425), "SPEED UP")
        textSpeedUp.setSize(15)
        textSpeedUp.setTextColor("WHITE")
        textSpeedUp.draw(self.win)

        # Button to show "slow down" to play games faster
        slowDown = Rectangle(Point(450, 410), Point(592, 440))
        slowDown.setFill("GRAY")
        slowDown.draw(self.win)
        textSlowDown = Text(Point(520, 425), "SLOW DOWN")
        textSlowDown.setSize(15)
        textSlowDown.setTextColor("WHITE")
        textSlowDown.draw(self.win)

        # Button to show "show statistics" to show average number of pegs left per starting position
        showStats = Rectangle(Point(180, 470), Point(440, 510))
        showStats.setFill("CYAN")
        showStats.draw(self.win)

        showStatsText = Text(Point(310, 490), "SHOW STATISTICS")
        showStatsText.setSize(19)
        showStatsText.setTextColor("BLACK")
        showStatsText.draw(self.win)

    # Show the number of games played
    def AddGame(self, numGames):
        self.textGamesPlayed.setText (str(numGames) + " GAMES PLAYED")

    # Set the win lose text
    def SetWinLoseText(self, didWin):
        if (didWin == True):
            self.textWinLose.setText(" WIN - CLICK TO CONTINUE ")
            self.textWinLose.setTextColor("green")
            self.win.getMouse() # Pause to view result
        else:
            self.textWinLose.setText(" LOSE ")
            self.textWinLose.setTextColor("RED")

    # Check for a mouse click to see if they click the speed up, slow down or statistics buttons, using coordinates of the buttons
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
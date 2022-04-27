from Classes.Board import Board
from Classes.Game import Game
from Classes.Results import Results
from graphics import *
from button import *

results = Results()

attemptsPerStartingPosition = 1

#result = Game.playGame(1, True, 500, win)

stats = GraphWin("Peg statistics", 320, 400)
stats.setBackground("gray")

win = GraphWin("Peg", 640, 480)
win.setBackground("white")

board = Board()
board.setupBoard(win)

while True:
    button = Button("SHOW STATISTICS", Point(160,420), Point(450,460),"green", "green", "white", 20, win)
    textWinLose = Text(Point(310,380),"")
    textWinLose.setSize(30)
    textWinLose.draw(win)

    for startingPosition in range(1,16):
        result = Game.playGame(startingPosition, True, 5, win, board)
        if (result.won):
            textWinLose.setText(" WIN ")
            textWinLose.setTextColor("green")
        else:
            textWinLose.setText(" LOSE ")
            textWinLose.setTextColor("RED")

            time.sleep(.2)
            textWinLose.setText("")

        #results.addResult(result)

#results.printResults()
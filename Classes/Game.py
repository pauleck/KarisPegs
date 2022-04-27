from ctypes import sizeof
from Classes.Board import Board
from Classes.Mover import Mover
from Classes.Result import Result

import random
import time

class Game:
    @staticmethod
    def playGame(startingPosition, showMoves, delayBetweenEachMoveMS, win, board):
        result = Result()
        pegs = {}

        for loop in range(1,16):
            pegs[loop] = 1

        mover = Mover()
        result.startingPosition = startingPosition

        pegs[startingPosition] = 0
        movesAvailable = True

        while (movesAvailable):
            theMove = mover.makeMove(pegs)
            if (len(theMove) == 0):  # No move found
                movesAvailable = False               
                result.pegsLeft = numPegsAfter
                if (numPegsAfter == 1) :
                    result.won = True
            else:
                movedTo = int(theMove.split("-")[1].replace(",", ""))

                result.moves = result.moves + theMove
                numPegsAfter = Board.countPegsLeft(pegs)
            
                if (showMoves):
                    board.drawBoard(pegs, win, movedTo)
                    time.sleep(delayBetweenEachMoveMS/1000)

        return result
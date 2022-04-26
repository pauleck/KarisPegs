from Classes.Board import Board
from Classes.Mover import Mover
from Classes.Result import Result

import random

class Game:
    @staticmethod
    def playGame(startingPosition):
        result = Result()
        pegs = {}

        for loop in range(1,16):
            pegs[loop] = 1

        mover = Mover()
        result.startingPosition = startingPosition

        pegs[startingPosition] = 0
        movesMade = []

        movesAvailable = True
        while (movesAvailable):
            numPegsBefore = Board.countPegsLeft(pegs)

            result.moves = result.moves + mover.makeMove(pegs)
            numPegsAfter = Board.countPegsLeft(pegs)
            
            if (numPegsBefore == numPegsAfter):
                movesAvailable = False
                result.pegsLeft = numPegsAfter
                if (numPegsAfter == 1) :
                    result.won = True

        return result
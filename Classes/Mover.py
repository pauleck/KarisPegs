from array import *
import random

class Mover:
    def __init__(self):
        config = [
                    "4-2:6-3",  # 1
                    "7-4:9-5",  # 2
                    "10-6:8-5", # 3
                    "1-2:6-5:11-7:13-8", # 4
                    "12-8:14-9", # 5
                    "15-10:1-3:4-5:13-9", # 6
                    "9-8:2-4", # 7
                    "3-5:10-9", # 8
                    "7-8:2-5", # 9
                    "3-6:8-9", # 10
                    "13-12:4-7", # 11
                    "5-8:14-13", # 12
                    "6-9:15-14:11-12:4-8", # 13
                    "12-13:5-9", # 14
                    "6-10:13-14"] # 15

        self.moves = {}
        pegNumber = 1

        # Iterate thru all the configs for each peg
        for peg in config:
            moveList = []

            # Get every move from config, each move seperated by :
            oneMoveConfig = peg.split(':')

            # For this move get the starting position and peg that we jump over, numbers seperated by -
            for one in oneMoveConfig:
                thisMoveConfig = one.split('-')
                mt = MoveTypes(pegNumber, int(thisMoveConfig[0]), int(thisMoveConfig[1]))
                moveList.append(mt)

            self.moves[pegNumber] = moveList
            pegNumber = pegNumber + 1

    def makeMove(self, pegs):
        movesAvailable = []

        # Find all available moves
        for peg in pegs:
            pegValue = pegs[peg]
            if (pegValue == 1):       # We have a peg here so moves possible!
                possibleMoves = self.moves[peg]

                for move in possibleMoves:
                    # Start has to have a peg, end should not, jump needs a peg
                    if (pegs[move.startPosition] == 1 and pegs[move.endPosition] == 0 and pegs[move.jumpOver] == 1):
                        movesAvailable.append(move)

                       # print (move.startPosition, move.endPosition, move.jumpOver)

        # Pick a random one (if we have any!)
        numMoves = len(movesAvailable)
        if (numMoves == 0):
            return "" # No move

        rf = random.randint(0, numMoves-1)

        theMove = movesAvailable[rf]

        # Move
        pegs[theMove.startPosition] = 0
        pegs[theMove.jumpOver] = 0
        pegs[theMove.endPosition] = 1

        return (str(theMove.startPosition) + "-" + str(theMove.endPosition) + ",")

class MoveTypes:
    def __init__(self, startPosition, endPosition, jumpOver) :
        self.startPosition = startPosition
        self.endPosition = endPosition
        self.jumpOver = jumpOver


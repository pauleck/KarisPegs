# Pegs - Program to play the "Peg game" popular in the "Cracker Barrel" chain of resturants
# Karis Eccleston - 3/15/2022

# This class is used to actually play the game, using random moves until no more moves are left

from Classes.Mover import Mover
from Classes.Result import Result
from time import sleep

class Game:
    @staticmethod
    # This function is used to start the game
    #   startingPosition  - Which of the 15 available pegs are empty
    #   showMoves         - Show each game being played on a graphical board
    #   win               - The graphical window used to show the graphical board
    #   board             - Instance of the board class which is used to show the graphical board
    def playGame(startingPosition, showMoves, win, board, delayBetweenEachMove):
        result = Result()

        # Setup a dictionary with all the pegs and start by putting a peg in each one
        pegs = {}
        for loop in range(1,16):
            pegs[loop] = 1

        # Remove a peg in the starting position
        result.startingPosition = startingPosition
        pegs[startingPosition] = 0

        # Class which is used to calculate next available moves
        mover = Mover()

        # Loop thru until we either WIN (yeah!) or run of moves (boo!)
        movesAvailable = True
        while (movesAvailable):
            # Make a move
            theMove = mover.makeMove(pegs)

            # No move found
            if (len(theMove) == 0):  # No move found
                movesAvailable = False               
                result.pegsLeft = Game.countPegsLeft(pegs)
                if (result.pegsLeft == 1):
                    result.won = True

            else:
                # The mover.makeMove returns the peg came from and peg it went to for example 2-5
                movedTo = int(theMove.split("-")[1].replace(",", ""))

                # Keep track of all the moves made here
                result.moves = result.moves + theMove

                # If requested draw a pretty board            
                if (showMoves):
                    board.drawBoard(pegs, movedTo)

                sleep(delayBetweenEachMove/1000)

        return result

    @staticmethod
    # Count number of pegs left
    def countPegsLeft(pegs):
        totalPegs = 0
        for pegPosition in range(1,16):
            if (pegs[pegPosition] == 1):
                totalPegs = totalPegs + 1
        
        return totalPegs
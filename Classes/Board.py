from array import *

class Board:
    @staticmethod
    def drawBoard(pegs):
        # Figure out display positions
        rowStartingValues = array('i', [0, 9, 7, 5, 3, 1])  # Ignore first element
        spacesBetweenCols = 3

        # Start at first peg
        arrayPosition = 1
        for row in range(1,6):
            prtLine = ""

            # Add spaces to get to the starting position of this row
            for spaces in range(rowStartingValues[row]):
                prtLine += " "

            # Display all the pegs in this row
            for cols in range(row):
                prtLine += str(pegs[arrayPosition])
                arrayPosition = arrayPosition + 1

                # Add the spaces
                for spaces in range(spacesBetweenCols):
                    prtLine += " "

            print (prtLine)

    @staticmethod
    def countPegsLeft(pegs):
        totalPegs = 0
        for pegPosition in range(1,16):
            if (pegs[pegPosition] == 1):
                totalPegs = totalPegs + 1
        
        return totalPegs

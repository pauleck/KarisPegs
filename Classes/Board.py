from array import *
from graphics import *

class Board:
    @staticmethod
    def drawBoard(pegs, useGraphics, win, pegMoved):
        if (useGraphics == False):
            Board.drawBoardText(pegs, win)
        else:
            Board.drawBoardGraphics(pegs, win, pegMoved)

    @staticmethod
    def countPegsLeft(pegs):
        totalPegs = 0
        for pegPosition in range(1,16):
            if (pegs[pegPosition] == 1):
                totalPegs = totalPegs + 1
        
        return totalPegs

    @staticmethod
    def drawBoardText(pegs):
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
    def drawBoardGraphics(pegs, win, pegMoved):
        top  = Point(320, 10)
        bottomLeft = Point(60,360)
        bottomRight = Point(550,360)
        
        triangle = Polygon(top, bottomLeft, bottomRight)
        triangle.setFill("yellow")
        triangle.draw(win)

        pegPositions = []
        pegPositions.append(Point(318,80))    

        pegPositions.append(Point(280,140))    
        pegPositions.append(Point(356,140))    
        
        pegPositions.append(Point(240,200))    
        pegPositions.append(Point(318,200))    
        pegPositions.append(Point(400,200))    

        pegPositions.append(Point(190,260))    
        pegPositions.append(Point(280,260))    
        pegPositions.append(Point(356,260))    
        pegPositions.append(Point(440,260))    
        
        pegPositions.append(Point(145,320))    
        pegPositions.append(Point(240,320))    
        pegPositions.append(Point(318,320))    
        pegPositions.append(Point(400,320))    
        pegPositions.append(Point(480,320))    
        
        radius = 25
        
        pegCircles = []    
        pegPosition  = 1
        for p in pegPositions:
            c = Circle(p, radius)
            if (pegMoved == pegPosition):
                c.setFill("red")
            else:
                if (pegs[pegPosition] == 0):
                    c.setFill("white")
                else:
                    c.setFill("green")

            pegCircles.append(c)
            c.draw(win)
            pegPosition = pegPosition + 1

from array import *
from graphics import *

class Board:
    def setupBoard(self, win):
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
        
        self.pegCircles = []    

        for p in pegPositions:
            c = Circle(p, radius)
            c.setFill("white")
            self.pegCircles.append(c)
            c.draw(win)

    def drawBoard(self, pegs, win, pegMoved):
        Board.drawBoardGraphics(self, pegs, win, pegMoved)

    def countPegsLeft(pegs):
        totalPegs = 0
        for pegPosition in range(1,16):
            if (pegs[pegPosition] == 1):
                totalPegs = totalPegs + 1
        
        return totalPegs

    def drawBoardGraphics(self, pegs, win, pegMoved):
        pegPosition = 1
        
        for c in self.pegCircles:
            if (pegMoved == pegPosition):
                c.setFill("red")
            else:
                if (pegs[pegPosition] == 0):
                    c.setFill("white")
                else:
                    c.setFill("green")

            pegPosition = pegPosition + 1

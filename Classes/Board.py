# Pegs - Program to play the "Peg game" popular in the "Cracker Barrel" chain of resturants
# Karis Eccleston - 3/15/2022

# This class is used to display the board and the pegs 
from array import *
from graphics import *

class Board:
    def setupBoard(self, win):
        # Draw the triangle
        top  = Point(320, 10)
        bottomLeft = Point(60,360)
        bottomRight = Point(550,360)
        triangle = Polygon(top, bottomLeft, bottomRight)
        triangle.setFill("yellow")
        triangle.draw(win)

        # Decide where all the pegs live for each row
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
        
        # Draw the pegs
        radius = 25
        self.pegCircles = []    

        for p in pegPositions:
            c = Circle(p, radius)
            c.setFill("white")
            self.pegCircles.append(c)
            c.draw(win)

    # Draw the board every time a move is made
    def drawBoard(self, pegs, pegMoved):
        pegPosition = 1
        
        for c in self.pegCircles:
            # Peg was moved to this spot so color it red
            if (pegMoved == pegPosition):
                c.setFill("red")
            else:
                # This spot has no peg so white
                if (pegs[pegPosition] == 0):
                    c.setFill("white")
                else:
                    # Peg here so green
                    c.setFill("green")

            pegPosition = pegPosition + 1

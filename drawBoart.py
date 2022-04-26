from turtle import circle
from graphics import *

# function definition
def main():
    
    win = GraphWin("Peg", 640, 480)
    win.setBackground("white")
    #win.setCoords(-1.75, -200, 11.5, 10400)

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
    
    pegs = []    
    for p in pegPositions:
        c = Circle(p, radius)
        c.setFill("green")
        pegs.append(c)
        c.draw(win)
        
    input("Press <Enter> to quit window")
    win.close()
    
main()

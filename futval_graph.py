# futval_graph.py
#
# module definition

from graphics import *


# function definition
def main():
    # Introduction

    # Get principal and interest rate
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the Annualized Interest Rate:"))

    # Create Window
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), '0.0K').draw(win)
    Text(Point(-1, 2500), '2.5K').draw(win)
    Text(Point(-1, 5000), '5.0K').draw(win)
    Text(Point(-1, 7500), '7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    # Draw Initial bar for Principal
    # height = principal * 0.02
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1, 11):
        principal = principal * (1 + apr)
        # print("Year:",year,end="\n")
        # print("  Principal:",round(principal,2),end="\n")
        # xll = year*25+40
        # height = principal*0.02
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

        # Close window
    input("Press <Enter> to quit window")
    win.close()


main()

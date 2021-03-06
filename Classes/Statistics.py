# Pegs - Program to play the "Peg game" popular in the "Cracker Barrel" chain of resturants
# Karis Eccleston - 3/15/2022

# This class is used to store and display statistics about the number of games played, specifically how many pegs on average are left in each 
# starting position

from graphics import *

class Statistics:
    # Setup the statistics we need which is a total of the pegs left in each game for each starting position
    # and the number of games attempted for each start position, then we can calculate the averages
    def __init__(self):
        self.pegsLeftByStarintgPosition = []
        self.numberGamesPlayednStartingPosition = []

        for loop in range(1, 18):
            self.pegsLeftByStarintgPosition.append(0)
            self.numberGamesPlayednStartingPosition.append(0)

    # A game has been played so show the results
    def addResult(self, startingPosition, pegsLeft, showChart):
        # Make sure this is a number
        startingPosition = int(startingPosition)

        self.pegsLeftByStarintgPosition[startingPosition] = self.pegsLeftByStarintgPosition[startingPosition] + pegsLeft
        self.numberGamesPlayednStartingPosition[startingPosition] = self.numberGamesPlayednStartingPosition[startingPosition] + 1

        if (showChart == True) :
            self.drawChart()

    # Draw the graphs showing average pegs left for each starting position
    def drawChart(self):
        # Configuration to help position the graph in the window
        windowHeight = 500
        windowWidth = 500
        paddingPerLine = 5
        chartXPositionStart = 40
        startYPosition = 10
        textYPadding = 10
        maxWidth = 420
        maxPegsLeft = 8
        xWidthForeachPegLeft = maxWidth / maxPegsLeft
        averagePosition = 440

        # Create the window and make it gray
        statsWindow = GraphWin("Average Pegs Left Based on Starting Position", windowHeight, windowWidth)
        statsWindow.setBackground("gray")

        # Calculate height of each graph line, 15 lines and 10 pixels between each line
        heightPerLine = ((windowHeight-startYPosition) / 15) - paddingPerLine

        # Draw each of the 16 lines
        chartLabels = []
        chartLines = []

        yPosition = startYPosition
        
        for loop in range(1, 16):
            # Show the starting position
            t = Text(Point(10, yPosition + textYPadding), str(loop))
            chartLabels.append(t)
            t.draw(statsWindow)

            # Draw rectangle if this starting position "seen" yet
            if (self.numberGamesPlayednStartingPosition[loop] != 0):
                averagePegs = self.pegsLeftByStarintgPosition[loop] / self.numberGamesPlayednStartingPosition[loop]
            else:
                averagePegs = 0

            # Figure out size of the chart, we can have at most 13 pegs left, sustract the average and then calculate bar length
            xSize = (maxPegsLeft - averagePegs ) * xWidthForeachPegLeft

            # Draw the chart for this starting position
            r = Rectangle(Point(chartXPositionStart ,yPosition), Point(xSize, yPosition + heightPerLine))
            r.setFill("yellow")
            chartLines.append(r)
            r.draw(statsWindow)

            # Show the average pegs next to the chart 
            tAvg = Text(Point(averagePosition, yPosition + textYPadding), str(round(averagePegs,2)))
            tAvg.setSize(10)
            tAvg.draw(statsWindow)

            # Move y down to where next line would go
            yPosition = yPosition + heightPerLine + paddingPerLine

from ctypes import pointer
from graphics import *
import random

class Statistics:
    def __init__(self):
        self.pegsLeftByStarintgPosition = []
        self.numberGamesPlayednStartingPosition = []

        for loop in range(1, 18):
            self.pegsLeftByStarintgPosition.append(0)
            self.numberGamesPlayednStartingPosition.append(0)

    def addResult(self, startingPosition, pegsLeft, showChart):
        # Make sure this is a number
        startingPosition = int(startingPosition)

        self.pegsLeftByStarintgPosition[startingPosition] = self.pegsLeftByStarintgPosition[startingPosition] + pegsLeft
        self.numberGamesPlayednStartingPosition[startingPosition] = self.numberGamesPlayednStartingPosition[startingPosition] + 1

        if (showChart == True) :
            self.drawChart()

    def drawChart(self):
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

        statsWindow = GraphWin("Average Pegs Left Based on Starting Position", windowHeight, windowWidth)
        statsWindow.setBackground("gray")

        # Calculate height of each graph line, 15 lines and 10 pixels between each line
        heightPerLine = ((windowHeight-startYPosition) / 15) - paddingPerLine

        chartLabels = []
        chartLines = []
        chartPegLabels = []

        yPosition = startYPosition
        
        for loop in range(1, 16):
            # Text
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

            r = Rectangle(Point(chartXPositionStart ,yPosition), Point(xSize, yPosition + heightPerLine))
            r.setFill("yellow")
            chartLines.append(r)

            tAvg = Text(Point(averagePosition, yPosition + textYPadding), str(round(averagePegs,2)))
            tAvg.setSize(10)
            tAvg.draw(statsWindow)

            r.draw(statsWindow)

            # Move y down to where next line would go
            yPosition = yPosition + heightPerLine + paddingPerLine

from graphics import *


class Button:
    def __init__(self, text, p1, p2, color, linecolor, txtcolor, txtsize, win):
        self.p1 = p1
        self.p2 = p2
        self.win = win
        self.valuelist = []
        self.x = (p1.getX() + p2.getX()) / 2
        self.y = (p1.getY() + p2.getY()) / 2
        self.box = Rectangle(p1, p2)
        self.box.setFill(color)
        self.box.setOutline(linecolor)
        self.title = Text(Point(self.x, self.y), text)
        self.title.setFill(txtcolor)
        self.title.setSize(txtsize)
        self.box.draw(win)
        self.title.draw(win)

    def getCenter(self):
        return Point(self.x, self.y)

    def click(self):
        press = self.win.getMouse()
        if self.p2.getX() > press.getX() > self.p1.getX():
            if self.p2.getY() > press.getY() > self.p1.getY():
                pressvalue = True
                self.valuelist.append("True")
            else:
                pressvalue = False
                self.valuelist.append("False")
        else:
            pressvalue = False
            self.valuelist.append("False")
        return pressvalue

    def movingClick(self, clicks):
        a = self.x
        b = self.y
        end = 0
        while end < clicks:
            new = self.win.getMouse()
            x = new.getX()
            y = new.getY()
            self.box.move(x - a, y - b)
            self.title.move(x - a, y - b)
            a = x
            b = y
            end = end + 1

    def move(self, dx, dy):
        self.box.move(dx, dy)
        self.title.move(dx, dy)

    def undraw(self):
        self.box.undraw()
        self.title.undraw()

    def resetColor(self, newcolor):
        self.box.undraw()
        self.title.undraw()
        self.box.setFill(newcolor)
        self.box.draw(self.win)
        self.title.draw(self.win)

    def resetLinecolor(self, newlinecolor):
        self.box.undraw()
        self.title.undraw()
        self.box.setOutline(newlinecolor)
        self.box.draw(self.win)
        self.title.draw(self.win)

    def resetTextcolor(self, newtxtcolor):
        self.title.undraw()
        self.title.setFill(newtxtcolor)
        self.title.draw(self.win)

    def resetTextsize(self, newtxtsize):
        self.title.undraw()
        self.title.setSize(newtxtsize)
        self.title.draw(self.win)

    def getValues(self):
        return self.valuelist
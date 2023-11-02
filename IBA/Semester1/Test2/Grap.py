from graphics import *

def main():
    win=GraphWin("My Circle", 600, 600)
    c= Circle(Point(50,50), 10)
    center=Point(100,100)
    label = Text(center, "Hej Hej")
    label.draw(win)
    c.draw(win)
    win.getMouse()
    win.close
main()

# Module 5
#   Programming Assignment 6
#       Prob-3.py

# <Garrett>

from graphics import *

def main():
    win = GraphWin("Archery Target", 600,600)
    shape = Circle(Point(300,300), 250)
    shape.draw(win)
    
    shape2 = Circle(Point(300,300), 200)
    shape2.setFill("black")
    shape2.draw(win)

    shape3 = Circle(Point(300,300), 150)
    shape3.setOutline("blue")
    shape3.setFill("blue")
    shape3.draw(win)

    shape4 = Circle(Point(300,300), 100)
    shape4.setOutline("red")
    shape4.setFill("red")
    shape4.draw(win)

    shape5 = Circle(Point(300,300), 50)
    shape5.setOutline("yellow")
    shape5.setFill("yellow")
    shape5.draw(win)
    




    win.getMouse()

main()    
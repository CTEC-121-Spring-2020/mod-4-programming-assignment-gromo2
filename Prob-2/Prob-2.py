# Module 5
#   Programming Assignment 6
#       Prob-2.py

# <Garrett>

from graphics import *

def main():
     win = GraphWin()

     # Draw Square
     shape = Rectangle(Point(50,50), Point(100,100))
     shape.setOutline("red")
     shape.setFill("red")
     shape.draw(win)
     
     # Establish Controls
     for i in range(5):
          p = win.getMouse()
          c = shape.getCenter()
          dx = p.getX() - c.getX()
          dy = p.getY() - c.getY()
          shape.move(dx,dy)
     
     # Set Exit Conditions
     Text(Point(75,175), "Click again to quit.").draw(win)
     win.getMouse()
     win.close()

main()
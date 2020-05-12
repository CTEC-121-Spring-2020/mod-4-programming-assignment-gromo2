# Module 5
#   Programming Assignment 6
#       Prob-1.py

# <Garrett>

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does

# imports code from the graphics library; allows for use of objects and functions from it
from graphics import *

# Defines main
def main():
     # Defines the graphics window as a variable
     win = GraphWin()
     # Defines a circle at the point (50,50), radius 20, under the variable "Shape"
     shape = Circle(Point(50,50), 20)
     # Sets the outline of the circle (variable 'shape') to red
     shape.setOutline("red")
     # Sets the fill of the circle to red
     shape.setFill("red")
     # Tells python to draw the shape with the previously defined parameters, in the window 
     shape.draw(win)
     #Sets a for loop in a range of 5 times. Executes the code in the indent underneath
     for i in range(5):
          # Sets variable p to search for user input via mouse clicks
          p = win.getMouse()
          # Sets variable c to check for what the center point of the shape is (In this case, (50,50))
          c = shape.getCenter()
          # Sets variable dx to subtract the x coordinate of the center from the x coordinate of the mouse input point
          dx = p.getX() - c.getX()
          # Sets variable dy to subtract the y coordinate of the center from the y coordinate of the mouse input point
          dy = p.getY() - c.getY()
          # Moves the shape based on the previously determined mouse input
          shape.move(dx,dy)
     # Closes the graphics window
     win.close()
# Calls back to main
main()
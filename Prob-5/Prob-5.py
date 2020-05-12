# Module 5
#   Programming Assignment 6
#       Prob-5.py

# <Garrett>

from graphics import *
def main():
    win = GraphWin("Car Drawing", 300, 300)

    

    # Main Body
    body = Rectangle(Point(50, 100), Point(250, 125))
    body.setFill("purple")
    body.setOutline("purple")
    body.draw(win)

    roof = Polygon(Point(50, 100), Point(110, 50), Point(150, 50), Point(250, 100))
    roof.setOutline("purple")
    roof.setFill("purple")
    roof.draw(win)

    # Windows
    window = Polygon(Point(140,70), Point(170, 70), Point(215, 90), Point(140, 90))
    window.setOutline("light blue")
    window.setFill("light blue")
    window.draw(win)

    window2 = Polygon(Point(130, 70), Point(130, 70), Point(85, 90), Point(130,90))
    window2.setOutline("light blue")
    window2.setFill("light blue")
    window2.draw(win)

    # Antenna
    antenna = Line(Point(230, 90), Point(230, 50))
    antenna.draw(win)
    antennaTopper = Circle(Point(230, 50), 3)
    antennaTopper.setFill("gray")
    antennaTopper.draw(win)

    # Wheels
    wheel1 = Circle(Point(200, 125),25)
    wheel1.setFill("dark gray")
    wheel1.draw(win)

    wheel2 = Circle(Point(100, 125),25)
    wheel2.setFill("dark gray")
    wheel2.draw(win)

    # Bumpers
    frontBumper = Polygon(Point(250, 100), Point(250, 125), Point(260, 125))
    frontBumper.setOutline("dark gray")
    frontBumper.setFill("silver")
    frontBumper.draw(win)

    backBumper = Polygon(Point(50, 100), Point(50, 125), Point(40, 125))
    backBumper.setOutline("dark gray")
    backBumper.setFill("dark gray")
    backBumper.draw(win)

    win.getMouse()
    


main()
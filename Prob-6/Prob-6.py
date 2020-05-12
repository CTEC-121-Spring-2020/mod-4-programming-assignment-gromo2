# Module 5
#   Programming Assignment 6
#       Prob-6.py

# <Garrett>

from graphics import *
def main():
    win = GraphWin("LEGO Bricks", 500, 500)
    
    # Dark Blue LEGO
    LEGO = Rectangle(Point(50, 50), Point(200, 100))
    LEGO.setWidth(2)
    LEGO.setFill("dark blue")
    stud = Rectangle(Point(56,50), Point(75,45))
    stud.setWidth(2)
    stud.setFill("dark blue")
    for i in range(5):
        P1 = stud.getP1()
        P1x = P1.getX()
        if P1x > 30:
            stud2 = stud.clone()
            stud2.move(30*i,0)
            stud2.draw(win)

    # Dark Green LEGO
    LEGO2 = LEGO.clone()
    LEGO2.move(200,0)
    LEGO2.setFill("Dark Green")
    for i in range(5):
        P1 = stud.getP1()
        P1x = P1.getX()
        if P1x > 30:
            stud2 = stud.clone()
            stud2.move(200,0)
            stud2.move(30*i,0)
            stud2.setFill("dark green")
            stud2.draw(win)
    LEGO2.draw(win)

    # Yellow LEGO
    LEGO3 = LEGO.clone()
    LEGO3.move(0, 100)
    LEGO3.setFill("Yellow")
    for i in range(5):
        P1 = stud.getP1()
        P1x = P1.getX()
        if P1x > 30:
            stud2 = stud.clone()
            stud2.move(0, 100)
            stud2.move(30*i,0)
            stud2.setFill("yellow")
            stud2.draw(win)
    LEGO3.draw(win)

    # Red LEGO
    LEGO4 = LEGO.clone()
    LEGO4.move(200, 100)
    LEGO4.setFill("Red")
    for i in range(5):
        P1 = stud.getP1()
        P1x = P1.getX()
        if P1x > 30:
            stud2 = stud.clone()
            stud2.move(200, 100)
            stud2.move(30*i,0)
            stud2.setFill("Red")
            stud2.draw(win)
    LEGO4.draw(win)

    # Cyan/Light Blue? LEGO
    LEGO5 = LEGO.clone()
    LEGO5.move(0, 200)
    LEGO5.setFill("Cyan")
    for i in range(5):
        P1 = stud.getP1()
        P1x = P1.getX()
        if P1x > 30:
            stud2 = stud.clone()
            stud2.move(0, 200)
            stud2.move(30*i,0)
            stud2.setFill("Cyan")
            stud2.draw(win)
    LEGO5.draw(win)

    # Black LEGO

    LEGO6 = LEGO.clone()
    LEGO6.move(200, 200)
    LEGO6.setFill("Black")
    for i in range(5):
        P1 = stud.getP1()
        P1x = P1.getX()
        if P1x > 30:
            stud2 = stud.clone()
            stud2.move(200, 200)
            stud2.move(30*i,0)
            stud2.setFill("Black")
            stud2.draw(win)
    LEGO6.draw(win)

    stud.draw(win)
    LEGO.draw(win)


    win.getMouse()


main()
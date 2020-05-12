# Module 5
#   Programming Assignment 6
#       Prob-7.py

# <Garrett>

from graphics import *
def main():
    win = GraphWin("Weird Shape Face", 500, 500)
    
    # Ears
    leftEar = Circle(Point(100,240),30)
    leftEar.setFill("light yellow")
    rightEar = leftEar.clone()
    rightEar.move(300,0)
    rightEar.draw(win)
    leftEar.draw(win)
    
    # Head
    head = Circle(Point(250,250), 150)
    head.setFill("light yellow")
    head.draw(win)

    # Eyes
    leftEye = Circle(Point(200, 215),25)
    leftEye.setFill("white")
    leftPupil = Circle(Point(200,215),8)
    leftPupil.setFill("Black")
    leftIris = Circle(Point(200,215), 15)
    leftIris.setFill("dark green")
    rightIris = leftIris.clone()
    rightIris.move(100,0)
    rightPupil = leftPupil.clone()
    rightPupil.move(100,0)
    rightEye = leftEye.clone()
    rightEye.move(100, 0)
    rightEye.draw(win)
    leftEye.draw(win)
    rightIris.draw(win)
    leftIris.draw(win)
    leftPupil.draw(win)
    rightPupil.draw(win)

    # Hair
    hair = Polygon(Point(100, 185), Point(160, 90), Point(350, 90), Point(400, 185))
    hair.setFill("brown")
    hair.setOutline("brown")
    hair.draw(win)

    # Nose
    nose = Circle(Point(250, 250), 20)
    nose.setOutline("brown")
    nose.draw(win)

    # Mouth
    mouth = Polygon(Point(215, 300), Point(280, 300), Point(270, 330), Point(230, 330))
    mouth.draw(win)
    tooth1 = Rectangle(Point(230, 300), Point(245, 310))
    tooth1.setFill("white")
    tooth1.draw(win)
    tooth2 = tooth1.clone()
    tooth2.move(20,0)
    tooth2.draw(win)
    win.getMouse()


main()
# Module 5
#   Programming Assignment 6
#       Prob-4.py

# <Garrett>

from graphics import *
def main():
    win = GraphWin("Five-Click House",500,500)
    

    # Draw main body of house
    h1 = win.getMouse()
    h2 = win.getMouse()
    house = Rectangle(h1, h2)
    house.draw(win)
    
    # Draw the door of the house
    d0 = win.getMouse()
    if h2.getX() > h1.getX():
        dx1 = d0.getX() - (((h2.getX()-h1.getX())/10))
        dx2 = d0.getX() + (((h2.getX()-h1.getX())/10))
    else:
        dx1 = d0.getX() - (((h1.getX()-h2.getX())/10))
        dx2 = d0.getX() + (((h1.getX()-h2.getX())/10))
    
    if h2.getY() > h1.getY():
        dy = h2.getY()
    else:
        dy = h1.getY()
    d1 = Point(dx1, d0.getY())
    d2 = Point(dx2, dy)
    door = Rectangle(d1, d2)
    door.draw(win)
    
    # Draw the window of the house
    w0 = win.getMouse()
    if dx2 > dx1:
        wx1 = w0.getX() - ((dx2 - dx1)/4)
        wx2 = w0.getX() + ((dx2 - dx1)/4)
    else:
        wx1 = w0.getX() - ((dx1 - dx2)/4)
        wx2 = w0.getX() + ((dx1 - dx2)/4)
    
    wy1 = w0.getY() + ((dx2 - dx1)/4)
    wy2 = w0.getY() - ((dx2 - dx1)/4)

    w1 = Point(wx1, wy1)
    w2 = Point(wx2, wy2)
    

    w1 = Point(wx1, wy1)
    w2 = Point(wx2, wy2)
    window = Rectangle(w1, w2)
    window.draw(win)
    
    # Draw the roof

    r0 = win.getMouse()
    l1 = Point(h1.getX(), h1.getY())
    l2 = Point(r0.getX(), r0.getY())
    l3 = Point(h2.getX(), h1.getY())
    l4 = Point(r0.getX(), r0.getY())
    roof1 = Line(l1, l2)
    roof2 = Line(l3, l4)
    roof1.draw(win)
    roof2.draw(win)

    # Set Exit Conditions
    Text(Point(175,475), "House complete! Click again to exit.").draw(win)
    win.getMouse()

main()
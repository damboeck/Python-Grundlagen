'''
Created on 23.11.2011

@author: maxi
'''
from graphics import *

def main():
    win = GraphWin("My Circle", 500, 500)
    c = Circle(Point(250,250), 170)
    c.draw(win)    
    win.getMouse() # pause for click in window
    win.close()

main()

from graphics import *
from math import sin,cos
from time import sleep
from random import randint
win=GraphWin("test",500,500)

r=100
th=0
cx,cy=randint(10,490),randint(10,490)
temp=0.0

while 1:
    x=r*cos(th)
    y=r*sin(th)
    p1=Point(x+randint(10,490),y+randint(10,490))
    p2=Point(x+randint(10,490),y+randint(10,490))
    
    temp=p2

    l=Line(p1,p2)
    l.draw(win)
    th+=1
    r-=1
    cx,cy=randint(10,490),randint(10,490)

    sleep(.1)
    



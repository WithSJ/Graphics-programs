from graphics import *
from time import sleep
from random import randint

winsize=[1000,600]
win=GraphWin("Test",winsize[0],winsize[1])
# for i in range(100):

#     posx=randint(0,winsize[0]) 
#     posy=randint(0,winsize[1]) 

#     cir=Circle(Point(posx,posy),randint(5,50))
#     r =randint(0,255)
#     g =randint(0,255)
#     b =randint(0,255)
#     cir.setFill(color_rgb(r,g,b))
# #    cir.setOutline(color_rgb(r,g,b))
#     cir.draw(win)
#     sleep(.33)
#     cir.move(posx+randint(10,100),posy+randint(10,60) )
    
#     sleep(.01)

pt=0
cir=Circle(Point(pt,pt),50)
cir.draw(win)
cir.setFill(color_rgb(randint(0,255),randint(0,255),randint(0,255)))
for i in range(400):
    inc=1
    
    cir.move(pt+inc,pt+inc)
    sleep(.06)
    inc+=1










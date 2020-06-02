from graphics import *
from time import sleep
from math import cos,sin
win=GraphWin("Circle",500,500)

r=100
hk=[250,250]
i=1
Cend=3-2*r
Csrt=0
Clist=[]


while abs(Cend)*2>Csrt:
    x=r*cos(Csrt)
    y=r*sin(Csrt)

    Clist.append([x+hk[0],y+hk[1]])
    Csrt+=i


Clist.sort()

print("-"*30)
print(Clist)


first=[]
sec=[]
third=[]
fourth=[]
for i in Clist:
    if i[0]>=hk[0] and i[1]<=hk[1]:
        first.append(i)
    if i[0]>=hk[0] and i[1]>=hk[1]:
        sec.append(i)
    if i[0]<=hk[0] and i[1]>=hk[1]:
        third.append(i)
    if i[0]<=hk[0] and i[1]<=hk[1]:
        fourth.append(i)


sec.reverse()
third.reverse()

print("-"*30+"First"+"-"*30)
print(first)

print("-"*30+"Sec"+"-"*30)
print(sec)

print("-"*30+"Third"+"-"*30)
print(third)

print("-"*30+"Fouth"+"-"*30)
print(fourth)

mergeC=first+sec+third+fourth
cir=Circle(Point(250,250),100)
cir.draw(win)

obj=Circle(Point(0,0),10)
obj.setFill(color_rgb(255,0,0))
obj.draw(win)

# for i in mergeC:
#     pt=Point(i[0],i[1])
#     pt.draw(win)
#     sleep(.05)
last=[0,0]
while 1:

    for i in mergeC:
        obj.move(i[0]-last[0],i[1]-last[1])
        last[0]=i[0]
        last[1]=i[1]
        sleep(.01)

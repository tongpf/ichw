import turtle
import math

def firststep(p,a,b):
    a = a*5.0
    b = b*5.0
    c = a - math.sqrt(a**2-b**2)
    p.shape("circle")
    p.pensize(3)
    p.penup()
    p.forward(c)
    p.left(90)
    p.pendown()

def drawcircle(p,sz):
    sz = sz * 5.0
    d = 2 * math.pi * sz
    p.forward((d/360)*(400.0/(sz+1)))
    p.left(400.0/(sz+1))

def drawellipse(p,a,b,rad):
    a = a*5.0
    b = b*5.0
    rad = (math.pi * rad / 180.0)*(400.0/(a+1))
    x=a*math.cos(rad) - math.sqrt(a**2-b**2)
    y=b*math.sin(rad)
    p.goto(x,y)

wn = turtle.Screen()
Sun = turtle.Turtle()
Sun.color("orange")
Mer = turtle.Turtle()
Mer.color("purple")
Ven = turtle.Turtle()
Ven.color("yellow")
Ear = turtle.Turtle()
Ear.color("blue")
Mar = turtle.Turtle()
Mar.color("red")
Jup = turtle.Turtle()
Jup.color("gray")
Sat = turtle.Turtle()
Sat.color("brown")

firststep(Sun,0,0)
firststep(Mer,8,8)
firststep(Ven,12,12)
firststep(Ear,16,16)
firststep(Mar,23,22.5)
firststep(Jup,60,55)
firststep(Sat,80,70)
for i in range(3600):
    drawellipse(Sun,0,0,i+1)
    drawellipse(Mer,8,8,i+1)
    drawellipse(Ven,12,12,i+1)
    drawellipse(Ear,16,16,i+1)
    drawellipse(Mar,23,22.5,i+1)
    drawellipse(Jup,60,55,i+1)
    drawellipse(Sat,80,70,i+1)
wn.exitonclick()

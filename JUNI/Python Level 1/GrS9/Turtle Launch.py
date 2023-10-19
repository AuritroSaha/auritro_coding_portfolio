import turtle
import random

t = turtle.Turtle()
t.speed(100)
u = turtle.Screen()

u.bgcolor("black")


def drawEarth():
    t.goto(-200,100)
    t.begin_fill()
    t.color("blue")
    t.circle(100)
    t.end_fill()
drawEarth()

def drawMoon():
    t.penup()
    t.goto(200,150)
    t.pendown()
    t.begin_fill()
    t.color("gray")
    t.circle(50)
    t.end_fill()
drawMoon()

t.ht()

def launchTurtle():
    y = turtle.Turtle()
    y.shape("turtle")
    y.penup()
    y.color("red")
    y.ht()
    y.goto(-200,200)
    y.st()
    x = random.randint(370,430)
    y.forward(x)
    if x>400:
        y.color("white")
    else:
        y.color("red")

u.onkey(launchTurtle, "space")

u.listen()
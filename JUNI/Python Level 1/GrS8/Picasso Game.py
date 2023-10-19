import turtle
import random

colors = ["red", "green", "blue", "black", "magenta"]

t = turtle.Turtle()

screen = turtle.Screen()

t.goto(0,0)

def drawSquare():
    sideLength = random.randint(50,100)
    color = random.choice(colors)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.color(color)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(sideLength)
        t.right(90)
    t.end_fill()
screen.onkey(drawSquare, "Up")


def drawTriangle():
    sideLength = random.randint(50,100)
    color = random.choice(colors)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.color(color)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(3):
        t.forward(sideLength)
        t.right(120)
    t.end_fill()
screen.onkey(drawTriangle, "Down")


def drawOctogon():
    sideLength = random.randint(50,100)
    color = random.choice(colors)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.color(color)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(8):
        t.forward(sideLength)
        t.right(45)
    t.end_fill()
screen.onkey(drawOctogon, "Left")


def drawPentagon():
    sideLength = random.randint(50,100)
    color = random.choice(colors)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.color(color)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(5):
        t.forward(sideLength)
        t.right(72)
    t.end_fill()
screen.onkey(drawPentagon, "Right")

screen.listen()
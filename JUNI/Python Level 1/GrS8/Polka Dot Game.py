import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()


t.penup()

t.goto(0,0)

def forward():
    t.forward(2)

screen.onkey(forward, "Up")

def backward():
    t.backward(2)

screen.onkey(backward, "Down")

def left():
    t.left(3)

screen.onkey(left, "Left")

def right():
    t.right(3)

screen.onkey(right, "Right")

def drawPolkaDot():
    t.pendown()
    colors = ["red", "green", "blue", "black", "magenta"]
    color = random.choice(colors)
    x = random.randint(50,100)
    t.color(color)
    t.begin_fill()
    t.circle(x)
    t.end_fill()
    t.penup()

screen.onkey(drawPolkaDot, "Space")

screen.listen()
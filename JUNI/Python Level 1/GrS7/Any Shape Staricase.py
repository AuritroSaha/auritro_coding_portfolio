import turtle
import random

t = turtle.Turtle()
t.speed(100)

numOfSides = random.randint(3,8)

def drawLine(sideLength):
    t.forward(sideLength)

colors = ["red","green","blue","orange","purple","pink","yellow"]
#colors = ["black"]

def drawShape(sideLength, numSides):
    for i in range(100):
        color = random.choice(colors)
        t.color(color)
        for i in range(numSides):
            drawLine(sideLength)
            t.right(360/numSides)
        t.right(10)
        sideLength = sideLength + 2

drawShape(50,numOfSides)
import turtle
import random

t = turtle.Turtle()
t.speed(100)

colors = ["red", "green", "blue", "purple", "orange", "magenta", "teal"]


def drawBranch(branchLength, sideBranchLength):
    t.speed(100)
    t.pensize(5)
    for i in range(branchLength):
        t.forward(sideBranchLength)
        t.left(45)
        t.forward(sideBranchLength)
        t.backward(sideBranchLength)
        t.right(90)
        t.forward(sideBranchLength)
        t.backward(sideBranchLength)
        t.left(45)


def drawSnowFlake(numBranches, branchLength, sideBranchLength):
    t.speed(100)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(numBranches):
        drawBranch(branchLength, sideBranchLength)
        t.backward(branchLength * sideBranchLength)
        t.right(360 / numBranches)


def snowing():
    t.speed(100)
    while True:
        color = random.choice(colors)
        t.color(color)
        numBranches = random.randint(5, 8)
        branchLength = random.randint(3, 6)
        sideBranchLength = random.randint(5, 15)

        drawSnowFlake(numBranches, branchLength, sideBranchLength)


snowing()


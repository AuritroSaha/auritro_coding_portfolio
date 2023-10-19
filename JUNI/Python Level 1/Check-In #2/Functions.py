import turtle

t = turtle.Turtle()

def moveForwardFive():
    t.forward(5)

def drawSquare(x):
    for i in range(4):
        t.forward(x)
        t.right(90)
moveForwardFive()
drawSquare(50)
t.ht()
t.st()

x = 10

for i in range(15):
    drawSquare(x)
    x = x + 5


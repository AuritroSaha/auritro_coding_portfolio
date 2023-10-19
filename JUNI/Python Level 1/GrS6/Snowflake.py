import turtle

t = turtle.Turtle()
t.speed(50)


def drawLine(sideLength):
    t.forward(sideLength)


def drawBranch():
    t.color("blue")
    t.pensize(5)
    for i in range(6):
        t.forward(10)
        t.left(45)
        t.forward(10)
        t.backward(10)
        t.right(90)
        t.forward(10)
        t.backward(10)
        t.left(45)


def drawSnowFlake():
    for i in range(6):
        drawBranch()
        t.backward(60)
        t.right(60)


drawSnowFlake()
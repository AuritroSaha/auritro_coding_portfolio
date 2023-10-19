import turtle

t = turtle.Turtle()
t.speed(100)


def drawLine(lineLength):
    t.forward(lineLength)


# length = 100
# drawLine(length)

length = 20


def drawSquare(sideLength):
    for i in range(4):
        drawLine(sideLength)
        t.right(90)


for i in range(10):
    drawSquare(length)
    length = length + 5


def drawTriangle(sideLength):
    t.color("magenta")
    t.begin_fill()
    for i in range(3):
        drawLine(sideLength)
        t.right(120)
    t.end_fill()


drawTriangle(length)

# square: 360 / 4 = 90
# triangle: 360 / 3 = 120
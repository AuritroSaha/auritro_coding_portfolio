import turtle

t = turtle.Turtle()
t.speed(100)
t.ht()


def drawLine(lineLength):
    t.forward(lineLength)


length = 3


def drawTriangle(sideLength):
    for i in range(3):
        drawLine(sideLength)
        t.right(120)


t.left(90)
t.penup()
t.forward(200)
t.right(150)
t.pendown()
for i in range(100):
    drawTriangle(length)
    length = length + 5
t.left(60)
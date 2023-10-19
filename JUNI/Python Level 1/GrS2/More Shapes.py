import turtle

t = turtle.Turtle()
t.ht()

screen = turtle.Screen()
screen.bgcolor("black")
length = 150
length2 = 50
length3 = 300

def drawLine(sideLength):
    t.forward(sideLength)

def drawHexagon(sideLength):
    t.color("magenta")
    t.begin_fill()
    for i in range(6):
        drawLine(sideLength)
        t.right(60)
    t.end_fill()
drawHexagon(length)

t.penup()
t.forward(length)
t.left(90)
t.forward(250)
t.right(90)
t.pendown()

def drawDecagon(sideLength):
    t.color("purple")
    t.begin_fill()
    for i in range(10):
        drawLine(sideLength)
        t.right(36)
    t.end_fill()
drawDecagon(length2)

t.penup()
t.left(180)
t.forward(450)
t.left(90)
t.forward(100)
t.left(90)
t.pendown()

def drawStar(sideLength):
    t.color("teal")
    t.begin_fill()
    for i in range(5):
        drawLine(sideLength)
        t.right(144)
    t.end_fill()
drawStar(length3)

# to draw a shape: amount to turn = 360 / numSides
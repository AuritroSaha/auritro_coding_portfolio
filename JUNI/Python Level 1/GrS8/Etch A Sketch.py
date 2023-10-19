import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.goto(0, 0)


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


def pensizeup1():
    size = 0
    t.pensize(size + 3)


screen.onkey(pensizeup1, "z")


def pensizeup2():
    size = 0
    t.pensize(size + 6)


screen.onkey(pensizeup2, "a")


def pensizedown1():
    t.pensize(1)


screen.onkey(pensizedown1, "x")


def pensizedown2():
    size = 6
    t.pensize(size - 3)


screen.onkey(pensizedown2, "s")


def penup_pendown():
    if t.isdown():
        t.penup()
    else:
        t.pendown()


screen.onkey(penup_pendown, "Space")

screen.listen()
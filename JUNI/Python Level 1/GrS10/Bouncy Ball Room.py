import turtle, random

t = turtle.Turtle()
screen = turtle.Turtle()
screen.tracer(0)


def drawSquare():
    t.pensize(10)
    t.speed(100)
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    for i in range(4):
        t.forward(400)
        t.right(90)
    t.ht()


drawSquare()

turtles = []

for i in range(10):
    turtles.append(turtle.Turtle())

for t in turtles:
    t.speed(100)
    t.penup()
    q = random.randint(-195, 195)
    w = random.randint(-195, 195)
    t.goto(q, w)
    t.shape("circle")
    x = random.randint(1, 360)
    t.color("red")
    t.right(x)

m = range(-200, 200)


def checkCollision(ball):
    if ball.xcor() < -195 or ball.xcor() > 195 or ball.ycor() < -195 or ball.ycor() > 195:
        ball.right(180)


while True:
    for t in turtles:
        t.speed(10)
        checkCollision(t)
        t.forward(5)
    screen.update()
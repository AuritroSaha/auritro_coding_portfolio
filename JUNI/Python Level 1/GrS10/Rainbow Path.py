import random, turtle

t = turtle.Turtle()
t2 = turtle.Turtle()

t2.speed(1000)

colors = ["red", "blue", "green", "cyan", "purple", "pink", "yellow", "brown", "magenta"]

t.penup()
t.goto(-300, 0)
t.pendown()


def drawBox():
    t2.penup()
    t2.goto(-300, 300)
    t2.pendown()
    for i in range(4):
        t2.forward(600)
        t2.right(90)
    t2.ht()
    t2.penup()
    t2.goto(0, 20)


drawBox()

while True:
    color = random.choice(colors)
    turn = random.randint(-10, 10)
    go = random.randint(5, 10)
    t.color(color)
    t.right(turn)
    t.forward(go)
    if t.xcor() < -300 or t.ycor() > 300 or t.xcor() > 300 or t.ycor() < -300:
        t2.write("Out of Bounds!")
        break

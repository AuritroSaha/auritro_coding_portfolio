import turtle, random

t = turtle.Turtle()
t2 = turtle.Turtle()
screen = turtle.Screen()

x = random.randint(-200, 200)
y = random.randint(-200, 200)

x2 = random.randint(-200, 200)
y2 = random.randint(-200, 200)

t.penup()
t2.penup()
t.goto(x, y)
t2.goto(x2, y2)
t.color("green")
t2.color("red")
t.pendown()
t2.pendown()

def t_right():
    t.right(4)
screen.onkey("Right", t_right)

def t_left():
    t.left(4)
screen.onkey("Left", t_left)

def t2_right():
    t2.right(4)
screen.onkey("d", t2_right)

def t2_left():
    t2.left(4)
screen.onkey("a", t2_left)

screen.listen()

def check_collision():
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    r2 = random.randint(0, 256)
    g2 = random.randint(0, 256)
    b2 = random.randint(0, 256)
    if abs(t.xcor() - t2.xcor()) < abs(10) and abs(t.ycor() - t2.ycor()) < abs(10):
        t.color(r, g, b)
        t2.color(r2, g2, b2)
        t.write("Collision!")
        t2.write("Collision!")

while True:
    t.forward(1)
    t2.forward(1)
    check_collision()
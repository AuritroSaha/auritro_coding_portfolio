import turtle, random

t = turtle.Turtle()
t3 = turtle.Screen()

num_markStarCalled = 0

t.penup()
t.shape("turtle")
t.color("white")

r = 195

g = []

for i in range(10):  # Creates a list: [0, 1, 2,... 9]
    t2 = turtle.Turtle()
    t2.speed(100)
    t2.shape("circle")
    t2.color("White")
    g.append(t2)

for i in g:  # g: [Turtle1, Turtle2, ...]
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    i.penup()
    i.goto(x, y)


def t_right():
    t.right(5)


t3.onkey(t_right, "Right")


def t_left():
    t.left(5)


t3.onkey(t_left, "Left")

t3.listen()


def makeStar(x):
    x.begin_fill()
    for i in range(5):
        x.pendown()
        x.color("yellow")
        x.ht()
        x.forward(18)
        x.right(144)
        x.penup()
    x.end_fill()


def collision():
    m = 0
    for x in g:
        if abs(x.xcor() - t.xcor()) < 8 and abs(x.ycor() - t.ycor()) < 8:
            m = m + 1
            makeStar(x)
            x.goto(-200, -200)
    return m


while True:
    t3.bgcolor(r, 20, 50)
    t.forward(1)
    m = collision()
    num_markStarCalled = num_markStarCalled + m
    r = r - 0.1
    if r <= 30:
        t.ht()
        t.write("Times up! Game Over!", font=("Arial", 18, "normal"))
        break
    elif num_markStarCalled == 10:
        t.ht()
        t.write("Great Job! You've won!", font=("Arial", 18, "normal"))
        break


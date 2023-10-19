import turtle, random

t = turtle.Turtle()
s = turtle.Screen()

colors = ["red", "green", "blue", "purple", "yellow", "cyan", "orange", "brown"]  # can add more colors if you want to

t.speed(10)

col = random.choice(colors)
s.bgcolor(col)
colors.remove(col)


def bowtie(length, colors):
    col = random.choice(colors)
    t.color(col)
    colors.remove(col)
    t.pendown()
    t.left(30)

    t.begin_fill()

    for i in range(3):
        t.forward(length)
        t.right(120)

    t.end_fill()

    t.left(180)
    t.color(random.choice(colors))

    t.begin_fill()

    for i in range(3):
        t.forward(length)
        t.right(120)

    t.end_fill()

    t.ht()


bowtie(100, colors)
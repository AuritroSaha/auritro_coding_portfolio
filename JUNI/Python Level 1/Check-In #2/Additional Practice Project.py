import turtle, random

radius = 10
flag = 1
spin = True
t = turtle.Turtle()
t2 = turtle.Turtle()
screen = turtle.Screen()

t.shape("turtle")
t.color("blue")

x = random.randint(-300, 300)
y = random.randint(-300, 300)

t2.penup()
t2.color("red")
t2.shape("circle")
t2.goto(x, y)


def collision():
    if x - radius < t.xcor() < x + radius and y - radius < t.ycor() < y + radius:
        print("You won!")
        return True
    else:
        return False


def shoot():
    global spin
    spin = False
    while True:
        t.forward(1)
        t.speed(1000)
        if collision():
            break


screen.onkey(shoot, "Up")
screen.listen()

while spin:
    t.left(1)
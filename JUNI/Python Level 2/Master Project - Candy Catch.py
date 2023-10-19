#                                          Candy Catch

# bringing in all libraries needed
import turtle
import random
import time

# make turtles
tm = turtle.Turtle()
tb = turtle.Turtle()
ts = turtle.Turtle()
ts2 = turtle.Turtle()
ts3 = turtle.Turtle()
tm2 = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(0)

ts3.penup()
ts3.goto(-800, 800)
ts3.color("white")

# background color
screen.bgcolor("black")

# color lists
colorsTM = ["white", "orange"]
colorsTM2 = ["purple", "yellow"]

screen.register_shape("ghost", ((2, 24), (10, 20), (11, 19), (11, 5), (8, 5), (8, 14), (4, 14), (4, 5), (1, 5), (1, 14),
                                (-1, 14), (-1, 5), (-4, 5), (-4, 14), (-8, 14), (-8, 5), (-11, 5), (-11, 19), (-10, 20),
                                (-2, 24)))

tm.penup()
tm.shape("ghost")

tm2.penup()
tm2.shape("ghost")

# candy list
turtles = []

# make candies
for i in range(10):
    turtles.append(turtle.Turtle())

# place the candies
screen.register_shape("candy", ((5, 10), (5, -10), (0, -10), (4, -15), (-4, -15), (0, -10), (-5, -10), (-5, 10), (0, 10)
                                , (-4, 15), (4, 15), (0, 10), (5, 10)))

for t in turtles:
    t.penup()
    q = random.randint(-195, 195)
    w = random.randint(-195, 195)
    t.goto(q, w)
    t.shape("candy")
    x = random.randint(1, 360)
    t.color("red")
    t.right(x)

m = range(-200, 200)


# candy wall collision
def checkCollision(candy):
    if candy.xcor() < -195 or candy.xcor() > 195 or candy.ycor() < -195 or candy.ycor() > 195:
        candy.right(180)


# box/walls
def draw_box():
    tb.color("red")
    tb.speed(100)
    tb.penup()
    tb.goto(-200, 200)
    tb.pendown()
    for i in range(4):
        tb.forward(400)
        tb.right(90)
    tb.ht()


draw_box()


# Ghost wall collision
def check_collisionTM():
    if tm.xcor() < -200 or tm.ycor() > 200 or tm.xcor() > 200 or tm.ycor() < -200:
        tm.right(180)


def check_collisionTM2():
    if tm2.xcor() < -200 or tm2.ycor() > 200 or tm2.xcor() > 200 or tm2.ycor() < -200:
        tm2.right(180)


# controls
def left():
    tm.left(5)


screen.onkey(left, "Left")


def right():
    tm.right(5)


screen.onkey(right, "Right")


def right2():
    tm2.right(5)


screen.onkey(right2, "d")


def left2():
    tm2.left(5)


screen.onkey(left2, "a")

screen.listen()

# score counter
ts.ht()
ts.penup()
ts.goto(-200, 210)
ts.pendown()
ts.st()
ts.color("white")

ts2.ht()
ts2.penup()
ts2.goto(120, 210)
ts2.pendown()
ts2.st()
ts2.color("white")

# ghost/candy collisions
y = 0


def check_collisionBTM():
    q = random.randint(-195, 195)
    w = random.randint(-195, 195)
    x = random.randint(1, 360)
    for t in turtles:
        if abs(t.xcor() - tm.xcor()) < 12 and abs(t.ycor() - tm.ycor()) < 12:
            global y
            y = y + 1
            t.ht()
            t.goto(q, w)
            t.right(x)
            t.st()


y2 = 0


def check_collisionBTM2():
    q = random.randint(-195, 195)
    w = random.randint(-195, 195)
    x = random.randint(1, 360)
    for t in turtles:
        if abs(t.xcor() - tm2.xcor()) < 12 and abs(t.ycor() - tm2.ycor()) < 12:
            global y2
            y2 = y2 + 1
            t.ht()
            t.goto(q, w)
            t.right(x)
            t.st()


# win var
win = "P1 won!"
win2 = "P2 won!"
tied = "You Tied!"

# main loop for the game
while True:
    # player colors
    tm.color(random.choice(colorsTM))
    tm2.color(random.choice(colorsTM2))
    # score counter
    ts.clear()
    ts.write("P1 Score: " + str(y), font=("Times New Roman", 12, "normal"))

    ts2.clear()
    ts2.write("P2 Score: " + str(y2), font=("Times New Roman", 12, "normal"))

    tm.forward(2)
    check_collisionBTM()
    check_collisionTM()

    tm2.forward(2)
    check_collisionBTM2()
    check_collisionTM2()

    for t in turtles:
        t.speed(1)
        checkCollision(t)
        t.forward(1)

    screen.update()

    if y >= 0 or y2 >= 1:
        break

# win statements
if y > y2:
    ts.clear()
    ts.penup()
    ts.ht()
    ts.goto(-200, 220)
    ts.pendown()
    ts.write(win, font=("Times New Roman", 24, "normal"))
    ts2.ht()

elif y2 > y:
    ts2.clear()
    ts2.penup()
    ts2.ht()
    ts2.goto(120, 220)
    ts2.pendown()
    ts2.write(win2, font=("Times New Roman", 24, "normal"))
    ts.ht()

elif y == y2:
    ts3.goto(0, 220)
    ts3.pendown()
    ts3.write(tied, font=("Times New Roman", 24, "normal"))
    ts2.ht()
    ts.ht()

screen.update()

# win turtles
winner = turtle.Turtle()
winner2 = turtle.Turtle()
winner3 = turtle.Turtle()
winner4 = turtle.Turtle()
winner5 = turtle.Turtle()
winner6 = turtle.Turtle()
winner7 = turtle.Turtle()
winner8 = turtle.Turtle()

# win turtle colors
soup = ["green", "red", "blue", "white", "purple", "pink", "magenta", "orange"]

# win turtle setup
winner.penup()
winner2.penup()
winner3.penup()
winner4.penup()
winner5.penup()
winner6.penup()
winner7.penup()
winner8.penup()

winner.ht()
winner2.ht()
winner3.ht()
winner4.ht()
winner5.ht()
winner6.ht()
winner7.ht()
winner8.ht()

winner.goto(-500, 500)
winner2.goto(0, 500)
winner3.goto(500, 500)
winner4.goto(-500, 0)
winner5.goto(500, 0)
winner6.goto(-500, -500)
winner7.goto(0, -500)
winner8.goto(500, -500)

winner.right(45)
winner2.right(90)
winner3.right(135)
winner5.right(180)
winner6.left(45)
winner7.left(90)
winner8.left(135)

winner.st()
winner2.st()
winner3.st()
winner4.st()
winner5.st()
winner6.st()
winner7.st()
winner8.st()

p = 0

screen.tracer(10)

# win turtle loop
while False:
    for i in range(4):
        soups = random.choice(soup)
        winner.color(soups)
        winner2.color(soups)
        winner3.color(soups)
        winner4.color(soups)
        winner5.color(soups)
        winner6.color(soups)
        winner7.color(soups)
        winner8.color(soups)

        winner.forward(250)
        winner2.forward(250)
        winner3.forward(250)
        winner4.forward(250)
        winner5.forward(250)
        winner6.forward(250)
        winner7.forward(250)
        winner8.forward(250)

    winner.right(180)
    winner2.right(180)
    winner3.right(180)
    winner4.right(180)
    winner5.right(180)
    winner6.right(180)
    winner7.right(180)
    winner8.right(180)

    p = p + 1

    if p == 5:
        break

    screen.update()

# Ending Drawing
input("Step 1 hit a: ")
#screen = turtle.Screen()
#screen.clear()
screen.bgcolor("black")
screen.update()

pen = turtle.Turtle()
pen.ht()

# function to make pumpkin stub
def square(x, y, color):
    pen.penup()
    pen.goto(x, y)
    pen.begin_fill()
    pen.color(color)
    pen.pendown()
    for count2 in range(3):
        pen.forward(50)
        pen.left(90)
    pen.end_fill()


square(-20, 125, "brown")

screen.update()

input("Step 1 hit a: ")

# function to make pumpkin ball


def pumpkin():
    pen.penup()
    pen.goto(-125, -10)
    pen.pendown()
    pen.color("orange")
    pen.begin_fill()
    pen.circle(150)
    pen.end_fill()


pumpkin()

input("Step 1 hit p: ")

screen.update()

pen.penup()
pen.color("white")
pen.goto(-80, -10)


# pumpkin carving selection
if y > y2:
    pen.write("Amazing! P1 won", font=("Times New Roman", 24, "normal"))
elif y2 > y:
    pen.write("Amazing! P2 won", font=("Times New Roman", 24, "normal"))
elif y == y2:
    pen.write("Wow! It's a tie", font=("Times New Roman", 24, "normal"))

pen.penup()
pen.goto(-120, 200)
pen.write("Happy Halloween!", font=("Times New Roman", 34, "normal"))

screen.update()

time.sleep(10)

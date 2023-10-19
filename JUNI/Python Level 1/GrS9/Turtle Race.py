import turtle
import random

t = turtle.Turtle()
r = turtle.Turtle()
y = turtle.Turtle()
u = turtle.Turtle()
t.speed(100)

x = -40

for i in range(16):
    t.penup()
    t.goto(x,20)
    t.pendown()
    t.right(90)
    t.forward(99)
    t.backward(99)
    t.left(90)
    t.write(i)
    x = x+20
t.ht()

r.color("red")
r.shape("turtle")

y.color("blue")
y.shape("turtle")

u.color("orange")
u.shape("turtle")

r.penup()
y.penup()
u.penup()
r.goto(-40,-2)
y.goto(-40,-35)
u.goto(-40,-68)
r.pendown()
y.pendown()
u.pendown()
for i in range(100):
    rr = random.randint(2,4)
    r.forward(rr)
    yy = random.randint(2,4)
    y.forward(yy)
    uu = random.randint(2,4)
    u.forward(uu)
    if y.xcor() == 260 or r.xcor() == 260 or u.xcor() == 260:
        break

if r.xcor() > y.xcor() and r.xcor() > u.xcor():
    r.write("       I won!")
elif y.xcor() > r.xcor() and y.xcor() > u.xcor():
    y.write("       I won!")
elif u.xcor() > r.xcor() and u.xcor() > y.xcor():
    u.write("       I won!")
elif r.xcor() == y.xcor():
    r.write("       We tied!")
    y.write("       We tied!")
elif r.xcor() == u.xcor():
    r.write("       We tied!")
    u.write("       We tied!")
elif y.xcor() == r.xcor():
    y.write("       We tied!")
    r.write("       We tied!")
elif y.xcor() == u.xcor():
    y.write("       We tied!")
    u.write("       We tied!")
elif u.xcor() == r.xcor():
    u.write("       We tied!")
    r.write("       We tied!")
elif u.xcor() == y.xcor():
    u.write("       We tied!")
    y.write("       We tied!")
elif r.xcor() == y.xcor() and r.xcor() == u.xcor() and u.xcor() == y.xcor():
    u.write("       We tied!")
    r.write("       We tied!")
    y.write("       We tied!")
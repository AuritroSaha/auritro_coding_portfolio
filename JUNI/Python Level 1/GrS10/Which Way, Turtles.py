import random
import turtle


#t.color(r,g,b)

turtles = []

for i in range(10):
    turtles.append(turtle.Turtle())

for turtle in turtles:
    turtle.speed(10)
    turtle.shape("turtle")
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    x = random.randint(1,360)
    turtle.color(r,g,b)
    turtle.right(x)
    turtle.forward(200)
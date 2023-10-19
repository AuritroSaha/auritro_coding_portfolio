import turtle

t = turtle.Turtle()
t2 = turtle.Screen()

t.goto(50,50)

def moveForwardFive():
    t.forward(5)
t2.onkey(moveForwardFive, "right")

def drawTriangle():
    for i in range(3):
        t.forward(50)
        t.right(120)
t2.onkey(drawTriangle, "up")

def drawTriangle2():
    for i in range(3):
        t.forward(50)
        t.right(120)
t2.onkey(drawTriangle2, "a")

t2.listen()

if t.xcor() > 40 or t.ycor() > 40 or t.xcor() < -40 or t.ycor() < -40:
    print ("The turtle is out of bounds")





while True:
    if t.xcor() > 300 or t.ycor() > 300 or t.xcor() < -300 or t.ycor() < -300:
        print ("The turtle is out of bounds")
        t.goto(50, 50)
        t.write("The turtle is out of bounds.")

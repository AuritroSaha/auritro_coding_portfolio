import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

def draw_box():
    t.color("red")
    t.speed(100)
    t.penup()
    t.goto(-200,200)
    t.pendown()
    for i in range(4):
        t.forward(400)
        t.right(90)
    t.ht()
draw_box()

def check_collision(x):
    if x.xcor() < -200 or x.ycor() > 200 or x.xcor() > 200 or x.ycor() < -200:
        x.write("Out of bounds!", font=("Times New Roman", 12, "normal"))
        return True
    else:
        return False

screen = turtle.Screen()

def right():
    t2.right(7)
screen.onkey(right, "Right")

def left():
    t2.left(7)
screen.onkey(left, "Left")
screen.listen()

t3.penup()
t3.goto(-200,210)
t3.pendown()
t3.ht()

y = 0

while True:
    t3.clear()
    t3.write("Score: " + str(y), font=("Times New Roman", 12, "normal"))
    t2.speed(100)
    t2.forward(5)
    y = y + 1
    if check_collision(t2):
        break
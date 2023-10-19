import random, turtle

t = turtle.Turtle()
t2 = turtle.Screen()

num = random.randint(1, 10)

t.write(num)

if num < 5:
  num = 0
else:
  num = num + 10

t.penup()
t.goto(10, 10)
t.pendown()

t.write(num)

def moveForwardFive():
  t.forward(5)
  if t.xcor() > 300 or t.ycor() > 300 or t.xcor() < -300 or t.ycor() < -300:
    print ("The turtle is out of bounds")
  elif t.xcor() > 250 and t.xcor() < 300:
    print ("The turtle is near the right boundary.")
  else:
    print ("The turtle is near the center.")

t2.onkey(moveForwardFive, "right")
t2.listen()

import turtle

t = turtle.Turtle()

def checkCoordinate():
    if t.xcor() > 100:
        return False
    else:
        return True

while checkCoordinate():
    t.forward(5)
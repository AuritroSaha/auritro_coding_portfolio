import turtle

whales = []

for i in range(3):
    t = turtle.Turtle()
    whales.append(t)

for t in whales:
    t.backward(30)
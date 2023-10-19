def add(x, y):
  return x + y

print(add(3,5))

# Write a function that takes in 3 numbers and returns their product

def multiply(x, y, z):
  return x * y * z

print(multiply(3,3,3))

# Write a function that takes in two numbers and returns their average

def average(x, y):
  return (x+y)/2

print(average(5,11))

# Write a function that takes in a number and returns its factorial
# 5! = 5 * 4 * 3 * 2 * 1 = 1 * 2 * 3 * 4 * 5

def factorial(x):
  y = x
  for i in range((x-1)):
    x=x*(y-(i+1))
  return x

def factorial2(x):
  y = 1
  for i in range(1,x):
    y = (i+1)*y
  return y

print (factorial(5))
print (factorial2(5))
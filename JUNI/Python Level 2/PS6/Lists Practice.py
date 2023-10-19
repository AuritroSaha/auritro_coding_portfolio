'''
x = []

x.append(5)
x.append(2)
x.append(7)
x.append(2)

for i in x:
  print(i)

print()

x.remove(2)
for i in range(len(x)):
  print(x[i])

if 2 in x:
  print("2 is in your list")
'''


# Create a list of all the perfect squares between 1 and 10,000. The print out the list.

sqrs = []

for i in range(1,101):
  sqrs.append(i*i)

for i in sqrs:
  print(i)

print()
print()
print()

# Use your factorial function to create a list of all the factorials from 1! to 25!. Print out this list.

f = []

def factorial(x):
  y = 1
  for i in range(1,x):
    y = (i+1)*y
  return y

for i in range(1,26):
  f.append(factorial(i))

for i in f:
  print(i)

print()
print()
print()

# Write a function that takes in a list and returns the sum of the numbers.

nums = [1,2,3,4,5,6,7,8,9]

def sumOfList(num):
  v = 0
  for i in num:
    v += i
  print (v)

sumOfList(nums)

print()
print()
print()

# Write a function that takes in a list and returns the largest number in the list.

def largest(num):
  p = 0
  for i in num:
    if p<i:
      p = i
  print(p)

largest(nums)

# Ask user for name.
x = input("what is your name: ")

length = len(x)

# Using a for loop, print out every letter in the name
for i in range(length):
  print (x[i])

print()

# Using a for loop, print out every other letter in name
for i in range(0, length, 2):
  print(x[i])

print()

# Using a for loop, print out every letter in the name backward
for i in range(length-1, -1, -1):
  print(x[i])

print()

# Using a while loop, print out every letter in name
p = 0


while p<length:
  print(x[p])
  p = p + 1

print()

# Using a while loop, print out every other letter in name
p = 0

while p<length:
  if p%2 == 0:
    print(x[p])
  p = p + 1

print()

# Using a while loop, print out every letter in name backward
p = length - 1

while p!=-1:
  print(x[p])
  p = p - 1

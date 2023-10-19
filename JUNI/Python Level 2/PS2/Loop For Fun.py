""" 
Part I:
12345
12345
12345
12345
12345

Part II:
54321
54321
54321
54321
54321

Part III:
12345
23456
34567
45678
56789

Part IV:
1
12
123
1234
12345

Part V:
12345
1234
123
12
1 

print("Hello", end="")
"""

# Part 1
print("Part 1:")
print()

for i in range(5):
  for i in range(5):
    print(i+1, end="")
  print()

print()
print()

# Part 2
print("Part 2:")
print()

for i in range(5):
  for i in range(5,0, -1):
    print(i, end="")
  print()

print()
print()

# Part 3
print("Part 3:")
print()

p = 1

for i in range(5):
  for i in range(5):
    print(i+p, end="")
  print()
  p = p + 1

print()
print()

# Part 4
print("Part 4:")
print()

p = 1

for i in range(5):
  for i in range(p):
    print(i+1, end="")
  print()
  p = p + 1

print()
print()

# Part 5
print("Part 5:")
print()

p = 5

for i in range(5):
  for i in range(p):
    print(i+1, end="")
  print()
  p = p - 1

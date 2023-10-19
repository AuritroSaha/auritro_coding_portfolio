# main.py

# [2, 4, 1, 3, 2, 5]
# pivot: 2
# Less (than pivot): [1], Equal: [2, 2], Greater: [4, 3, 5]
# pivot: 4
# less: [3] equal: [4] greater: [5]
# Repeatedly combine list in order of Less + Equal + Greater
import random

num = []

for i in range(10):
  num.append(random.randint(0,100))

def partition(lis, pivot):
  less = []
  equal = []
  greater = []
  for i in lis:
    if i < pivot:
      less.append(i)
    elif i == pivot:
      equal.append(i)
    else:
      greater.append(i)

  return less, equal, greater

x = partition(num, num[0])

print("Lower: "+str(x[0])+"\nEqual: "+str(x[1])+"\nGreater: "+str(x[2]))
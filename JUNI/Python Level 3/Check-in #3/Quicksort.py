# QUICKSORT

# What is Quicksort? Can you describe how it works by drawing out an example?

# Would it make sense to ask what a list looks like after 2 passes of Quicksort? What does it use in place of passes?

# The function partition() takes in a list and pivot, and is an important part of implementing Quicksort in code, but it is incomplete. Finish implementing the function. Be sure to test the function after adding your code!
def partition(lst, pivot):
  less = []
  eq = []
  great = []

  for i in lst:
    if i < pivot:
      less.append(i)
    elif i > pivot:
      great.append(i)
    else:
      eq.append(i)

  return less, eq, great

# Test your function here
num = [1,4,7,2,3,10,100,4,7,5]
print(partition(num, 4))

# What is the time complexity of Quicksort? Can you describe the best and worst case scenarios?
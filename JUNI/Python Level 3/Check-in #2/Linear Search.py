# Linear Search

# What is Linear Search? When can we use it? Can you describe how it works by drawing out an example?

# The linearSearch() function takes in a list and sorts the numbers from largest to smallest, but it's incomplete. Fill in the missing code to create a working Linear Search function. Be sure to test the function after adding your code!

num = (1,2,34,5,4,5,67,7)

def linearSearch(l, v):
  for i in range(len(l)):
    if l[i] == v:
      return True
  return False

print(linearSearch(num, 3))
# What is the time complexity of Linear Search? Can you describe the best and worst case scenarios?

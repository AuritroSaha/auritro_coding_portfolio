'''
1. Write a function isEven() that returns True if the input number is even and False if the input number is odd. Use this function to print all of the even numbers between 1 and 50.
2. Write a function isOdd() that returns True if the input number is odd and False if the input number is even. Use this function to print all of the odd numbers between 1 and 50.
3. Write a function isOdd2() that only uses the isEven() function in its implementation. Use this function to print all of the odd numbers between 1 and 50.
4. Write a function isMultiple7() that returns True if the input number is a multiple of 7 and False otherwise. Use this function to print all of the multiples of 7 between 1 and 50.
5. Write a function isMultiple14() that returns True if the input number is a multiple of 14 and False otherwise. Use this function to print all of the multiples of 14 between 1 and 50.
6. Write a function isMultiple14v2() that only uses the isEven() and isMultiple7 functions in its implementation. Use this function to p rint all of the multiples of 14 numbers between 1 and 50.
Challenge: Write a function isPrime() that returns True if the input number is a prime number and False otherwise. Use this function to print all of the prime numbers between 1 and 50. 


'''
# Function 1

def isEven(i):
    m = i
    if (m)%2 == 0:
      return True
    else:
      return False

for i in range(1, 51):
  if isEven(i):
    print(i)

for i in range(1,51):
  j = isEven(i)
  if j == True:
    print (i)

print()
print()

# Function 2

def isOdd(i):
  m = i
  if (m)%2 == 1:
    return True
  else:
    return False

for i in range(1,51):
  j = isOdd(i)
  if j == True:
    print (i+1)

print()
print()

# Function 3

def isOdd2():
  for i in range(1,51):
    if isEven(i) == False:
      print(i)

isOdd2()

print()
print()

# Function 4

def isMultiple7(i):
  m = i+1
  if m%7 == 0:
    return True
  else:
    return False

for i in range(50):
  j = isMultiple7(i)
  if j == True:
    print(i+1)

print()
print()

# Function 5

def isMultiple14(i):
  m = i+1
  if m%14 == 0:
    return True
  else:
    return False

for i in range(50):
  j = isMultiple14(i)
  if j == True:
    print(i+1)

print()
print()

# Function 6

def isMultiple14v2(i):
  j = isEven(i)
  if j == True:
    m = isMultiple7(i)
    if m == True:
      return True
    else:
      return False

for i in range(50):
  k = isMultiple14v2(i)
  if k == True:
    print(i+1)

print()
print()

# Bonus

def isPrime(m):
  for p in range(2,m-1):
    if m%p==0:
      return False
  return True

for i in range(50):
  a = isPrime(i+1)
  if a == True:
    print(i+1)

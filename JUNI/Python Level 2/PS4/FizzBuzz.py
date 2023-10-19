'''
Write a program that prints the numbers 1 through 50. However, the program should print "Fizz" instead of the number if the number is a multiple of 3, and "Buzz" if the number is a multiple of 5. If it is a multiple of 3 and 5, the program should print "FizzBuzz."

Expected output:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
'''





for i in range(1, 51):
  if i % 3 == 0 and i % 5 == 0:
    i = "FizzBuzz"
  elif i % 3 == 0:
    i = "Fizz"
  elif i % 5 == 0:
    i = "Buzz"
  print (i)

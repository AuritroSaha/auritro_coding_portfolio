"""
Write a function that translates a word into Juni Latin (a simplified version of Pig Latin). The rules for translation are: add the first letter of the word and the suffix "ay" to the end of the original word to create the Juni Latin word! Using this function, ask the user for a word and output its Juni Latin translation. 

pickle -> icklepay
"""

x = input("Give a word: ")

print(x[1:])
print(x[:4])
print(x[1:4])

x1 = x[0]

x += x1+"ay"

xlen = len(x)

for i in range(1,xlen):
  print (x[i], end = '')

print()

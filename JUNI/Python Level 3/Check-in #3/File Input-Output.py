# FILE INPUT/OUTPUT

# Ask the user to input a word. Then, write the word letter by letter into an external file.
word = input("Enter a word: ")

f = open("letterbyletter","w")

for i in word:
  f.write(i+"\n")
f.close()
# Reading from the file that you just created, create a dictionary where the keys are the unique letters of your input and the values are how often those letters occur.
f = open("letterbyletter", "r")

occur = {}

for i in f.readlines():
  i = i.strip()
  if i not in occur:
    occur[i] = 0
  occur[i] += 1

print(occur)
# What's the difference between read() and readlines()?
# read returns everything in one string and readliens returns a list where each element is a line
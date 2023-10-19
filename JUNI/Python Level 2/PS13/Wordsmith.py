'''
Try at least one:

Bonus #1: Change the scoring system so that the user gets more points for longer words. For example, 1 point for 1-letter words, 2 points for 2-letter words, 3 points for 3-letter words, 5 points for 4-letter words, 8 points for 5-letter words, etc.
Bonus #2: Allow the user to end the game whenever they'd like to and start a new game. Keep track of the high score!
Bonus #3: Make it so that the list of 7 random letters always contains at least two vowels.
'''


import random
import time

# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()

consonents = []
vowels = []

for i in range(98,101):
  consonents.append(chr(i))
for i in range(102,105):
  consonents.append(chr(i))
for i in range(106,111):
  consonents.append(chr(i))
for i in range(112,117):
  consonents.append(chr(i))
for i in range(118,123):
  consonents.append(chr(i))

vowels.append(chr(97))
vowels.append(chr(101))
vowels.append(chr(105))
vowels.append(chr(111))
vowels.append(chr(117))

x = input("Welcome to Wordsmith! In this game, come up with as many words as you can using the 7 letters you are given. \nPress Enter to begin!")
print("Ready....")
time.sleep(2)
print("Set....")
time.sleep(2)
print("Type!")

print("Your random letters are: ")

randomletters = []

for i in range(5):
  randomletters.append(random.choice(consonents))
for i in range(2):
  randomletters.append(random.choice(vowels))

print(randomletters)

score = 0

usedwords = []

while True:
  word = input("Enter a word: ")
  if word not in usedwords:
    if word in validWords:
      isValid = True
      for i in word:
        if i not in randomletters:
          isValid = False
      if isValid:
        score = len(word)+score
        print("Your score is "+str(score))
        usedwords.append(word)
      else:
        print("You can only use the 7 letters given.")
    else:
      print("The word you typed does not exist.")
  else:
    print("You already used that word.")
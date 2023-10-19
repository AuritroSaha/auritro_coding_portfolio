import random

def product(x, y):
  return x*y

print(product(15,22))

'''

1. Make a variable that is randomly set to either 0 or 1 (this tracks whether the player wins or not). Make another variable that contains a random number from 1 to 1000 (this is how much money the player wins). Now let’s play the lottery! 2. Define a function that takes in the two random variables we created. The function should return a string that either tells the player that they lost, or tells the player how much money they won. 3. Print a message that welcomes the user to the lottery, and then calls the function to play the game. 

'''

print("Welcome to the grand lottery where you may or may not win!")

def lottery(win, winnings):
  if win == 1:
    print("You won $" + str(winnings) + ", play again for way more $$$$$$$$!")
  else:
    print("You lose, but you can always play again!")

win = random.randint(0,1)
winnings = random.randint(1,1000)

lottery(win, winnings)


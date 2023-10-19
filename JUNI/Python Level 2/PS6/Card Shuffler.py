'''
Write a function shuffle(numShuffles) which first generates an ordered list of 52 playing card, as such: [1,1,1,1,2,2,2,2,...,13,13,13,13]. Then, randomly choose two positions within the deck and swap the two cards at these two position. Do this numShuffles number of times, and then print out the resulting shuffled deck. Call this function with 10, 50, 100, and 500 shuffles and notice at what point the deck seems randomly shuffled! 



'''
import random

numShuffles = int(input("How many times do you want to shuffle? "))

deck = []

for g in range(4):
  for i in range(1,14):
    deck.append(i)


def shuffle(numShuffles):
  for i in range(numShuffles):
    m = random.randint(0,51)
    n = random.randint(0,51)
    deck[m], deck[n] = deck[n], deck[m]
  for i in deck:
    print(i)

shuffle(numShuffles)

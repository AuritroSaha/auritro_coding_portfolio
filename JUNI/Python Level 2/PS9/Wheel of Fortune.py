import random

wordbank = ["programming", "bananas", "potato", "pants", "computers", "television", "videogames"]

word = random.choice(wordbank)

secretword = ""

wordvset = set()

for i in word:
    wordvset.add(i)

for i in range(len(word)):
    secretword += "_ "

secretset = set()

correctguesses = set()

for i in word:
    secretset.add(i)

guesses = len(word) + 5

print("Welcome to Hangman! You have " + str(guesses) + " guesses to figure out the correct word. Good luck!")


def checkLetter(guess):
    global guesses

    if guess in secretset:
        correctguesses.add(guess)
        guesses = guesses - 1
    else:
        guesses = guesses - 1


while True:

    guesstense = ""
    if guesses == 1:
        guesstense = "guess"
    else:
        guesstense = "guesses"

    print(secretword)
    print()
    letter = input("Guess a letter! You have " + str(guesses) + " " + guesstense + " remaining. ")
    checkLetter(letter)
    secretword = ""
    for i in word:
        if i in correctguesses:
            secretword += i + " "
        else:
            secretword += "_ "
    if str(correctguesses).strip() == str(wordvset).strip():
        print(secretword)
        print("You guessed the word correctly, Great Job!")
        break
    elif guesses == 0:
        print(secretword)
        print("You ran out of guesses, You Lose!")
        break

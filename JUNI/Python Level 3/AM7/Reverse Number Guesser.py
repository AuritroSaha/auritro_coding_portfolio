import random

print("Think of a whole number between 1 and 100 and I'll try to guesss it in 7 tries.")

guesses = 7
lower = 1
upper = 100

while guesses > 0:
    guesses = guesses - 1

    guess = (lower + upper) // 2

    while True:
        g = input("Is your number " + str(guess) + "?\nType Yes, Above, or Below: ")
        g.lower()
        if g == "yes" or g == "above" or g == "below":
            break

    if g == "yes":
        break

    elif g == "above":
        lower = guess + 1

    elif g == "below":
        upper = guess - 1

print("Knew I'd get it with " + str(guesses) + " guess(es) left!")

# 2 ^ 5 = 32
# 2 ^ 6 = 64
# 2 ^ 7 = 128
# log_2(100) < 7
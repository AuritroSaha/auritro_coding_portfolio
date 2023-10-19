# main.py

'''
1. Dictionary to map values of 1, 11, 12, and 13 to Ace, Jack, Queen, and King
2. printHnad() function that prints cards with proper names
3. calcHandValues() that takes in a list of cards and returns the possible values the hand can be worth
4. getFinalValue() function that takes in a list of cards and returns the best value resulting from that hand
'''

import random, time

print(
    "Welcome to the game of Blackjack! In this game, you will be dealt two cards to start. Your goal is to get as close to 21 as possible without going over - or busting! In this simple version of Blackjack, we only use the cards 2 through 11(Ace).\n\n The dealer will first ask you to hit (take another card) or stay. As long as you don't bust, once you decide to stay, the dealer will then play his hand. The dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!\n")

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

cardname = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

phandwnames = []


def printhand(hand):
    name = ""
    if hand == phand:
        name = "your"
    elif hand == dhand:
        name = "the dealer's"
    for i in hand:
        if i == 1 or i == 11 or i == 12 or i == 13:
            i = cardname[i]
        phandwnames.append(i)
    print("Here is " + str(name) + " hand:\n" + str(phandwnames))
    phandwnames.clear()


'''
Hand: [Ace, Ace, Ace, 2]
We see we have 3 aces.

If we turn 0 aces into 11: sum = 5
If we turn 1 ace into 11: sum = 15
If we turn 2 aces into 11: sum = 25
If we turn 3 aces into 11: sum = 35

'''


def calcHandValues(hand):
    acenum = 0
    x = []
    for i in hand:
        if i == 1:
            acenum += 1
    for i in range(acenum + 1):
        y = sum(hand) + (10 * i)
        x.append(y)
    return x


def getFinalValue(hand):
    finalvalue = 22
    sortedPossibleValues = sorted(calcHandValues(hand))
    for i in sortedPossibleValues:
        if i <= 21:
            finalvalue = i
    return finalvalue


dealerchoice = ["H", "S"]

while True:
    while True:
        phand = []
        dhand = []

        for i in range(2):
            x = random.choice(cards)
            phand.append(x)

        for i in range(2):
            x = random.choice(cards)
            dhand.append(x)

        if getFinalValue(phand) <= 21 and getFinalValue(dhand) <= 21:
            break

    input("Press Enter to start playing.")
    while True:
        while True:
            printhand(phand)
            x = input("Type H to hit or S to stay or calcHand to see the sum of your hand: ")
            if getFinalValue(phand) == 21:
                break
            if x == "H" or x == "S":
                break
            if x == "calcHand":
                print("These could be the values of your hand: " + str(calcHandValues(phand)))
        if getFinalValue(phand) == 21:
            time.sleep(2)
            print("You got Blackjack!")
            printhand(phand)
            break
        if x == "H":
            phand.append(random.choice(cards))
        elif x == "S":
            break
        if getFinalValue(phand) > 21:
            print("You busted and the dealer wins!")
            printhand(phand)
            break

    while True:
        if getFinalValue(phand) > 21 or getFinalValue(phand) == 21:
            break
        time.sleep(2)
        printhand(dhand)
        if getFinalValue(dhand) == 21:
            time.sleep(2)
            print("The dealer got Blackjack!")
            printhand(dhand)
            break
        x = random.choice(dealerchoice)
        if getFinalValue(dhand) <= 17:
            if x == "H":
                dhand.append(random.choice(cards))
            if x == "S":
                dhand.append(random.choice(cards))
        elif getFinalValue(dhand) > 17:
            if x == "H":
                dhand.append(random.choice(cards))
            elif x == "S":
                break
        if getFinalValue(dhand) > 21:
            time.sleep(2)
            print("The dealer busted and you win!")
            printhand(dhand)
            break

    if getFinalValue(dhand) < 21 and getFinalValue(phand) < 21:
        time.sleep(2)
        if getFinalValue(phand) > getFinalValue(dhand):
            print("You Won!")
        elif getFinalValue(phand) < getFinalValue(dhand):
            print("You lost!")
        elif getFinalValue(phand) == getFinalValue(dhand):
            print("You tied")


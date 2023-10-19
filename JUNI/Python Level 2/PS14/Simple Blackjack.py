import random, time

print(
    "Welcome to the game of Blackjack! In this game, you will be dealt two cards to start. Your goal is to get as close to 21 as possible without going over - or busting! In this simple version of Blackjack, we only use the cards 2 through 11(Ace).\n\n The dealer will first ask you to hit (take another card) or stay. As long as you don't bust, once you decide to stay, the dealer will then play his hand. The dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!\n")

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

dealerchoice = ["H", "S"]

while True:
    phand = []
    dhand = []

    for i in range(2):
        phand.append(random.choice(cards))

    for i in range(2):
        dhand.append(random.choice(cards))

    input("Press Enter to start playing.")
    while True:
        while True:
            print("Here is your hand:\n" + str(phand))
            x = input("Type H to hit or S to stay: ")
            if x == "H" or x == "S":
                break
        if x == "H":
            phand.append(random.choice(cards))
        elif x == "S":
            break
        if sum(phand) > 21:
            print("You busted and lost!")
            print("Your hand was:\n" + str(phand))
            break
        if sum(phand) == 21:
            print("You got Blackjack!")
            break

    while True:
        if sum(phand) > 21 or sum(phand) == 21:
            break
        time.sleep(2)
        print("Here is the dealer's hand:\n" + str(dhand))
        x = random.choice(dealerchoice)
        if sum(dhand) <= 17:
            if x == "H":
                dhand.append(random.choice(cards))
            if x == "S":
                dhand.append(random.choice(cards))
        elif sum(dhand) > 17:
            if x == "H":
                dhand.append(random.choice(cards))
            elif x == "S":
                break
        if sum(dhand) > 21:
            time.sleep(2)
            print("Dealer busted and you win!")
            print("Their hand was:\n" + str(dhand))
            break
        elif sum(dhand) == 21:
            time.sleep(2)
            print("The dealer got Blackjack!")
            break

    if sum(dhand) < 21 and sum(phand) < 21:
        time.sleep(2)
        if sum(phand) > sum(dhand):
            print("You Won!")
        elif sum(phand) < sum(dhand):
            print("You lost!")
        elif sum(phand) == sum(dhand):
            print("You tied")


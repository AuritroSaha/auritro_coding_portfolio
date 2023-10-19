import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str(self.value) + " of " + self.suit


class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Hearts", "Spades", "Diamonds", "Clovers"]

        for j in self.suits:
            for i in range(13):
                self.cards.append(Card(i + 1, j))

    def __str__(self):
        deck = ""
        for card in self.cards:
            deck += str(card) + "\n"
        return deck

    def drawCard(self):
        if len(self.cards) == 0:
            return "There are no cards."

        return self.cards.pop(0)

    def shuffle(self):
        for i in range(len(self.cards)):
            x = random.randint(0, len(self.cards) - 1)
            temp = self.cards[x]
            self.cards[x] = self.cards[i]
            self.cards[i] = temp


card1 = Card(3, "Diamonds")
card2 = Card(7, "Hearts")
card3 = Card(4, "Spades")

print(card1)
print(card2)
print(card3)

deck1 = Deck()

for i in range(53):
    print(deck1.drawCard())

deck1 = Deck()
deck1.shuffle()
print(deck1)

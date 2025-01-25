# Player object, contains information about their hand and remaining chips.

class Player:
    def __init__(self):
        self.hand = []
        self.chips = 500 # arbitrary amount of chips 

    def printHand(self):
        print("Player Hand:")
        [print(card.name) for card in self.hand]

class Dealer():
    def __init__(self):
        self.hand = []

    def printHand(self):
        print("Dealer Hand:")
        print(self.hand[0].name)
        print("Card Hidden")
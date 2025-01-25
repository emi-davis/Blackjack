# Player object, contains information about their hand and remaining chips.

class Player:
    def __init__(self):
        self.hand = []
        self.chips = 500 # arbitrary amount of chips 

    def printHand(self):
        [print(card.value, card.name) for card in self.hand]
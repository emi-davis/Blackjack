class Player:
    def __init__(self):
        self.hand = []

    def printHand(self):
        [print(card.value, card.name) for card in self.hand]
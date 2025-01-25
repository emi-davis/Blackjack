# Player object, contains information about their hand and remaining chips.

class Player:
    def __init__(self):
        self.hand = []
        self.split_hand = []
        self.chips = 500 # arbitrary amount of chips 

    def printHand(self):
        print("\nPlayer Hand:")
        [print(card.name) for card in self.hand]
    
    def evaluateHand(self):
        total = sum([card.value for card in self.hand]) # sum total value of cards, treating aces as 1
        if any(card.is_ace for card in self.hand) and total+10 <= 21: # see if there are any aces in hand and make sure total stays under or equal to 21
            total+=10
        return total

class Dealer(Player):
    def printHand(self):
        print("\nDealer Hand:")
        print(self.hand[0].name)
        print("Card Hidden") # hide second card to mimic casino
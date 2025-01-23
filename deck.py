# Deck object 

from card import Card

class Deck:
    ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    # Creates deck when initialized
    def __init__(self):
        self.cards = []
        count = 2
        for suit in self.suits:
            for rank in self.ranks:
                if rank in ['Jack', 'Queen', 'King']:
                    self.cards.append(Card(f"{rank} of {suit}", 10, False))
                elif rank == 'Ace':
                    self.cards.append(Card(f"{rank} of {suit}", 11, True))
                else:
                    self.cards.append(Card(f"{rank} of {suit}", count, False))
                    count += 1
                    if count > 10:
                        count = 2

    # DEBUG STATEMENT
    def printDeck(self):
        print([(card.value, card.name) for card in self.cards])
    # DELETE LATER

deck = Deck()
deck.printDeck()
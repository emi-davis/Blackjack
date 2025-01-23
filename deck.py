# Deck object 

from card import Card
import random

class Deck:
    ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    # Creates deck when initialized
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    # DEBUG STATEMENT
    def printDeck(self):
        [print(card.rank+' of '+card.suit) for card in self.cards]
        print(self.cards[0].is_ace)
    # DELETE LATER
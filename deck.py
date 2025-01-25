# Deck object, contains logic for card creation, drawing from the deck, and shuffling.

from card import Card
import random

class Deck:
    ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    # creates deck when initialized
    def __init__(self, num_decks):
        self.cards = []
        for i in range(num_decks): # allows user to choose how many decks to use
            count = 1
            for suit in self.suits:
                for rank in self.ranks:
                    if rank in ['Jack', 'Queen', 'King']:
                        self.cards.append(Card(f"{rank} of {suit}", 10, False)) # face cards are worth 10
                    else:
                        self.cards.append(Card(f"{rank} of {suit}", count, count==1)) # all other cards are worth written value
                        count += 1
                        if count > 10:
                            count = 1
    
    def drawCard(self): # draw card
        return self.cards.pop(0)
    
    def shuffleDeck(self): # shuffle
        random.shuffle(self.cards)
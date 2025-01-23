# Deck object 

from card import Card

class Deck:
    ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    # creates deck when initialized
    def __init__(self, num_decks):
        self.cards = []
        for i in range(num_decks): # allows user to choose how many decks to use
            count = 2
            for suit in self.suits:
                for rank in self.ranks:
                    if rank in ['Jack', 'Queen', 'King']:
                        self.cards.append(Card(f"{rank} of {suit}", 10, False)) # face cards are worth 10
                    elif rank == 'Ace':
                        self.cards.append(Card(f"{rank} of {suit}", 11, True)) # aces are worth 11
                    else:
                        self.cards.append(Card(f"{rank} of {suit}", count, False)) # all other cards are worth written value
                        count += 1
                        if count > 10:
                            count = 2

    # DEBUG STATEMENT
    def printDeck(self):
        print([(card.value, card.name) for card in self.cards])
        print(len(self.cards))
    # DELETE LATER
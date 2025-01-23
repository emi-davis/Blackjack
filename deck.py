# Deck object 

from card import Card

class Deck:
    ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    # Creates deck when initialized
    def __init__(self):
        self.cards = []
        count = 1
        for suit in self.suits:
            for rank in self.ranks:
                if rank in ['Jack', 'Queen', 'King']:
                    count = 10
                self.cards.append(Card(rank, suit, count))
                count += 1
                if count > 10:
                    count = 1

    # DEBUG STATEMENT
    def printDeck(self):
        #[print(card.rank+' of '+card.suit) for card in self.cards]
        #print(self.cards[0].is_ace)
        print([card.value for card in self.cards])
    # DELETE LATER

deck = Deck()
deck.printDeck()
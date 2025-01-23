# Card object used in deck.

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.is_ace = (rank == 'Ace')
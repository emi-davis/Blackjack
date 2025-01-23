# Card object used in deck.

class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.is_ace = (rank == 'Ace')
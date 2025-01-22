# Card object used in deck, contains suits/ranks

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.is_ace = (rank == 'ace')
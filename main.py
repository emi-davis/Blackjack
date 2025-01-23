# Developed by Emilia
# Last updated 1/22/2025

from deck import Deck

def main():
    num_decks = int(input("How many decks would you like to use? "))
    deck = Deck(num_decks)
    deck.printDeck()

if __name__ == "__main__":
    main()
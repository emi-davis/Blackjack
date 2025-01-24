# Developed by Emilia
# Last updated 1/22/2025

from deck import Deck

def main():
    while True:
        try:
            num_decks = int(input("How many decks would you like to use? (1-6) "))
            if 1 <= num_decks <= 6:
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid number between 1-6.")
    deck = Deck(num_decks)
    deck.printDeck()

if __name__ == "__main__":
    main()
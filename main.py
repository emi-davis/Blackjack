# Developed by Emilia
# Last updated 1/24/2025

from deck import Deck
from player import Player, Dealer

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
    player = Player()
    dealer = Dealer()

    deck.shuffleDeck()
    player.hand.append(deck.drawCard())
    dealer.hand.append(deck.drawCard())
    player.hand.append(deck.drawCard())
    dealer.hand.append(deck.drawCard())
    player.printHand()
    dealer.printHand()
    
    while player.evaluateHand() < 21:
        match input("Please decide what you would like to do next. (Hit / Stand) ").lower():
            case 'hit':
                player.hand.append(deck.drawCard())
                player.printHand()
            case 'stand':
                player.printHand()
                break
    
    player.printHand()
    
    while dealer.evaluateHand() < 17:
        dealer.hand.append(deck.drawCard())
    
    dealer.printHand()
            
    
if __name__ == "__main__":
    main()
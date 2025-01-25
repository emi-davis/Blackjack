# Developed by Emilia
# Last updated 1/24/2025

from deck import Deck
from player import Player, Dealer

def main():
    while True: # ask user how many decks they would like to use
        try:
            num_decks = int(input("How many decks would you like to use? (1-6) "))
            if 1 <= num_decks <= 6:
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid number between 1-6.")

    deck = Deck(num_decks) # create objects used in game
    player = Player()
    dealer = Dealer()

    deck.shuffleDeck() # shuffle then deal cards to player / dealer in alternating order
    player.hand.append(deck.drawCard())
    dealer.hand.append(deck.drawCard())
    player.hand.append(deck.drawCard())
    dealer.hand.append(deck.drawCard())
    player.printHand()
    dealer.printHand()

    if player.hand[0].value == player.hand[1].value:
        while True: # ask if user would like to split their hand
            match input("Would you like to split your hand? (y/n) ").lower():
                case 'y':
                    player.split_hand.append(player.hand.pop(0))
                    break
                case 'n':
                    break
                case _:
                    print("Please enter y or n.")

    while player.evaluateHand() < 21: # if player hand value is under 21, ask them what they want to do
        match input("Please decide what you would like to do next. (Hit / Stand) ").lower():
            case 'hit':
                player.hand.append(deck.drawCard())
                player.printHand()
            case 'stand':
                player.printHand()
                break
            case _:
                print("Please enter a valid choice.")

    player.printHand()

    while dealer.evaluateHand() < 17:
        dealer.hand.append(deck.drawCard())

    dealer.printHand()
    
if __name__ == "__main__":
    main()
#Bring in python's random library
import random #This brings in the random library so we may generate a random value. 

def calculate_total(hand):
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total

#Shuffle deck
while True:
    deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
    random.shuffle(deck)

#Deal cards
    def draw_card():
        card = random.choice(deck)
        deck.remove(card)
        return card
    
    player = [draw_card(), draw_card()]
    dealer = [draw_card(), draw_card()]

#First, the player's turn
    while True:
        print("Your hand:", player, "Total =", calculate_total(player))
        print("Dealer Shows:", dealer[0])

        if calculate_total(player) > 21:
            print("You bust! Dealer Wins")
            break
        
        choice = input("hit or stand? ").lower()
        if choice == "hit":
            player.append(draw_card())
        else:
            break

#If you bust 
    if calculate_total(player) <= 21:

#Dealer Turn
        print("Dealer's Hand:", dealer, "Total =", calculate_total(dealer))   
        while calculate_total(dealer) < 17:
            dealer.append(draw_card())
            print("Dealer Hits:", dealer, "Total=", calculate_total(dealer))


#Show hand and determine winner
        player_total = calculate_total(player)
        dealer_total = calculate_total(dealer)

        print("\n ****    Final Results    ****")
        print("Player:", player_total)
        print("Dealer:", dealer_total)


        if dealer_total > 21:
            print("Dealer Busts, you win!")
        elif player_total > dealer_total:
            print("You win!")
        elif dealer_total > player_total:
            print("Dealer Wins")
        else:
            print("It is a tie")

#Potential loop or exit for the player
    play_again = input("\n Would you like to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thank you for playing!")
        break
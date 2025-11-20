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
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]

#First, the player's turn
    while True:
        print("Your hand:", player, "Total =", calculate_total(player))
        print("Dealer Shows:", dealer[0])

        if calculate_total(player) > 21:
            print("You bust! Dealer Wins")
            break
        
        choice = input("hit or stand? ").lower()
        if choice == "hit":
            player.append(deck.pop())
        else:
            break

#If you bust 
    if calculate_total(player) <= 21:

#Dealer Turn
        print("Dealer's Hand:", dealer, "Total =", calculate_total(dealer))   
        while calculate_total(dealer < 17):
            dealer.append(deck.pop)
            print("Dealer Hits:", dealer, "Total=", calculate_total(dealer))


#Show hand and determine winner
        

#Potential loop or exit for the player
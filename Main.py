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

#First, the player's turn
   

#If you bust 
        

#Hit or Stand
        
#Next the dealer's turn



#Show hand and determine winner


#Potential loop or exit for the player
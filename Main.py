import random #This brings in the random library so we may generate a random value. 

#A function for situations where you could convert an ace to a 1 to prevent a bust. 
def calculate_total(hand):  
    total = sum(hand)
    while total > 21 and 11 in hand: #If the player has more than 21 in their hands, with an ace (11), convert to (1)
        hand[hand.index(11)] = 1
        total = sum(hand) #Recalculate the total now that the conversion is complete.
    return total

#Shuffle deck
while True:
    deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4 #Values 2-11. 10 also being face cards. Times 4 for suits
    random.shuffle(deck) #Jumble up the deck in a complete random order. 

#Deal cards
    def draw_card():
        card = random.choice(deck) #A random card will be drawn from the deck when this function is called
        deck.remove(card) #Make sure to remove that card from the deck so it cannot be drawn again. 
        return card
    
    player = [draw_card(), draw_card()] #Swtiched from deck.pop() to draw_card
    dealer = [draw_card(), draw_card()] #Player and dealer each given two random cards

#First, the player's turn
    while True:
        print("Your hand:", player, "Total =", calculate_total(player)) #Make sure the player knows whats in their hand
        print("Dealer Shows:", dealer[0])

        if calculate_total(player) > 21: #If you have a value over 21, you lose the game.
            print("You bust! Dealer Wins")
            break 
        
        while True:
            choice = input("Hit or Stand? ").strip().lower() #Help the user out, if they enter lowercase, uppercase, it counts. 
            if choice in ("hit", "stand"):
                break
            print("Invalid Input. Please type hit or stand.") #Make sure the user enters some variation of "hit" or "Stand"

        if choice == "hit":
            player.append(draw_card())
        else:
            break
            

#If you bust 
    if calculate_total(player) <= 21: #After the player takes their turn, if you have a value less than/equal to 21, the game will continue. 

#Dealer Turn
        print("Dealer's Hand:", dealer, "Total =", calculate_total(dealer))  #Show what the dealer has.
        while calculate_total(dealer) < 17:   #The dealer will hit anytime he has a value less than 17
            dealer.append(draw_card())
            print("Dealer Hits:", dealer, "Total=", calculate_total(dealer)) #Display the new total to the player.


#Show hand and determine winner
        player_total = calculate_total(player) #Calculate the player's hand here and dealer's hand in the next line
        dealer_total = calculate_total(dealer)

        print("\n ****    Final Results    ****") #Format the display to present results.
        print("Player:", player_total)
        print("Dealer:", dealer_total)


        if dealer_total > 21:
            print("Dealer Busts, you win!")   #If the dealer has more than 21 you win
        elif player_total > dealer_total:   #Of course if you have more than the dealer, you win
            print("You win!")
        elif dealer_total > player_total:  #Conversely, if the dealer has more than you, dealer wins.
            print("Dealer Wins")
        else:
            print("It is a tie")    #In this project, a tie is a straight tie. The house does not win on a tie. 

#Potential loop or exit for the player
    play_again = input("\n Would you like to play again? (y/n): ").lower() #Ask the user if they would like another round. 
    if play_again != "y":
        print("Thank you for playing!") #If they don't want another round, thank them for playing and end. 
        break
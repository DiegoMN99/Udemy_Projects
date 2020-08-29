import random


symbols = ("Hearts", "Diamonds", "Clubs", "Spades")

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine": 9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

# CARD CLASS, INTERNAL CHARACTERISTICS OF INDIVIDUAL CARDS
class Card:
    def __init__(self,symbol,rank):
        self.symbol = symbol
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.symbol
#---------------------------------------------------------------------------------------------------------------------------------------------#

class Deck: 

#CREATE A DECK OF CARDS

    def __init__(self):

        self.all_cards = []

        for symbol in symbols:
            for rank in ranks:
                created_card = Card(symbol,rank) 
                self.all_cards.append(created_card)

#MIXING CARDS (SHUFFLE THE DECK)

    def shuffle(self):

        random.shuffle(self.all_cards)

#DEALING CARDS

    def deal(self,x):
        my_list=[]
        for i in range (x):
            my_list += [self.all_cards.pop()]
            
        return my_list
          
#Check Deck length (Amount of cards)

    def check_if_empty(self):
        if len(self.all_cards) == 0:
            return True
        else: 
            return False
        
    
#---------------------------------------------------------------------------------------------------------------------------------------------#

#CREATING PLAYERS 

class Player:

    #Player name
    def __init__(self,name):

        self.name = name
        self.all_cards = []
        self.chips = 1000
        self.bet = 10

#---------------------------------------------------------------------------------------------------------------------------------------------#
class Dealer:

    def __init__(self, name):

        self.name = name
        self.all_cards = []


#----------------------------------------------------------------LOGIC------------------------------------------------------------------------#

print ("Welcome to BlackJack!")
turn = True
playing = True 
turn_win = True
deck_empty = False

new_deck = Deck()
new_deck.shuffle()

round_counter = 0

player = Player("PC")
dealer = Dealer("Casa")



while playing:
    if turn_win == True:
        player.bet = 10
    else:
        player.bet *= 2

    if player.chips < player.bet:
        player.bet = player.chips

    player.chips -= player.bet

    player.all_cards = player.all_cards + new_deck.deal(2) 
    dealer.all_cards = dealer.all_cards + new_deck.deal(2)

    player_total = 0

    if player.all_cards[0].rank == "Ace" and player.all_cards[1].rank == "Ace":
        player_total = 12
    
    if player.all_cards[0].rank == "Ace" and player.all_cards[1].rank != "Ace":
        if player.all_cards[1].value + 11 > 21:
            player_total = player.all_cards[1].value + 1
        
        else: 
            player_total = player.all_cards[1].value + 11


    if player.all_cards[1].rank == "Ace" and player.all_cards[0].rank != "Ace":
        if player.all_cards[0].value + 11 > 21:
            player_total = player.all_cards[0].value + 1
        
        else: 
            player_total = player.all_cards[0].value + 11

    hit = True

    while hit:   

        deck_empty = new_deck.check_if_empty()

        if deck_empty == True:
            break

        if player_total <= 11:
            player.all_cards = player.all_cards + new_deck.deal(1)

        elif player_total == 12 and dealer.all_cards[0].value in [2,3,4,7,8,9,10,11]:
            player.all_cards = player.all_cards + new_deck.deal(1)

        elif player_total == 13 and dealer.all_cards[0].value in [2,7,8,9,10,11]:
            player.all_cards = player.all_cards + new_deck.deal(1)

        elif player_total == 14 and dealer.all_cards[0].value in [2,7,8,9,10,11]:
            player.all_cards = player.all_cards + new_deck.deal(1)

        elif player_total == 15 and dealer.all_cards[0].value in [7,8,9,10,11]:
            player.all_cards = player.all_cards + new_deck.deal(1)
        
        elif player_total == 16 and dealer.all_cards[0].value in [7,8,9,10,11]:
            player.all_cards = player.all_cards + new_deck.deal(1)

        elif player_total == 17 and dealer.all_cards[0].value in [7,8,9,11]:
            player.all_cards = player.all_cards + new_deck.deal(1)

        else: 

            hit = False

        if player.all_cards[-1].rank == "Ace":
            if player_total + 11 > 21:
                player_total = player_total + 1
        
            else: 
                player_total = player_total + 11
        else: 
            player_total += player.all_cards[-1].value
        
    if deck_empty == True:
            break

    dealer_total = 0

    if dealer.all_cards[0].rank == "Ace" and dealer.all_cards[1].rank == "Ace":
        dealer_total = 12
    
    if dealer.all_cards[0].rank == "Ace" and dealer.all_cards[1].rank != "Ace":
        if dealer.all_cards[1].value + 11 > 21:
            dealer_total = dealer.all_cards[1].value + 1
        
        else: 
            dealer_total = dealer.all_cards[1].value + 11


    if dealer.all_cards[1].rank == "Ace" and dealer.all_cards[0].rank != "Ace":
        if dealer.all_cards[0].value + 11 > 21:
            dealer_total = dealer.all_cards[0].value + 1
        
        else: 
            dealer_total = dealer.all_cards[0].value + 11


    hit = True

    while hit:   

        deck_empty = new_deck.check_if_empty()

        if deck_empty == True:
            break

        if dealer_total < 17:
            dealer.all_cards = dealer.all_cards + new_deck.deal(1)

        else: 

            hit = False

        if dealer.all_cards[-1].rank == "Ace":
            if dealer_total + 11 > 21:
                dealer_total = dealer_total + 1
        
            else: 
                dealer_total = dealer_total + 11
        else: 
            dealer_total += dealer.all_cards[-1].value
    
    if deck_empty == True:
            break

    round_counter += 1

    print (f"ROUND NUMBER {round_counter}")
    print (f"The dealer has gotten {dealer_total}")
    print (f"The player has gotten {player_total}")
    print (f"The deck now has {len(new_deck.all_cards)} cards")


    player.all_cards = []
    dealer.all_cards = []
    
    
    
    
    
    if player_total > 21: 
        print ("Lost the round!")
        turn_win = False

        

    elif dealer_total > 21:
        player.chips += player.bet*2
        earnings = player.bet*2
        print (f"Player has won {earnings}! chips")
        turn_win = True
        

    elif player_total > dealer_total:
        player.chips += player.bet*2
        earnings = player.bet*2
        print (f"Player has won {earnings}! chips")
        turn_win = True
        
    else: 
        print ("Lost the round!")
        turn_win = False

    if player.chips == 0:
        print ("Out of chips! Sorry!")
        playing = False
    
    if len(new_deck.all_cards) < 4:
        print ("Out of cards! Sorry!")
        print ("GAME OVER!")
        playing = False

    
        



    

    


    

    
        




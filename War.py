import random


symbols = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine": 9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

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

    def deal_one(self):
        return self.all_cards.pop()
    
#---------------------------------------------------------------------------------------------------------------------------------------------#

#CREATING PLAYERS (HANDS)

class Player:

    #Player name
    def __init__(self,name):

        self.name = name
        self.all_cards = []

    # Player status 
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"


    #Cast a card (Top of the deck)

    def remove_one(self):
        return self.all_cards.pop(0)


    #Take cards and add them to the player's hand

    def add_cards (self,new_cards):

        if type(new_cards) == type([]): # <----- List of multiple cards (taking more than one card)
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards) # <------ Taking a single card
        

    #---------------------------------------------------------------------------------------------------------------------------------------------#

#                                                                LOGIC

    #---------------------------------------------------------------------------------------------------------------------------------------------#

#GAME SETUP

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle() #<-------Shuffling the deck before game starts

#Splitting the deck in half (Half the deck for each player)

for x in range(26):
    player_one.add_cards(new_deck.deal_one()) #<-------- Giving each player one card x26
    player_two.add_cards(new_deck.deal_one())

game_on = True #<---- Still playing

round_counter = 0

while game_on:

    round_counter += 1
    print (f"Round {round_counter}")

    if len(player_one.all_cards) == 0: #<------ "All cards" refers to their hand (cards in front of them in real life) 
        print ("Player One is out of cards! Player Two Wins!")
        game_on = False

    if len(player_two.all_cards) == 0:
        print ("Player Two is out of cards! Player One Wins!")
        game_on = False

    # NEW ROUND 

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

# If the cards are the same, War is initialized

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value: #<----- Negative one "[-1]" represents them drawing the top (new) card
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_two_cards[-1].value > player_one_cards[-1].value: 
            
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

            at_war = False

        else:                                                      # <----------- Because cards are not different, they must be the same. Thus, war occurs. 
            print ("WAR!!!") 

            if len(player_one.all_cards) < 3:
                print ("Player One is unable to fight this war!")
                print ("Player Two wins!!!")
                game_on = False 
                break

            elif len(player_two.all_cards) < 3:
                print ("Player Two is unable to fight this war!")
                print ("Player One wins!!!")
                game_on = False 
                break
    
            else: 
                for n in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

                




    

    










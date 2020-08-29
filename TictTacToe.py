# Game Table
from IPython.display import clear_output

players_dict = {}
test_board = [1,2,3,4,5,6,7,8,9]

def display_board(board):
    clear_output()
    print ("    |    |    ")
    print (f" {board[0]}  | {board[1]}  | {board[2]}  ")
    print ("____|____|____")
    print ("    |    |    ")
    print (f" {board[3]}  | {board[4]}  | {board[5]}  ")
    print ("____|____|____")
    print ("    |    |    ")
    print (f" {board[6]}  | {board[7]}  | {board[8]}  ")
    print ("    |    |    ")


# Ask for names
def player_input():
    
    nick1 = " "
    nick2 = " "
    while nick1 == " ":
        nick1 = input ("Player 1, What is your name? ")
    while nick2 == " ":
        nick2 = input ("Player 2, What is your name? ")
        
    # Choose X or O
    
    character1 = " "
    character2 = " "
    while character1 != "X" and character1 != "O":
        character1 = input (f"{nick1}, Choose X or O: ")
    if character1 == "X":
        character2 = "O"
    else:
        character2 = "X"
    
    global players_dict
    players_dict = {"player1nick": nick1, "player1character":character1, "player2nick": nick2, "player2character":character2}
    print (f"{nick1}, you are {character1}")
    print (f"{nick2}, you are {character2}")

    print (f"{nick1}, you go first!")


#Ask for position

def character_position(turn):
    if turn == True:
        nick = players_dict["player1nick"]
        character = players_dict["player1character"]
    else: 
        nick = players_dict["player2nick"]
        character = players_dict["player2character"]
    
    global test_board

    display_board(test_board)

    position = input(f"{nick}, where do you want to place your character? (1-9)")

    while position != "1" and position != "2" and position != "3" and position != "4" and position != "5" and position != "6" and position != "7" and position != "8" and position != "9":  
        position = input(f"{nick}, where do you want to place your character? (1-9)")
    
    if test_board[int(position) - 1] == "X" or test_board[int(position) - 1] == "O":
        print ("Sorry that spot is taken!")
        character_position(turn)
    else: 
        test_board[int(position) - 1] = character
    

# Check if win
def check_win(turn):
    global test_board
    global players_dict
    if turn == True:
        nick = players_dict["player1nick"]
    else: 
        nick = players_dict["player2nick"]
    
    if test_board[0] == "X" or test_board[0] == "O":
        if test_board[1] == test_board[0] and test_board[2] == test_board[0]:
            print (f"Congratulations {nick} you have won!")
            return True
        elif test_board[3] == test_board[0] and test_board[6] == test_board[0]:
            print (f"Congratulations {nick} you have won!")
            return True
        elif test_board[4] == test_board[0] and test_board[8] == test_board[0]:
            print (f"Congratulations {nick} you have won!")
            return True
    
    if test_board[1] == "X" or test_board[1] == "O":
        if test_board[1] == test_board[4] and test_board[1] == test_board[7]:
            print (f"Congratulations {nick} you have won!")
            return True

    if test_board[3] == "X" or test_board[3] == "O":
        if test_board[3] == test_board[4] and test_board[3] == test_board[5]:
            print (f"Congratulations {nick} you have won!")
            return True
    
    if test_board[6] == "X" or test_board[6] == "O":
        if test_board[6] == test_board[7] and test_board[6] == test_board[8]:
            print (f"Congratulations {nick} you have won!")
            return True
    
    if test_board[2] == "X" or test_board[2] == "O":
        if test_board[2] == test_board[5] and test_board[2] == test_board[8]:
            print (f"Congratulations {nick} you have won!")
            return True
        elif test_board[2] == test_board[4] and test_board[2] == test_board[6]:
            print (f"Congratulations {nick} you have won!")
            return True
            

    return False



print ("Welcome to TicTacToe!")    
display_board(test_board)
player_input()
turn = True
won = False 
turns = 0

while not won:
    if turns >= 9:
        print("No one has won!")
        break
    character_position(turn)
    display_board(test_board)
    won = check_win(turn)
    turns = turns + 1
    turn = not turn
    


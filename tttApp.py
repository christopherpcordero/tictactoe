#
#board
#display board
#play game 
#to go back in forth handle a turn 
#--func---
#get win 
    #check rows, columns, diagonals
#check tie
    #entire board if full and no winner
# flip players 

#Global Vars

board = ["-","-","-",
        "-","-","-",
        "-","-","-",]

playing_game = True
winner = None
curr_player = "X"

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' +board[2] )
    print(board[3] + ' | ' + board[4] + ' | ' +board[5] )
    print(board[6] + ' | ' + board[7] + ' | ' +board[8] )


def play_game():    
    #Display initial board
    display_board()

    while playing_game:
        handle_turn(curr_player)

        #check winner
        check_game()

        flip_player()
    
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie.")

#check if game is over
def check_game():
    if_winner()
    if_tie()

def if_winner():
    global winner

    #check rows
    row_winner = check_rows()
    #check cols
    col_winner = check_cols()
    #check diagonals
    dia_winner = check_diagonals()

    if row_winner:
        #there is a win
        winner = row_winner
    elif col_winner:
        #win
        winner = col_winner
    elif dia_winner:
        #win
        winner = dia_winner
    else:
        #no winner
        winner = None
    return
def if_tie():
    global playing_game

    if "-" not in board:
        playing_game = False
    return

def check_rows():

    global playing_game
    #Check for row winner
    # row 1 is index 0-2
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    if row_1 or row_2 or row_3:
        playing_game = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]   
    elif row_3:
        return board[6]
    return

def check_cols():
    global playing_game
    #Check for row winner
    # row 1 is index 0-2
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    
    if col_1 or col_2 or col_3:
        playing_game = False

    if col_1:
        return board[0]
    elif col_2:
        return board[1]   
    elif col_3:
        return board[2]

    return
def check_diagonals():
    global playing_game
    #Check for row winner
    # row 1 is index 0-2
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[6] == board[4] == board[2] != "-"
 
    
    if dia_1 or dia_2:
        playing_game = False

    if dia_1:
        return board[0]
    elif dia_2:
        return board[6]   
    return

def flip_player():
    global curr_player

    if curr_player == 'X':
        curr_player = "O"
    elif curr_player == "O":
        curr_player = "X"
    return  

def handle_turn(player):

    print(player + "'s turn. ")
    position = input("Choose a position from 1 -9: ")
    valid = False
    
    while not valid:
            
        while position not in ["1","2","3",'4','5','6','7','8','9']:
            position = input("Choose a position from 1-9: ")
        
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("Invalid Position. That spot is already used. Go Again.")

    board[position] = player
    display_board()



play_game()


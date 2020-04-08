from random import *
# GLOBAL VARIABLES
play_board = ["-" for play_board in range(0,9)]
current_player = "X" #Starting player
game_in_progress = True
winner = "TBD"

def print_board():
    print(play_board[0] + " | " + play_board[1] + " | " + play_board[2] + "\n" +
          play_board[3] + " | " + play_board[4] + " | " + play_board[5] + "\n" +
          play_board[6] + " | " + play_board[7] + " | " + play_board[8])
        

def play_game():
    print_board()
    global game_in_progress
    while game_in_progress:
        check_if_game_over()
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if not game_in_progress and winner != "TIE":
        print("Gra skończona, wygrał: " + winner)
    elif winner == "TIE":
        print("REMIS")
        game_in_progress = False
    

def handle_turn(player):

    print("Ruch gracza: " + player)
    while True:
        try:
            cell = int(input("Wpisz nr pola 1-9: "))
        except ValueError:
            print("Nie wpisałeś liczby. Popraw się.")       
        else:
            if cell in range(10) and play_board[cell - 1] == "-":
                break
            else:
                print("Cyfra nie w zakresie lub pole jest już pełne")
    cell = cell - 1
    play_board[cell] = player

  

    print_board()

def check_if_game_over():
    global game_in_progress
    global winner

    row_1 = play_board[0] == play_board[1] == play_board[2] !="-"
    row_2 = play_board[3] == play_board[4] == play_board[5] !="-"
    row_3 = play_board[6] == play_board[7] == play_board[8] !="-"
    
    col_1 = play_board[0] == play_board[3] == play_board[6] !="-"
    col_2 = play_board[1] == play_board[4] == play_board[7] !="-"
    col_3 = play_board[2] == play_board[5] == play_board[8] !="-"

    diag_1 = play_board[0] == play_board[4] == play_board[8] !="-"
    diag_2 = play_board[6] == play_board[4] == play_board[2] !="-"

    if row_1 or row_2 or row_3 or col_1 or col_2 or col_3 or diag_1 or diag_2:
        game_in_progress = False
        winner = current_player
    
    if "-" not in play_board:
        winner = "TIE"
        game_in_progress = False
    

    
    return

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

def get_random_player():
    global current_player
    random = randint(0,1)
    if random == 0:
        current_player = "X"
    else:
        current_player = "O"
get_random_player()
play_game()
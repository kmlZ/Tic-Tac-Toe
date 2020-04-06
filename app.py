# GLOBAL VARIABLES
play_board = ["-" for board in range(0,9)]
current_player = "X"
game_in_progress = True
winner = None

def print_board():
    print(play_board[0] + " | " + play_board[1] + " | " + play_board[2] + "\n" +
          play_board[3] + " | " + play_board[4] + " | " + play_board[5] + "\n" +
          play_board[6] + " | " + play_board[7] + " | " + play_board[8])

def play_game():

    while game_in_progress:
        check_if_win()
        check_if_tie()
        handle_turn(current_player)
        print_board()      
        flip_player()

    if winner == "X":
        print("Winner is " + winner)
    elif winner == "O":
        print("Winner is " + winner)
    elif winner == "Tie":
        print("!! TIE !!")

def handle_turn(player):
    print("Teraz ruch gracza: " + player)
    cell = int(input("Wpisz nr komórki 1-9: "))
    cell = cell -1

    play_board[cell] = player

    return

def flip_player():

    global current_player

    if current_player == "X":
        current_player == "O"
    else:
        current_player == "X"      

def check_if_win():
    




play_game()
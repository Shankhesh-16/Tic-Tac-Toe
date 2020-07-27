# BOARD

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

value = "nthng"

playerx = input("Players X's name : ")
playero = input("Players Y's name : ")

current_player = playerx

game_status = True

# Switch player
def switchplayer():
  global current_player

  if current_player == playerx:
    current_player = playero
    return current_player

  elif current_player == playero:
    current_player = playerx
    return current_player

# Converts player choice
def player2choice():
  global current_player
  global value
  if current_player == playerx:
    value = str("X")
    return value
  elif current_player == playero:
    value = str("Y")
    return value

# Plays the game
def play():
  global game_status
  global current_player

  display_board()

  while game_status:
    print(current_player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False

    while not valid:

      while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid. Choose a position from 1-9: ")

      position = int(position) - 1

      if board[position] == "-":
        valid = True
      else:
        print("You can't go there. Go again.")

    board[position] = player2choice()
    display_board()

    if board[0] == board[1] == board[2] != "-" or board[3] == board[4] == board[5] != "-" or board[6] == board[7] == board[8] != "-" :
      print(current_player + " won.")
      game_status = False

    elif board[0] == board[3] == board[6] != "-" or board[1] == board[4] == board[7] != "-" or board[2] == board[5] == board[8] != "-":
      print(current_player + " won.")
      game_status = False

    elif board[0] == board[4] == board[8] != "-" or board[2] == board[4] == board[6] != "-" :
      print(current_player + " won.")
      game_status = False

    elif "-" not in board:
      game_status = False

    switchplayer()

play()

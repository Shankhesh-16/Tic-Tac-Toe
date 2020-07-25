# ---- Global Variables ----

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Who won or tie ?
winner = None

# Whose turn is it?
current_player = "Monica"
 
# ---- FUnctions ----

def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


def play_game():

  # Display initial board 
  display_board()

# While game is still going
  while game_still_going:
     
    # Handle a single turn to a player 
    handle_turn(current_player)

    # Check if game has ended
    check_if_game_over()

    # Flip to the other pllayer
    flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
      print(winner + ' won.')

    elif winner == "tie":
      print("Tie.")


# Handle a single turn to a player 
def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid. Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  if current_player == "Monica":
    board[position] = "X"
  elif current_player == "Chandler":
    board[position] = "O"

  # Show the game board
  display_board()


def check_if_game_over():
  check_if_win()
  check_if_tie()


def check_if_win():
  global winner
  #check row
  row_winner = check_rows()
  #check column
  column_winner = check_columns()
  #check diagonal
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  # Set global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner
  if row_1:
    winner_name = board[0]
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "O":
      print("Chandler won") 

  elif row_2:
    winner_name = board[1] 
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "O":
      print("Chandler won") 

  elif row_3:
    winner_name = board[2]
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "O":
      print("Chandler won") 
  # Or return None if there was no winner
  else:
    return None
  

# Check the columns for a win
def check_columns():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner
  if column_1:
    winner_name = board[0] 
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "O":
      print("Chandler won") 
      
  elif column_2:
    winner_name = board[1] 
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "O":
      print("Chandler won") 

  elif column_3:
    winner_name = board[2]  
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "O":
      print("Chandler won") 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner
  if diagonal_1:
    winner_name = board[0] 
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "O":
      print("Chandler won") 

  elif diagonal_2:
    winner_name = board[2]
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "O":
      print("Chandler won") 
  # Or return None if there was no winner
  else:
    return None
  


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False


def flip_player():
  global current_player

  if current_player == "Monica":
    current_player = "Chandler"
  elif current_player == "Chandler":
    current_player = "Monica"


play_game()

  # Put the game piece on the board
  if current_player == "Monica":
    board[position] = "X"
  elif current_player == "Chandler":
    board[position] = "Y"

  # Show the game board
  display_board()


def check_if_game_over():
  check_if_win()
  check_if_tie()


def check_if_win():
  global winner
  #check row
  row_winner = check_rows()
  #check column
  column_winner = check_columns()
  #check diagonal
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  # Set global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner
  if row_1:
    winner_name = board[0]
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "Y":
      print("Chandler won") 

  elif row_2:
    winner_name = board[1] 
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "Y":
      print("Chandler won") 

  elif row_3:
    winner_name = board[2]
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "Y":
      print("Chandler won") 
  # Or return None if there was no winner
  else:
    return None
  

# Check the columns for a win
def check_columns():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner
  if column_1:
    winner_name = board[0] 
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "Y":
      print("Chandler won") 
      
  elif column_2:
    winner_name = board[1] 
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "Y":
      print("Chandler won") 

  elif column_3:
    winner_name = board[2]  
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "Y":
      print("Chandler won") 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner
  if diagonal_1:
    winner_name = board[0] 
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "Y":
      print("Chandler won") 

  elif diagonal_2:
    winner_name = board[2]
    if winner_name == "X":
      print("Monica won")
    elif winner_name == "Y":
      print("Chandler won") 
  # Or return None if there was no winner
  else:
    return None
  


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False


def flip_player():
  global current_player

  if current_player == "Monica":
    current_player = "Chandler"
  elif current_player == "Chandler":
    current_player = "Monica"


play_game()

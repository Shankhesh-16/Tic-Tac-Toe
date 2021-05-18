board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def displayBoard():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "    1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "    4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "    7 | 8 | 9")
    print("\n")

def playerX():
    choice = input("Where would you like to place X : ")

    position = int(choice) - 1

    if board[position] == "-":
        board[position] = "X"
        displayBoard()

    else:
        print("Position already occupied, Try another Position ?")
        displayBoard()
        playerX()

def playerO():
    choice = input("Where would you like to place O : ")

    position = int(choice) - 1

    if board[position] == "-":
        board[position] = "O"
        displayBoard()

    else:
        print("Position already occupied, Try another Position ?")
        displayBoard()
        playerO()

gameWon = False

def rowChecker():
    global gameWon

    for i in range(1):
        if board[i] == board[i+1] == board[i+2] != "-" and gameWon == False:
            print("Game Won by " + board[i])
            gameWon = True

        elif board[i+3] == board[i+4] == board[i+5] != "-" and gameWon == False:
            print("Game Won by " + board[i+3])
            gameWon = True

        elif board[i+6] == board[i+7] == board[i+8] != "-" and gameWon == False:
            print("Game Won by " + board[i+3])
            gameWon = True

def rowChecker():
    global gameWon

    for i in range(1):
        if board[i] == board[i+1] == board[i+2] != "-" and gameWon == False:
            print("Game Won by " + board[i])
            gameWon = True

        elif board[i+3] == board[i+4] == board[i+5] != "-" and gameWon == False:
            print("Game Won by " + board[i+3])
            gameWon = True

        elif board[i+6] == board[i+7] == board[i+8] != "-" and gameWon == False:
            print("Game Won by " + board[i+6])
            gameWon = True

def columnChecker():
    global gameWon

    for i in range(1):
        if board[i] == board[i+3] == board[i+6] != "-" and gameWon == False:
            print("Game Won by " + board[i])
            gameWon = True

        elif board[i+1] == board[i+4] == board[i+7] != "-" and gameWon == False:
            print("Game Won by " + board[i+1])
            gameWon = True

        elif board[i+2] == board[i+5] == board[i+8] != "-" and gameWon == False:
            print("Game Won by " + board[i+2])
            gameWon = True

def diagonalChecker():
    global gameWon

    for i in range(1):
        if board[i] == board[i+4] == board[i+8] != "-" and gameWon == False:
            print("Game Won by " + board[i])
            gameWon = True


        elif board[i+2] == board[i+4] == board[i+6] != "-" and gameWon == False:
            print("Game Won by " + board[i+2])
            gameWon = True

gameTie = False

def tieChecker():
    global gameTie
    if "-" not in board:
        gameTie = True
        print("There's a Tie, Play again?")

def checker():
    rowChecker()
    columnChecker()
    diagonalChecker()
    tieChecker()

def play():
    global gameTie
    global gameWon
    displayBoard()

    stop = 1
    while stop < 99 :
         if gameWon == False and gameTie == False:
            playerX()
            checker()
            if gameWon == False and gameTie == False:
                playerO()
                checker()
         elif gameWon == True or gameTie == True:
            stop = 100

play()


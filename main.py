from random import randrange


freeSpaces = []
moveCount = 1
isTie = False

def Main():
    board = [[1,2,3],[4,"X",6],[7,8,9]]
    
    #core game loop
    while True:
        if MakeListOfFreeFields(board) == 0:
            DisplayBoard(board)
            isTie = True
            print("The game ended in a tie!")
            break
        DisplayBoard(board)
        EnterMove(board,)
        if (VictoryFor(board, "O")):
            break        
        DrawMove(board)
        if (VictoryFor(board, "X")):
            break
        
    playAgain = input("Would you like to play again? (y/n): ")
    if (playAgain == "y" or playAgain == "Y"):
        Main()
    else:
        exit()


#the function accepts one parameter containing the board's current status
def DisplayBoard(board):
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+""")


# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
def EnterMove(board):
    playerMove = int(input("Enter your move: "))
    MakeListOfFreeFields(board)
    if playerMove in freeSpaces:
        for row in board:
            for column in row:                
                if(column == playerMove):
                    board[board.index(row)][row.index(column)] = "O"
                                       
    else:
        print("Sorry that is not a valid space.")
        EnterMove(board)

# the function browses the board and builds a list of all the free squares; 
def MakeListOfFreeFields(board):
    freeSpaces.clear()
    for row in board:
        for column in row:
            if(isinstance(column, int)):
                freeSpaces.append(column)
    if len(freeSpaces) == 0:
        return 0


# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
def VictoryFor(board, sign):
    if (#horizontal win conditions:
        board[0][0] == board[0][1] and board[0][1] == board[0][2] or
        board[1][0] == board[1][1] and board[1][1] == board[1][2] or
        board[2][0] == board[2][1] and board[2][1] == board[2][2] or
        #vertical win conditions:
        board[0][0] == board[1][0] and board[1][0] == board[2][0] or
        board[0][1] == board[1][1] and board[1][1] == board[2][1] or
        board[0][2] == board[1][2] and board[1][2] == board[2][2] or
        #diagonal win conditions
        board[0][0] == board[1][1] and board[1][1] == board[2][2] or
        board[2][0] == board[1][1] and board[1][1] == board[0][2]        
        ):
        DisplayBoard(board)
        print(f'Victory for "{sign}"!')
        return True
    else:
        return False

        
# the function draws the computer's move and updates the board
def DrawMove(board):
    MakeListOfFreeFields(board)
    randomFreeField = randrange(len(freeSpaces))
    computerMove = freeSpaces[randomFreeField]
    for row in board:
        for column in row:                
           if(column == computerMove):
               board[board.index(row)][row.index(column)] = "X"
               DisplayBoard(board)
    
Main()




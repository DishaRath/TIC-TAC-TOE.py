

"""
Tic Tc Toe Player
"""



import math
import copy

X = 'X'
O = 'O'
EMPTY = None


def initial_state()
    """
    Returns starting state of the board.
    """
    return[[EMPTY,EMPTY,EMPTY],
           [EMPTY,EMPTY,EMPTY],
           [EMPTY,EMPTY,EMPTY]]

def player(board):
    """
    Returns stating state of the board.
    """
    countX = 0
    count0 = 0

    for row in range(len(board)):
        for col in range(len(board[0])): 
            if board[row][col] == x:
                countX += 1
            if board[row][col] == 0:
                count0 += 1


    if countX > count0:
        return 0
     else:
         return X 


def actions(board):
    """
    Returns set of all possible actions (i,j) available on the board.
    """
    allPossibleActions = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY
               allPossibleActions.add((row,col))

    return allPossibleActions


def result(board,action):
    """
    Returns the board that results from making move(i,j) on the board.
    """
    if action not in actions(board):
        raise Expection("Not valid action")
    

    row,col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy

def checkRow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkCol(board,player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
        return False

def chcekFirstDig(board,player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count +=1
    if count == 3:
        return True
    else:
        return False

def chcekSecondDig(board,player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row -1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board,X) or checkCol(board,X) or checkFirstDig(board,X) or checkSecondDig(board,X):
        return X
    elif checkRow(board,0) or checkCol(board,X) or checkFirstDig(board,0) or checkSecondDig(board,0):
        return 0
    else:
        return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == 0:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if 0 has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == 0:
        return -1
    else:
        return 0

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
return v




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        returns None

    # Case of player is X (max-player)
    elif player(board) == X:
        plays = []

        # Loop over the possible actions
        for action in actions(board):

            # Add in plays list a tupple with the min_value and the action that results to its value
            plays.append((min_value(result(board,action)),action))

        # Reverse sort for the plays list and get the action that should take
        return sorted(plays, key=lambda x: x[0],reverse=True)[0][1]


    # Case of player is 0
    elif player(board) == X:
        plays = []

        # Loop over the possible actions
        for action in actions(board):

            # Add in plays list a tupple with the min_value and the action that results to its value
            plays.append((min_value(result(board,action)),action))

        # Reverse sort for the plays list and get the action that should take
        return sorted(plays, key=lambda x: x[0],reverse=True)[0][1]

       

    
















        

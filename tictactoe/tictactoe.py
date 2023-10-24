"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0

    for row in board:
        xCount += row.count(X)
        oCount += row.count(O)

    if oCount < xCount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleActions.append((i,j))
            print(possibleActions)
    
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    if board[i,j] != EMPTY:
        raise Exception("Invalid action")

    if i not in [0,1,2] or j not in [0,1,2]:
        raise Exception("i or j not valid")
    
    nextBoard = board
    nextBoard[i,j] = player(board)

    return nextBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in board: # checks the rows if there are 3 Xs or 3 Os
        if i.count(X) == 3:
            return X
        if i.count(O) == 3:
            return O
    
    for j in range(3): # checks the columns if there are 3 Xs or 3 Os
        vertical = ""
        for i in range(3):
            vertical += str(board[i][j])

    if vertical.count(X) == 3:
            return X
    if vertical.count(O) == 3:
            return O

    diag1 = ""
    diag2 = ""
    for i in range(3): # determines the main diagonal(top-left to bottom-right)
        diag1 += str(board[i][i])
    for i in range(3): # determines the second diagonal(top-right to bottom-left)
        diag2 += str(board[i][2-i])

    if diag1.count(X) == 3: # if the diagonal is (xxx)
        return X
    if diag2.count(O) == 3: # if the diagonal is (ooo) 
        return O

    return None # if the board is not a terminal state or tie state


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) or not actions(board):
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board) == True:
        return None
    
        

    # raise NotImplementedError

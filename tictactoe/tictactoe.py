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
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

actions(initial_state())
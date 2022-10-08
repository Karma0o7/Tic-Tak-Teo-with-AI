"""
Tic Tac Toe Player
"""

import math
import copy


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
    Xcount = 0
    Ocount = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                Xcount += 1
            elif board[i][j] == O:
                Ocount += 1
    
    if Xcount > Ocount:
        return O
    else:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    Available_Actions = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                Available_Actions.add((i,j))

    return Available_Actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
 

    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    

    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in i for i in board) and winner(board) is None):
        return True
    else:
        return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(terminal(board)):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    MaxVal = -math.inf
    move = None
    for action in actions(board):
        currentVal, act = min_value(result(board, action))
        if currentVal > MaxVal:
            MaxVal = currentVal
            move = action
            if MaxVal == 1:
                return MaxVal, move

    return MaxVal, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    MinVal = math.inf
    move = None
    for action in actions(board):
        currentVal, act = max_value(result(board, action))
        if currentVal < MinVal:
            MinVal = currentVal
            move = action
            if MinVal == -1:
                return MinVal, move

    return MinVal, move
'''Helper functions that regulate bot behaviour.'''
import random

from assets import Difficulty
from components import Board
from helper import board_helper as BoardHelper


def calculate_next_move(difficulty: int, board: Board, possible_moves: list[int]) -> int:
    '''
    - Easy just throws random.
      Therefore easy will likely loose.
    - Medium difficulty moves are:
        - stopping the other players winning move
        - other than that, are random
      Therefore medium should try to get a draw.
    - Hard difficulty moves are:
        - stopping the other players winning move
        - try to get 4 in a row by
        - other than that, are random
      Therefore hard should try to get a win.
    - Extreme difficulty moves are:
        - same as hard
        - not dropping coins where the player could win next turn
    '''
    if difficulty >= Difficulty.HARD.value:
        # try to win
        for move in possible_moves:
            if _move_as(board=board,
                        move=move,
                        player=2):
                return move
    if difficulty >= Difficulty.EXTREME.value:
        # make safe moves
        safe_moves = []
        for move in possible_moves:
            if _move_is_safe(board, move):
                safe_moves.append(move)
        for move in safe_moves:
            if _move_as(board=board,
                        move=move,
                        player=1):
                return move
        return random.choice(safe_moves)
    if difficulty >= Difficulty.MEDIUM.value:
        for move in possible_moves:
            # prevent win
            if _move_as(board=board,
                        move=move,
                        player=1):
                return move
    return random.choice(possible_moves)


def _move_is_safe(board: Board, move: int) -> bool:
    abstract_board = board.get_abstract_board()
    affected_cells = BoardHelper.get_cells_in_col(abstract_board, move)
    affected_cells.reverse()
    for cell in affected_cells:
        if cell.is_empty():
            cell.current_player = 2
            break
    if BoardHelper.has_connected_four(board_cells=abstract_board,
                                      cols=board.cols,
                                      rows=board.rows):
        return True
    if BoardHelper.board_is_full(abstract_board):
        return True
    for cell in affected_cells:
        if cell.is_empty():
            cell.current_player = 1
            break
    if BoardHelper.has_connected_four(board_cells=abstract_board,
                                      cols=board.cols,
                                      rows=board.rows):
        return False
    if BoardHelper.board_is_full(abstract_board):
        return True
    return True


def _move_as(board: Board, move: int, player: int) -> bool:
    abstract_board = board.get_abstract_board()
    affected_cells = BoardHelper.get_cells_in_col(abstract_board, move)
    affected_cells.reverse()
    for cell in affected_cells:
        if cell.is_empty():
            cell.current_player = player
            break
    if BoardHelper.has_connected_four(board_cells=abstract_board,
                                      cols=board.cols,
                                      rows=board.rows):
        return True
    if BoardHelper.board_is_full(abstract_board):
        return True
    return False

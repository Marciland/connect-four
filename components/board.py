'''component class for managing the board.'''
from typing import TYPE_CHECKING

from assets import AbstractCell, Cell, EntryPoint, Position
from helper import board_helper as BoardHelper

if TYPE_CHECKING:
    from components import GameFrame


class Board:
    '''Board component for the connect four game.'''

    def __init__(self, frame) -> None:
        self.frame: GameFrame = frame
        self.rows = 6
        self.cols = 7
        self.entry_points: dict[int, EntryPoint] = {}
        self.cells: dict[Position, Cell] = {}
        self._prepare_board()

    def _prepare_board(self) -> None:
        '''Creates an empty board by placing all necessary widgets.'''
        for col_index in range(0, self.cols, 1):
            entry_point = EntryPoint(board=self,
                                     col_index=col_index)
            self.entry_points.update({col_index: entry_point})
            for row_index in range(0, self.rows, 1):
                cell = Cell(board=self,
                            col_index=col_index,
                            row_index=row_index)
                self.cells.update({Position(x=col_index, y=row_index): cell})

    def get_abstract_board(self) -> dict[Position, AbstractCell]:
        '''Converts the current board's state to an abstract board for computation.'''
        abstract_board: dict[Position, AbstractCell] = {}
        for pos, cell in self.cells.items():
            abstract_cell = AbstractCell(col_index=cell.col_index,
                                         row_index=cell.row_index)
            abstract_cell.current_player = cell.current_player
            abstract_board.update({pos: abstract_cell})
        return abstract_board

    def get_possible_moves(self) -> list[int]:
        '''This prevents coin_dropped = False for the bot.'''
        return [col for col in range(0, self.cols, 1)
                if BoardHelper.has_empty_cell(BoardHelper.get_cells_in_col(self.cells, col))]

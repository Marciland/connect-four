'''component class for managing the board.'''
from .cell import Cell
from .entry_point import EntryPoint


class Board:
    '''Board component for the connect four game.'''

    def __init__(self, window) -> None:
        self.window = window
        self.entry_points = {}
        self.cells = {}

        self._prepare_board()

    def _prepare_board(self) -> None:
        '''Creates an empty board by placing all necessary widgets.'''
        for col_index in range(0, 7, 1):
            entry_point = EntryPoint(self.window, col_index)
            self.entry_points.update({col_index: entry_point})
            for row_index in range(1, 7, 1):
                cell = Cell(self.window, col_index, row_index)
                self.cells.update({
                    f'{col_index}x{row_index-1}': cell
                })

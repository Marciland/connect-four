'''component class for managing the board.'''
import tkinter as ttk


class Board:
    '''Board component for the connect four game.'''

    def __init__(self, window) -> None:
        self.window = window
        self.entry_points = {}
        self.cells = {}

        self._prepare_board()

    def _prepare_board(self) -> None:
        '''Initially places all necessary widgets.'''
        for col_index in range(0, 7, 1):
            entry_point = ttk.Button(self.window)
            entry_point.place(x=100*col_index, y=0, width=100, height=100)
            self.entry_points.update({col_index: entry_point})
            for row_index in range(1, 7, 1):
                cell = ttk.Label(self.window,
                                 text=f'{col_index}x{row_index}')
                cell.place(x=100*col_index,
                           y=100 * row_index,
                           width=100,
                           height=100)
                self.cells.update({
                    f'{col_index}x{row_index}': cell
                })

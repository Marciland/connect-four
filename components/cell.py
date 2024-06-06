'''Cell used on the board.'''
import tkinter as ttk
from os import getcwd, path


class Cell:
    '''Cell component that represents a piece of the board.'''

    def __init__(self, window, col_index: int, row_index: int) -> None:
        self.window = window
        self.col_index = col_index
        self.row_index = row_index
        cwd = getcwd()
        self.paths = {
            'empty_board': path.join(cwd, 'res/empty_board.png'),
            'purple_board': path.join(cwd, 'res/purple_board.png'),
            'yellow_board': path.join(cwd, 'res/yellow_board.png')
        }

        self._prepare_cell()

    def _prepare_cell(self) -> None:
        '''Creates a new cell in its initial state.'''
        self.image = ttk.PhotoImage(file=self.paths['empty_board'])
        self.widget = ttk.Label(self.window, image=self.image)
        self.widget.place(x=100 * self.col_index,
                          y=100 * self.row_index,
                          width=100,
                          height=100)

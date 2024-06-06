'''Cell used on the board.'''
import tkinter as ttk
from os import getcwd, path


class Cell:
    '''Cell component that represents a piece of the board.'''

    def __init__(self, window, col_index: int, row_index: int) -> None:
        self.window = window
        self.col_index = col_index
        self.row_index = row_index
        self.is_empty = True
        cwd = getcwd()
        self.empty_image = ttk.PhotoImage(file=path.join(cwd,
                                                         'res/empty_board.png'))
        self.player1_image = ttk.PhotoImage(file=path.join(cwd,
                                                           'res/purple_board.png'))
        self.player2_image = ttk.PhotoImage(file=path.join(cwd,
                                                           'res/yellow_board.png'))
        self._prepare_cell()

    def _prepare_cell(self) -> None:
        '''Creates a new cell in its initial state.'''
        self.widget = ttk.Label(self.window, image=self.empty_image)
        self.widget.place(x=100 * self.col_index,
                          y=100 * self.row_index,
                          width=100,
                          height=100)

    def change_state(self, player: int) -> None:
        '''Changes the rendered image based on player given.'''
        match player:
            case 1:
                self.widget.configure(image=self.player1_image)
            case 2:
                self.widget.configure(image=self.player2_image)
            case _:
                raise NotImplementedError(f'Player {player} not supported!')
        self.is_empty = False

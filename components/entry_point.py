'''entry point component'''
import tkinter as ttk
from os import getcwd, path


class EntryPoint:
    '''Entry for the coins above the board'''

    def __init__(self, window, col_index) -> None:
        self.window = window
        self.col_index = col_index
        cwd = getcwd()
        self.empty_image = ttk.PhotoImage(file=path.join(cwd,
                                                         'res/empty_entry.png'))
        self.player1_image = ttk.PhotoImage(file=path.join(cwd,
                                                           'res/purple_entry.png'))
        self.player2_image = ttk.PhotoImage(file=path.join(cwd,
                                                           'res/yellow_entry.png'))
        self._prepare_entry_point()

    def _prepare_entry_point(self) -> None:
        self.widget = ttk.Button(self.window, image=self.empty_image)
        self.widget.place(x=100 * self.col_index,
                          y=0,
                          width=100,
                          height=100)

    def change_state(self, player: int) -> None:
        '''Changes the visuals based on current player.'''
        match player:
            case 0:
                # 0 equals no player and renders empty
                self.widget.configure(image=self.empty_image)
            case 1:
                self.widget.configure(image=self.player1_image)
            case 2:
                self.widget.configure(image=self.player2_image)
            case _:
                raise NotImplementedError(f'Player {player} not supported!')

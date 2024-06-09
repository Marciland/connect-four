'''entry point component'''
from os import getcwd, path
from tkinter import Button, PhotoImage


class EntryPoint:
    '''Entry for the coins above the board'''

    def __init__(self, window, col_index) -> None:
        self.window = window
        self.col_index = col_index
        cwd = getcwd()
        self.images = {
            'empty': PhotoImage(file=path.join(cwd, 'res/empty_entry.png')),
            'player1': PhotoImage(file=path.join(cwd, 'res/purple_entry.png')),
            'player2': PhotoImage(file=path.join(cwd, 'res/yellow_entry.png'))
        }
        self._prepare_entry_point()

    def _prepare_entry_point(self) -> None:
        self.widget = Button(self.window, image=self.images['empty'])
        self.widget.place(x=100 * self.col_index,
                          y=0,
                          width=100,
                          height=100)

    def change_state(self, player: int) -> None:
        '''Changes the visuals based on current player.'''
        match player:
            case 0:
                # 0 equals no player and renders empty
                self.widget.configure(image=self.images['empty'])
            case 1:
                self.widget.configure(image=self.images['player1'])
            case 2:
                self.widget.configure(image=self.images['player2'])
            case _:
                raise NotImplementedError(f'Player {player} not supported!')

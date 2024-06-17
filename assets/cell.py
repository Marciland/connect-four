'''Cell used on the board.'''
from os import getcwd, path
from tkinter import Label, PhotoImage


class AbstractCell:  # pylint: disable=too-few-public-methods
    '''An abstract cell is for computing only and will not render anything.'''

    def __init__(self, col_index: int, row_index: int) -> None:
        self.col_index: int = col_index
        self.row_index: int = row_index
        self.current_player: int = -1

    def is_empty(self) -> bool:
        '''
        Cells are empty if no color is rendered.
        Thus current_player is at its default value.
        '''
        if self.current_player == -1:
            return True
        return False


class Cell(AbstractCell):
    '''Cell component that represents a piece of the board.'''

    def __init__(self, window, col_index: int, row_index: int) -> None:
        super().__init__(col_index=col_index,
                         row_index=row_index)
        self.window = window
        cwd = getcwd()
        self.images = {
            'empty': PhotoImage(file=path.join(cwd, 'res/cell/empty_cell.png')),
            'player1': PhotoImage(file=path.join(cwd, 'res/cell/purple_cell.png')),
            'player2': PhotoImage(file=path.join(cwd, 'res/cell/yellow_cell.png'))
        }
        self._prepare_cell()

    def _prepare_cell(self) -> None:
        '''Creates a new cell in its initial state.'''
        self.widget = Label(self.window, image=self.images['empty'])
        self.widget.place(x=100 * self.col_index,
                          # y + 100 because of the EntryPoints above
                          y=100 + 100 * self.row_index,
                          width=100,
                          height=100)

    def change_state(self, player: int) -> None:
        '''Changes the rendered image based on player given.'''
        match player:
            case 1:
                self.widget.configure(image=self.images['player1'])
                self.current_player = 1
            case 2:
                self.widget.configure(image=self.images['player2'])
                self.current_player = 2
            case 0:
                # bot is considered 0 and acts as player 2!
                self.widget.configure(image=self.images['player2'])
                self.current_player = 2
            case _:
                raise NotImplementedError(f'Player {player} not supported!')

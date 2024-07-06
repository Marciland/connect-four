'''Cell used on the board.'''
from tkinter import Label
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from components import Board


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

    def __init__(self, board, col_index: int, row_index: int) -> None:
        super().__init__(col_index=col_index,
                         row_index=row_index)
        self.board: Board = board
        self.width = self.board.frame.window.settings.resolution.width // self.board.cols
        self.height = self.width
        self._prepare_cell()

    def _prepare_cell(self) -> None:
        '''Creates a new cell in its initial state.'''
        self.widget = Label(master=self.board.frame,
                            image=self.board.frame.window.resources.images['cell']['empty'])
        self.widget.place(x=self.width * self.col_index,
                          # +1 because of the EntryPoints above
                          y=self.height * (self.row_index + 1),
                          width=self.width,
                          height=self.height)

    def change_state(self, player: int) -> None:
        '''Changes the rendered image based on player given.'''
        match player:
            case 1:
                self.widget.configure(image=self.board.frame.window
                                      .resources.images['cell']['player1'])
                self.current_player = 1
            case 2:
                self.widget.configure(image=self.board.frame.window
                                      .resources.images['cell']['player2'])
                self.current_player = 2
            case _:
                raise NotImplementedError(f'Player {player} not supported!')

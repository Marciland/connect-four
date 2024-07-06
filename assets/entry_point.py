'''entry point component'''
from tkinter import Button
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from components import Board


class EntryPoint:  # pylint: disable=too-few-public-methods
    '''Entry for the coins above the board'''

    def __init__(self, board, col_index) -> None:
        self.board: Board = board
        self.col_index = col_index
        self.width = self.board.frame.window.settings.resolution.width // self.board.cols
        self.height = self.width
        self._prepare_entry_point()

    def _prepare_entry_point(self) -> None:
        self.widget = Button(master=self.board.frame,
                             image=self.board.frame.window
                             .resources.images['entry']['empty'])
        self.widget.place(x=self.width * self.col_index,
                          y=0,
                          width=self.width,
                          height=self.height)

    def change_state(self, player: int) -> None:
        '''Changes the visuals based on current player.'''
        match player:
            case -1:
                # -1 equals no player and renders empty
                self.widget.configure(image=self.board.frame.window
                                      .resources.images['entry']['empty'])
            case 1:
                self.widget.configure(image=self.board.frame.window
                                      .resources.images['entry']['player1'])
            case 2:
                self.widget.configure(image=self.board.frame.window
                                      .resources.images['entry']['player2'])
            case _:
                raise NotImplementedError(f'Player {player} not supported!')

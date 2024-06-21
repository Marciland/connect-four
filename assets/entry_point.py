'''entry point component'''
from os import getcwd, path
from tkinter import Button, PhotoImage
from typing import TYPE_CHECKING

from .dataclasses import Resolution

if TYPE_CHECKING:
    from components import Board


class EntryPoint:  # pylint: disable=too-few-public-methods
    '''Entry for the coins above the board'''

    def __init__(self, board, col_index) -> None:
        self.board: Board = board
        self.col_index = col_index
        self.width = self.board.frame.window.settings.resolution.width // self.board.cols
        self.height = self.width
        self.images: dict[str, PhotoImage] = self._prepare_images()
        self._prepare_entry_point()

    def _prepare_images(self) -> dict[str, PhotoImage]:
        cwd = getcwd()
        base_path = path.join(cwd, 'res', 'entry_point')
        empty_image = PhotoImage(file=path.join(base_path,
                                                'empty_entry.png'))
        player1_image = PhotoImage(file=path.join(base_path,
                                                  'purple_entry.png'))
        player2_image = PhotoImage(file=path.join(base_path,
                                                  'yellow_entry.png'))
        if self.board.frame.window.settings.resolution == Resolution.SMALL.value:
            empty_image = empty_image.subsample(7).zoom(5)
            player1_image = player1_image.subsample(7).zoom(5)
            player2_image = player2_image.subsample(7).zoom(5)
        return {
            'empty': empty_image,
            'player1': player1_image,
            'player2': player2_image
        }

    def _prepare_entry_point(self) -> None:
        self.widget = Button(master=self.board.frame,
                             image=self.images['empty'])
        self.widget.place(x=self.width * self.col_index,
                          y=0,
                          width=self.width,
                          height=self.height)

    def change_state(self, player: int) -> None:
        '''Changes the visuals based on current player.'''
        match player:
            case -1:
                # -1 equals no player and renders empty
                self.widget.configure(image=self.images['empty'])
            case 1:
                self.widget.configure(image=self.images['player1'])
            case 2:
                self.widget.configure(image=self.images['player2'])
            case 0:
                # 0 equals bot and acts as player 2
                self.widget.configure(image=self.images['player2'])
            case _:
                raise NotImplementedError(f'Player {player} not supported!')

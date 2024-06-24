'''Cell used on the board.'''
from os import getcwd, path
from tkinter import Label, PhotoImage
from typing import TYPE_CHECKING

from .dataclasses import Resolution

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
        self.images: dict[str, PhotoImage] = self._prepare_images()
        self._prepare_cell()

    def _prepare_images(self) -> dict[str, PhotoImage]:
        cwd = getcwd()
        base_path = path.join(cwd, 'res', 'cell')
        empty_image = PhotoImage(file=path.join(base_path,
                                                'empty_cell.png'))
        player1_image = PhotoImage(file=path.join(base_path,
                                                  'purple_cell.png'))
        player2_image = PhotoImage(file=path.join(base_path,
                                                  'yellow_cell.png'))
        if self.board.frame.window.settings.resolution == Resolution.SMALL.value:
            empty_image = empty_image.subsample(7).zoom(5)
            player1_image = player1_image.subsample(7).zoom(5)
            player2_image = player2_image.subsample(7).zoom(5)
        return {
            'empty': empty_image,
            'player1': player1_image,
            'player2': player2_image
        }

    def _prepare_cell(self) -> None:
        '''Creates a new cell in its initial state.'''
        self.widget = Label(master=self.board.frame,
                            image=self.images['empty'])
        self.widget.place(x=self.width * self.col_index,
                          # +1 because of the EntryPoints above
                          y=self.height * (self.row_index + 1),
                          width=self.width,
                          height=self.height)

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

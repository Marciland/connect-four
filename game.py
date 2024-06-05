'''game class to play connect four.'''
from tkinter import Tk
from components import Board


class ConnectFour:
    '''Provides a game window with a connect four board.'''

    def __init__(self) -> None:
        self.root = Tk()
        self.width = 700
        self.height = 700

        self._configure_window()

        self.board = Board(window=self.root)
        for index, entry_point in self.board.entry_points.items():
            entry_point.configure(command=lambda i=index: self._drop_coin(i))
        # TODO manipulate this way:
        # self.board.cells['0x1']

    def _configure_window(self) -> None:
        '''
        Modifies the window to its desired initial state.
        '''
        self.root.title('Vier Gewinnt | Connect Four')
        self.root.resizable(False, False)
        self.root.geometry(self._get_geometry())

    def _get_geometry(self) -> str:
        '''
        Returns a geometry string of the tkinter format:
        width x height + startx + starty

        The geometry string is used to determine
        where the window is placed
        and what size it has.
        '''
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        startx = screen_w//2 - self.width//2
        starty = screen_h//2 - self.height//2
        return f'{self.width}x{self.height}+{startx}+{starty}'

    def run(self) -> None:
        '''Runs the game.'''
        self.root.mainloop()

    def _drop_coin(self, entry_point: int) -> None:
        # TODO
        print(f'Dropping coin at: {entry_point}')

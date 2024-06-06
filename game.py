'''game class to play connect four.'''
from tkinter import Tk
from components import Board


class ConnectFour:
    '''Provides a game window with a connect four board.'''

    def __init__(self) -> None:
        self.root = Tk()
        self.width = 700
        self.height = 700
        self.current_player = 1

        self._configure_window()

        self.board = Board(window=self.root)
        for index, entry_point in self.board.entry_points.items():
            entry_point.widget.configure(command=lambda i=index:
                                         self._drop_coin(i))
            entry_point.widget.bind("<Enter>", lambda _, entry=entry_point:
                                    entry.change_state(self.current_player))
            entry_point.widget.bind("<Leave>", lambda _, entry=entry_point:
                                    entry.change_state(0))

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

    def _drop_coin(self, col_index: int) -> None:
        affected_cells = []
        for pos, cell in self.board.cells.items():
            # position is 'colxrow'
            if len(affected_cells) == 6:
                break
            if f'{col_index}x' not in pos:
                continue
            affected_cells.append((pos, cell))
        # start at the bottom of the board (row=5)
        affected_cells.reverse()
        coin_dropped = False
        for cell in affected_cells:
            if cell[1].is_empty:
                cell[1].change_state(self.current_player)
                coin_dropped = True
                break
        # only change current player if a coin was actually dropped
        if coin_dropped:
            self.board.entry_points[col_index].change_state(0)
            # TODO: check win condition here, current_player can win, else change current_player
            self.current_player = 1 if self.current_player == 2 else 2

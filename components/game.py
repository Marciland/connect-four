'''Contains the games that can be played.'''
from tkinter import Frame, messagebox

from assets import Cell
from components import Board


class ConnectFour(Frame):
    '''Provides a game frame with a connect four board.'''

    def __init__(self, window) -> None:
        super().__init__(master=window)
        self.window = window
        self.width = 700
        self.height = 700
        self.current_player = 1
        self._new_game()

    def _new_game(self) -> None:
        '''Sets up a new game.'''
        self.board = Board(window=self)
        for index, entry_point in self.board.entry_points.items():
            entry_point.widget.configure(state='normal')
            entry_point.widget.configure(command=lambda i=index:
                                         self._drop_coin(i))
            entry_point.widget.bind("<Enter>", lambda _, entry=entry_point:
                                    entry.change_state(self.current_player))
            entry_point.widget.bind("<Leave>", lambda _, entry=entry_point:
                                    entry.change_state(0))

    def _end_game(self, remis: bool) -> None:
        '''Stops interactivity and asks for a new game.'''
        for _, entry_point in self.board.entry_points.items():
            entry_point.widget.configure(state='disabled')
            entry_point.widget.unbind("<Enter>")
            entry_point.widget.unbind("<Leave>")
        msg = f'Player {self.current_player} has won!\nPlay again?'
        if remis:
            msg = 'Draw!\nPlay again?'
        replay_window = messagebox.Message(master=self,
                                           icon=messagebox.QUESTION,
                                           title='Game ends!',
                                           message=msg,
                                           type=messagebox.RETRYCANCEL)
        response = replay_window.show()
        if response == messagebox.RETRY:
            self._new_game()
        if response == messagebox.CANCEL:
            self.window.show_main_menu()

    def _drop_coin(self, col_index: int) -> None:
        affected_cells: list[Cell] = []
        for pos, cell in self.board.cells.items():
            if len(affected_cells) == self.board.rows:
                break
            if f'{col_index}x' not in pos:
                continue
            affected_cells.append(cell)
        # start at the bottom of the board
        affected_cells.reverse()
        coin_dropped = False
        for cell in affected_cells:
            if cell.is_empty():
                cell.change_state(self.current_player)
                coin_dropped = True
                break
        if not coin_dropped:
            # skip win conditions if nothing happened, also do not swap current player!
            return None
        self.board.entry_points[col_index].change_state(0)
        if self.board.is_full():
            return self._end_game(remis=True)
        if self.board.connected_four():
            return self._end_game(remis=False)
        self.current_player = 1 if self.current_player == 2 else 2
        return None

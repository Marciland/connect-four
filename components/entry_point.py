'''entry point component'''
import tkinter as ttk
from os import getcwd, path


class EntryPoint:
    '''Entry for the coins above the board'''

    def __init__(self, window, col_index) -> None:
        self.window = window
        self.col_index = col_index
        cwd = getcwd()
        self.hover_image = ttk.PhotoImage(file=path.join(cwd,
                                                         'res/hovered_entry.png'))
        self.player1_image = ttk.PhotoImage(file=path.join(cwd,
                                                           'res/purple_entry.png'))
        self.player2_image = ttk.PhotoImage(file=path.join(cwd,
                                                           'res/yellow_entry.png'))
        self._prepare_entry_point()

    def _prepare_entry_point(self) -> None:
        self.widget = ttk.Button(self.window, image=self.hover_image)
        self.widget.bind("<Enter>", self._on_enter)
        self.widget.bind("<Leave>", self._on_leave)
        self.widget.place(x=100 * self.col_index,
                          y=0,
                          width=100,
                          height=100)

    def _on_enter(self, _) -> None:
        self.widget.configure(image=self.hover_image)

    def _on_leave(self, _) -> None:
        self.widget.configure(image=self.hover_image)

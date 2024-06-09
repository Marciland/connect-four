'''contains all menu components.'''
from os import getcwd, path
from tkinter import Button, Frame, Label, PhotoImage


class MainMenu(Frame):
    '''Creates a menu frame for the player to select the game mode.'''

    def __init__(self, window) -> None:
        super().__init__(master=window)
        self.window = window
        self.width = 700
        self.height = 700
        cwd = getcwd()
        self.images = {
            'background': PhotoImage(file=path.join(cwd, 'res/menu_background.png')),
            'singleplayer': PhotoImage(file=path.join(cwd, 'res/singleplayer.png')),
            'multiplayer': PhotoImage(file=path.join(cwd, 'res/multiplayer.png')),
            'settings': PhotoImage(file=path.join(cwd, 'res/settings.png')),
            'exit': PhotoImage(file=path.join(cwd, 'res/exit.png'))
        }
        self._prepare_menu()

    def _prepare_menu(self) -> None:
        background = Label(master=self.window,
                           image=self.images['background'])
        background.place(x=0, y=0,
                         width=self.width, height=self.height)
        single_player = Button(master=self.window,
                               image=self.images['singleplayer'])
        single_player.place(x=150, y=50, width=400, height=100)
        single_player.lift(background)
        multiplayer = Button(master=self.window,
                             image=self.images['multiplayer'],
                             command=self.window.start_multiplayer)
        multiplayer.place(x=150, y=200, width=400, height=100)
        multiplayer.lift(background)
        settings = Button(master=self.window,
                          image=self.images['settings'])
        settings.place(x=150, y=350, width=400, height=100)
        settings.lift(background)
        exit_game = Button(master=self.window,
                           image=self.images['exit'],
                           command=self.window.destroy)
        exit_game.place(x=150, y=550, width=400, height=100)
        exit_game.lift(background)

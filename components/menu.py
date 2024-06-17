'''contains all menu components.'''
from os import getcwd, path
from tkinter import Button, Frame, Label, PhotoImage


class MenuFrame(Frame):
    '''Frame extension for the game's menu.'''

    def __init__(self, window) -> None:
        super().__init__(master=window)
        self.window = window
        self.width = 700
        self.height = 700
        self.images: dict[str, PhotoImage] = {
            'background': PhotoImage(file=path.join(getcwd(), 'res/menu_background.png'))
        }

        self._prepare_menu()

    def _prepare_menu(self) -> None:
        self.background = Label(master=self,
                                image=self.images['background'])
        self.background.place(x=0, y=0,
                              width=self.width,
                              height=self.height)


class MainMenu(MenuFrame):  # pylint: disable=too-many-ancestors
    '''Creates a menu frame for the player to select the game mode.'''

    def __init__(self, window) -> None:
        super().__init__(window=window)
        self.window = window
        cwd = getcwd()
        self.images.update({
            'singleplayer': PhotoImage(file=path.join(cwd, 'res/button/singleplayer.png')),
            'multiplayer': PhotoImage(file=path.join(cwd, 'res/button/multiplayer.png')),
            'settings': PhotoImage(file=path.join(cwd, 'res/button/settings.png')),
            'exit': PhotoImage(file=path.join(cwd, 'res/button/exit.png'))
        })
        self._prepare_main_menu()

    def _prepare_main_menu(self) -> None:
        single_player = Button(master=self,
                               image=self.images['singleplayer'],
                               command=self.window.start_singleplayer)
        single_player.place(x=150, y=50, width=400, height=100)
        single_player.lift(self.background)
        multiplayer = Button(master=self,
                             image=self.images['multiplayer'],
                             command=self.window.start_multiplayer)
        multiplayer.place(x=150, y=200, width=400, height=100)
        multiplayer.lift(self.background)
        settings = Button(master=self,
                          image=self.images['settings'],
                          command=self.window.show_settings_menu)
        settings.place(x=150, y=350, width=400, height=100)
        settings.lift(self.background)
        exit_game = Button(master=self,
                           image=self.images['exit'],
                           command=self.window.destroy)
        exit_game.place(x=150, y=550, width=400, height=100)
        exit_game.lift(self.background)


class SettingsMenu(MenuFrame):  # pylint: disable=too-many-ancestors
    '''Creates a menu frame for the player to change settings.'''

    def __init__(self, window) -> None:
        super().__init__(window=window)
        self.window = window
        # cwd = getcwd()
        self.images.update({

        })
        self._prepare_settings_menu()

    def _prepare_settings_menu(self) -> None:
        pass

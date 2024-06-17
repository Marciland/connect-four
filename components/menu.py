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
        cwd = getcwd()
        self.images.update({
            'easy': PhotoImage(file=path.join(cwd, 'res/button/easy.png')),
            'medium': PhotoImage(file=path.join(cwd, 'res/button/medium.png')),
            'hard': PhotoImage(file=path.join(cwd, 'res/button/hard.png')),
            'extreme': PhotoImage(file=path.join(cwd, 'res/button/extreme.png')),
            'back': PhotoImage(file=path.join(cwd, 'res/button/back.png'))
        })
        self.difficulty_buttons: dict[str, Button] = {}
        self._prepare_settings_menu()
        self._change_difficulty(0, 'easy')

    def _prepare_settings_menu(self) -> None:
        easy = Button(master=self,
                      image=self.images['easy'],
                      command=lambda button='easy': self._change_difficulty(0, button))
        easy.place(x=150, y=50, width=200, height=100)
        easy.lift(self.background)
        self.difficulty_buttons.update({'easy': easy})
        medium = Button(master=self,
                        image=self.images['medium'],
                        command=lambda button='medium': self._change_difficulty(1, button))
        medium.place(x=350, y=50, width=200, height=100)
        medium.lift(self.background)
        self.difficulty_buttons.update({'medium': medium})
        hard = Button(master=self,
                      image=self.images['hard'],
                      command=lambda button='hard': self._change_difficulty(2, button))
        hard.place(x=150, y=200, width=200, height=100)
        hard.lift(self.background)
        self.difficulty_buttons.update({'hard': hard})
        extreme = Button(master=self,
                         image=self.images['extreme'],
                         command=lambda button='extreme': self._change_difficulty(3, button))
        extreme.place(x=350, y=200, width=200, height=100)
        extreme.lift(self.background)
        self.difficulty_buttons.update({'extreme': extreme})
        back = Button(master=self,
                      image=self.images['back'],
                      command=self.window.show_main_menu)
        back.place(x=150, y=550, width=400, height=100)
        back.lift(self.background)

    def _change_difficulty(self, dif_value: int, difficulty: str) -> None:
        self.window.set_difficulty(dif_value)
        for _difficulty, button in self.difficulty_buttons.items():
            if _difficulty == difficulty:
                button.configure(state='disabled')
            else:
                button.configure(state='active')

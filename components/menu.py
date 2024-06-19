'''contains all menu components.'''
from os import getcwd, path
from tkinter import Button, Frame, Label, PhotoImage
from tkinter.font import Font

from assets import Difficulty, Dimension


class MenuFrame(Frame):
    '''Frame extension for the game's menu.'''

    def __init__(self, window) -> None:
        super().__init__(master=window)
        self.window = window
        self.dimension: Dimension = Dimension(width=700,
                                              height=700)
        self.font: Font = Font(family='Cooper Black', size=40)
        self.background_img: PhotoImage = PhotoImage(file=path.join(getcwd(),
                                                                    'res/menu_background.png'))
        self._prepare_menu()

    def _prepare_menu(self) -> None:
        self.background = Label(master=self,
                                image=self.background_img)
        self.background.place(x=0, y=0,
                              width=self.dimension.width,
                              height=self.dimension.height)

    def _configure_menu_button(self, button: Button) -> None:
        button.configure(font=self.font,
                         background='pale turquoise')


class MainMenu(MenuFrame):  # pylint: disable=too-many-ancestors
    '''Creates a menu frame for the player to select the game mode.'''

    def __init__(self, window) -> None:
        super().__init__(window=window)
        self.window = window
        self._prepare_main_menu()

    def _prepare_main_menu(self) -> None:
        single_player = Button(master=self,
                               text='Singleplayer',
                               command=self.window.start_singleplayer)
        self._configure_menu_button(single_player)
        single_player.place(x=150, y=50, width=400, height=100)
        single_player.lift(self.background)
        multiplayer = Button(master=self,
                             text='Multiplayer',
                             command=self.window.start_multiplayer)
        self._configure_menu_button(multiplayer)
        multiplayer.place(x=150, y=200, width=400, height=100)
        multiplayer.lift(self.background)
        settings = Button(master=self,
                          text='Settings',
                          command=self.window.show_settings_menu)
        self._configure_menu_button(settings)
        settings.place(x=150, y=350, width=400, height=100)
        settings.lift(self.background)
        exit_game = Button(master=self,
                           text='Exit Game',
                           command=self.window.destroy)
        self._configure_menu_button(exit_game)
        exit_game.place(x=150, y=550, width=400, height=100)
        exit_game.lift(self.background)


class SettingsMenu(MenuFrame):  # pylint: disable=too-many-ancestors
    '''Creates a menu frame for the player to change settings.'''

    def __init__(self, window) -> None:
        super().__init__(window=window)
        self.window = window
        self.difficulty_font: Font = Font(family='Cooper Black', size=25)
        self.difficulty_buttons: dict[str, Button] = {}
        self._prepare_settings_menu()
        self._configure_difficulty_buttons()
        self._set_disabled_button()

    def _prepare_settings_menu(self) -> None:
        easy = Button(master=self,
                      command=lambda: self._change_difficulty(Difficulty.EASY))
        easy.place(x=150, y=50, width=200, height=100)
        easy.lift(self.background)
        self.difficulty_buttons.update({Difficulty.EASY.name: easy})
        medium = Button(master=self,
                        command=lambda: self._change_difficulty(Difficulty.MEDIUM))
        medium.place(x=350, y=50, width=200, height=100)
        medium.lift(self.background)
        self.difficulty_buttons.update({Difficulty.MEDIUM.name: medium})
        hard = Button(master=self,
                      command=lambda: self._change_difficulty(Difficulty.HARD))
        hard.place(x=150, y=200, width=200, height=100)
        hard.lift(self.background)
        self.difficulty_buttons.update({Difficulty.HARD.name: hard})
        extreme = Button(master=self,
                         command=lambda: self._change_difficulty(Difficulty.EXTREME))
        extreme.place(x=350, y=200, width=200, height=100)
        extreme.lift(self.background)
        self.difficulty_buttons.update({Difficulty.EXTREME.name: extreme})
        back = Button(master=self,
                      text='Back',
                      command=self.window.show_main_menu)
        self._configure_menu_button(back)
        back.place(x=150, y=550, width=400, height=100)
        back.lift(self.background)

    def _configure_difficulty_buttons(self) -> None:
        for difficulty, button in self.difficulty_buttons.items():
            button.configure(font=self.difficulty_font,
                             text=difficulty,
                             bg='pale turquoise',
                             activebackground='pale turquoise')

    def _change_difficulty(self, difficulty: Difficulty) -> None:
        self.window.set_difficulty(difficulty.value)
        for _difficulty, button in self.difficulty_buttons.items():
            if _difficulty == difficulty.name:
                button.configure(state='disabled')
            else:
                button.configure(state='active')

    def _set_disabled_button(self):
        match self.window.get_difficulty():
            case Difficulty.EASY.value:
                self._change_difficulty(Difficulty.EASY)
            case Difficulty.MEDIUM.value:
                self._change_difficulty(Difficulty.MEDIUM)
            case Difficulty.HARD.value:
                self._change_difficulty(Difficulty.HARD)
            case Difficulty.EXTREME.value:
                self._change_difficulty(Difficulty.EXTREME)

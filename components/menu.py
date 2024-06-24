'''contains all menu components.'''
from tkinter import Button, Frame, Label
from tkinter.font import Font
from typing import TYPE_CHECKING

from assets import Difficulty, Language, Resolution

if TYPE_CHECKING:
    from components import MainWindow


class MenuFrame(Frame):
    '''Frame extension for the game's menu.'''

    def __init__(self, window) -> None:
        super().__init__(master=window)
        self.window: MainWindow = window
        self.font: Font = Font(family='Cooper Black', size=40)
        match self.window.settings.resolution:
            case Resolution.SMALL.value:
                self.background_img = self.window.background_img.subsample(7)
            case Resolution.MEDIUM.value:
                self.background_img = self.window.background_img.subsample(5)
        self.button_height = self.window.settings.resolution.height // 7
        self.button_width = self.window.settings.resolution.width * 4 // 7
        self.button_spacing = self.button_height // 2
        self.button_margin = self.window.settings.resolution.width // 4.6
        self._prepare_menu()

    def _prepare_menu(self) -> None:
        self.background = Label(master=self,
                                name='background',
                                image=self.background_img)
        self.background.place(x=0, y=0,
                              width=self.window.settings.resolution.width,
                              height=self.window.settings.resolution.height)

    def _configure_menu_button(self, button: Button, text: str, position: int) -> None:
        button.configure(font=self.font,
                         text=text,
                         background='pale turquoise')
        button.lift(self.background)
        button.place(x=self.button_margin,
                     y=(position+1) * self.button_spacing +
                     position * self.button_height,
                     width=self.button_width,
                     height=self.button_height)


class MainMenu(MenuFrame):  # pylint: disable=too-many-ancestors
    '''Creates a menu frame for the player to select the game mode.'''

    def __init__(self, window) -> None:
        super().__init__(window=window)
        self.window = window
        self._prepare_main_menu()

    def _prepare_main_menu(self) -> None:
        singleplayer = Button(master=self,
                              command=self.window.start_singleplayer)
        singleplayer_text = self.window.translation.get('singleplayer')
        self._configure_menu_button(button=singleplayer,
                                    text=singleplayer_text,
                                    position=0)
        multiplayer = Button(master=self,
                             command=self.window.start_multiplayer)
        multiplayer_text = self.window.translation.get('multiplayer')
        self._configure_menu_button(button=multiplayer,
                                    text=multiplayer_text,
                                    position=1)
        settings = Button(master=self,
                          command=self.window.show_settings_menu)
        settings_text = self.window.translation.get('settings')
        self._configure_menu_button(button=settings,
                                    text=settings_text,
                                    position=2)
        exit_game = Button(master=self,
                           command=self.window.destroy)
        exit_text = self.window.translation.get('exit')
        self._configure_menu_button(button=exit_game,
                                    text=exit_text,
                                    position=3)


class SettingsMenu(MenuFrame):  # pylint: disable=too-many-ancestors
    '''Creates a menu frame for the player to change settings.'''

    def __init__(self, window) -> None:
        super().__init__(window=window)
        self.window = window
        self.difficulty_font: Font = Font(family='Cooper Black', size=25)
        self.difficulty_buttons: dict[str, Button] = {}
        self.resolution_buttons: dict[str, Button] = {}
        self.language_buttons: dict[str, Button] = {}
        self._prepare_settings_menu()

    def _enter_sub_menu(self) -> None:
        for child in self.winfo_children():
            if child.winfo_name() == 'back':
                child.configure(text=self.window.translation.get('save'))
                continue
            if child.winfo_name() == 'background':
                continue
            child.place_forget()

    def _prepare_settings_menu(self) -> None:
        difficulty = Button(master=self,
                            command=self._show_difficulty_settings)
        difficulty_text = self.window.translation.get('difficulty')
        self._configure_menu_button(difficulty,
                                    text=difficulty_text,
                                    position=0)
        resolution = Button(master=self,
                            command=self.show_resolution_settings)
        resolution_text = self.window.translation.get('resolution')
        self._configure_menu_button(resolution,
                                    text=resolution_text,
                                    position=1)
        language = Button(master=self,
                          command=self._show_language_settings)
        language_text = self.window.translation.get('language')
        self._configure_menu_button(language,
                                    text=language_text,
                                    position=2)
        back = Button(master=self,
                      name='back',
                      command=self.window.show_main_menu)
        back_text = self.window.translation.get('back')
        self._configure_menu_button(back,
                                    text=back_text,
                                    position=3)

    def _show_difficulty_settings(self) -> None:
        self._enter_sub_menu()
        easy = Button(master=self,
                      text=self.window.translation.get('easy'),
                      command=lambda: self._change_difficulty(Difficulty.EASY))
        self.difficulty_buttons.update({Difficulty.EASY.name: easy})
        medium = Button(master=self,
                        text=self.window.translation.get('medium_dif'),
                        command=lambda: self._change_difficulty(Difficulty.MEDIUM))
        self.difficulty_buttons.update({Difficulty.MEDIUM.name: medium})
        hard = Button(master=self,
                      text=self.window.translation.get('hard'),
                      command=lambda: self._change_difficulty(Difficulty.HARD))
        self.difficulty_buttons.update({Difficulty.HARD.name: hard})
        extreme = Button(master=self,
                         text=self.window.translation.get('extreme'),
                         command=lambda: self._change_difficulty(Difficulty.EXTREME))
        self.difficulty_buttons.update({Difficulty.EXTREME.name: extreme})
        self._configure_toggle_buttons(self.difficulty_buttons,
                                       self.difficulty_font)
        self._place_difficulty_buttons()
        self._set_difficulty_button()

    def _place_difficulty_buttons(self) -> None:
        '''difficulty buttons are half in width and need to group'''
        for index, button in enumerate(list(self.difficulty_buttons.values())):
            if index % 2 == 0:
                top = 0 if index == 0 else 1
                button.place(x=self.button_margin,
                             y=(top + 1) * self.button_spacing +
                             top * self.button_height,
                             width=self.button_width//2,
                             height=self.button_height)
            else:
                top = 0 if index == 1 else 1
                button.place(x=self.button_margin+self.button_width//2,
                             y=(top + 1) * self.button_spacing +
                             top * self.button_height,
                             width=self.button_width//2,
                             height=self.button_height)

    def show_resolution_settings(self) -> None:
        '''Loads the resolution settings.'''
        self._enter_sub_menu()
        small = Button(master=self,
                       command=lambda: self._change_resolution(Resolution.SMALL))
        small_text = self.window.translation.get('small_res')
        self._configure_menu_button(button=small,
                                    text=small_text,
                                    position=0)
        self.resolution_buttons.update({Resolution.SMALL.name: small})
        medium = Button(master=self,
                        command=lambda: self._change_resolution(Resolution.MEDIUM))
        medium_text = self.window.translation.get('medium_res')
        self._configure_menu_button(button=medium,
                                    text=medium_text,
                                    position=1)
        self.resolution_buttons.update({Resolution.MEDIUM.name: medium})
        self._configure_toggle_buttons(self.resolution_buttons,
                                       self.font)
        self._set_resolution_button()

    def _show_language_settings(self) -> None:
        self._enter_sub_menu()
        english = Button(master=self,
                         command=lambda: self._change_language(Language.ENGLISH))
        english_text = self.window.translation.get('english')
        self._configure_menu_button(button=english,
                                    text=english_text,
                                    position=0)
        self.language_buttons.update({Language.ENGLISH.value: english})
        german = Button(master=self,
                        command=lambda: self._change_language(Language.GERMAN))
        german_text = self.window.translation.get('german')
        self._configure_menu_button(button=german,
                                    text=german_text,
                                    position=1)
        self.language_buttons.update({Language.GERMAN.value: german})
        self._configure_toggle_buttons(self.language_buttons,
                                       self.font)
        self._set_language_button()

    def _configure_toggle_buttons(self, buttons: dict[str, Button], font: Font) -> None:
        for _, button in buttons.items():
            button.configure(font=font,
                             bg='pale turquoise',
                             activebackground='pale turquoise')
            button.lift(self.background)

    def _change_difficulty(self, difficulty: Difficulty) -> None:
        self.window.set_difficulty(difficulty.value)
        for _difficulty, button in self.difficulty_buttons.items():
            if _difficulty == difficulty.name:
                button.configure(state='disabled')
            else:
                button.configure(state='active')

    def _change_resolution(self, resolution: Resolution) -> None:
        self.window.set_resolution(resolution.value)
        self.window.show_settings_menu()
        # call the "next" frame as self will be destroyed
        self.window.current_frame.show_resolution_settings()

    def _change_language(self, language: Language) -> None:
        self.window.set_language(language.value)
        self.window.title(self.window.translation.get("title"))
        for _language, button in self.language_buttons.items():
            if _language == language.value:
                button.configure(state='disabled')
            else:
                button.configure(state='active')

    def _set_difficulty_button(self):
        match self.window.settings.difficulty:
            case Difficulty.EASY.value:
                self._change_difficulty(Difficulty.EASY)
            case Difficulty.MEDIUM.value:
                self._change_difficulty(Difficulty.MEDIUM)
            case Difficulty.HARD.value:
                self._change_difficulty(Difficulty.HARD)
            case Difficulty.EXTREME.value:
                self._change_difficulty(Difficulty.EXTREME)

    def _set_resolution_button(self):
        match self.window.settings.resolution:
            case Resolution.SMALL.value:
                self._toggle_resolution_button(Resolution.SMALL)
            case Resolution.MEDIUM.value:
                self._toggle_resolution_button(Resolution.MEDIUM)

    def _toggle_resolution_button(self, resolution: Resolution):
        for _resolution, button in self.resolution_buttons.items():
            if _resolution == resolution.name:
                button.configure(state='disabled')
            else:
                button.configure(state='active')

    def _set_language_button(self):
        match self.window.settings.language:
            case Language.ENGLISH.name:
                self._change_language(Language.ENGLISH)
            case Language.GERMAN.name:
                self._change_language(Language.GERMAN)

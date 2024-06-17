'''Contains a root window that renders the other components.'''
from tkinter import Frame, Tk

from .game import ConnectFour
from .menu import MainMenu, SettingsMenu


class MainWindow(Tk):
    '''The main window the user interacts with.'''

    def __init__(self) -> None:
        super().__init__()
        self.withdraw()
        # show after rendering
        self.after(0, self.deiconify)
        self.title('Vier Gewinnt | Connect Four')
        self.resizable(False, False)
        self.iconbitmap(r"res\icon.ico")
        self.current_frame: Frame = None
        self.show_main_menu()

    def _get_geometry(self, width: int, height: int) -> str:
        '''
        Returns a geometry string of the tkinter format:
        width x height + startx + starty

        The geometry string is used to determine
        where the window is placed
        and what its size is.
        '''
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        startx = screen_w//2 - width//2
        starty = screen_h//2 - height//2
        return f'{width}x{height}+{startx}+{starty}'

    def _update_frame(self, frame: Frame) -> None:
        '''Renders the given frame with its according size.'''
        if self.current_frame:
            self.current_frame.destroy()
        self.geometry(self._get_geometry(width=frame.width,
                                         height=frame.height))
        frame.place(x=0, y=0, width=frame.width, height=frame.height)
        self.current_frame = frame

    def show_main_menu(self) -> None:
        '''Renders the main menu.'''
        self._update_frame(MainMenu(window=self))

    def show_settings_menu(self) -> None:
        '''Renders the settings menu.'''
        self._update_frame(SettingsMenu(window=self))

    def start_singleplayer(self) -> None:
        '''Starts a solo game vs the computer.'''
        singleplayer: ConnectFour = ConnectFour(window=self)
        singleplayer.solo = True
        singleplayer.new_game()
        self._update_frame(singleplayer)

    def start_multiplayer(self) -> None:
        '''Starts a 2 player versus.'''
        multiplayer: ConnectFour = ConnectFour(window=self)
        multiplayer.solo = False
        multiplayer.new_game()
        self._update_frame(multiplayer)

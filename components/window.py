'''Contains a root window that renders the other components.'''
from tkinter import Frame, Tk

from components import ConnectFour, MainMenu


class MainWindow(Tk):
    '''The main window the user interacts with.'''

    def __init__(self) -> None:
        super().__init__()
        self.title('Vier Gewinnt | Connect Four')
        self.resizable(False, False)
        self.iconbitmap(r"res\icon.ico")
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
        self.geometry(self._get_geometry(width=frame.width,
                                         height=frame.height))
        frame.place(x=0, y=0,
                    width=frame.width,
                    height=frame.height)

    def show_main_menu(self) -> None:
        '''Renders the main menu.'''
        self._update_frame(MainMenu(self))

    def start_multiplayer(self) -> None:
        '''Starts a 2 player versus.'''
        self._update_frame(ConnectFour(self))

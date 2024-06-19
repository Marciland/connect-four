'''main entry point for the game.'''
from components import MainWindow, Settings

if __name__ == '__main__':
    settings = Settings()
    settings.read()
    window = MainWindow(settings)
    window.mainloop()

'''main entry point for the game.'''
from components import MainWindow, Settings

if __name__ == '__main__':
    settings = Settings()
    if settings.read():
        window = MainWindow(settings)
        window.mainloop()

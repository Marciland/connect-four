'''Settings to store in config.json'''
import json
from os import getcwd, makedirs, path

from assets import Difficulty, Dimension


class Settings:
    '''Setting class provides a way to dump and store settings.'''

    def __init__(self) -> None:
        self.path = path.join(getcwd(), 'config.json')
        self.difficulty: int = Difficulty.EASY.value
        self.resolution: Dimension = Dimension(width=700, height=700)
        self.language: str = 'en'
        self.last_ip: str = ''

    def _dump(self) -> None:
        self_dict = {
            "difficulty": self.difficulty,
            "resolution": {
                "width": self.resolution.width,
                "height": self.resolution.height
            },
            "language": self.language,
            "last_ip": self.last_ip
        }
        with open(file=self.path, mode='w', encoding='utf-8') as file_handle:
            json.dump(self_dict, file_handle, indent=4)

    def save(self) -> None:
        '''Saves the settings.'''
        if not path.exists(self.path):
            makedirs(path.dirname(self.path), exist_ok=True)
            # pylint: disable=consider-using-with
            open(file=self.path, mode='a', encoding='utf-8').close()
        self._dump()

    def read(self) -> None:
        '''Reads the settings. Dumps the current settings if config is corrupted.'''
        if not path.exists(self.path):
            self.save()
            return
        with open(file=self.path, mode='r', encoding='utf-8') as file_handle:
            new_settings = json.load(file_handle)
        try:
            self.difficulty = new_settings['difficulty']
            self.resolution = Dimension(width=new_settings['width'],
                                        height=new_settings['height'])
            self.language = new_settings['language']
            self.last_ip = new_settings['last_ip']
        except KeyError:
            self._dump()

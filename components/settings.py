'''Settings to store in config.json'''
import json
from json.decoder import JSONDecodeError
from os import getcwd, makedirs, path, remove

from assets import Difficulty, Dimension, Language, Resolution


class Settings:
    '''Setting class provides a way to dump and store settings.'''

    def __init__(self) -> None:
        self.path = path.join(getcwd(), 'config.json')
        self.difficulty: int = Difficulty.EASY.value
        self.resolution: Dimension = Resolution.MEDIUM.value
        self.language: Language = Language.ENGLISH.name
        self.last_ip: str = ''

    def _dump(self) -> bool:
        self_dict = {
            "difficulty": self.difficulty,
            "dimension": {
                "width": self.resolution.width,
                "height": self.resolution.height
            },
            "language": self.language,
            "last_ip": self.last_ip
        }
        try:
            with open(file=self.path, mode='w', encoding='utf-8') as file_handle:
                json.dump(self_dict, file_handle, indent=4)
            return True
        except TypeError as ex:
            remove(self.path)
            print('Failed to save settings:', ex)
            return False

    def save(self) -> bool:
        '''Saves the settings.'''
        if not path.exists(self.path):
            makedirs(path.dirname(self.path), exist_ok=True)
            # pylint: disable=consider-using-with
            open(file=self.path, mode='a', encoding='utf-8').close()
        return self._dump()

    def read(self) -> bool:
        '''Reads the settings. Dumps the current settings if config is corrupted.'''
        if not path.exists(self.path):
            return self.save()
        try:
            with open(file=self.path, mode='r', encoding='utf-8') as file_handle:
                new_settings = json.load(file_handle)
            self.difficulty = new_settings['difficulty']
            self.resolution = Dimension(width=new_settings['dimension']['width'],
                                        height=new_settings['dimension']['height'])
            self.language = new_settings['language']
            self.last_ip = new_settings['last_ip']
            return True
        except (KeyError, JSONDecodeError):
            return self._dump()

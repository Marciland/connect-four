'''Helper class for translations.'''
import json
from json.decoder import JSONDecodeError
from os import getcwd, path

from assets import Language


class TranslationTable:
    '''Contains all translations and knows what language is selected.'''

    def __init__(self, language: Language = Language.ENGLISH.value) -> None:
        self.current_language: Language = language
        self.base_path: str = path.join(getcwd(), 'res', 'lang')
        self.translations: dict[str, dict] = {}
        self.translations[Language.ENGLISH.value] = self._read_translation(path.join(self.base_path,
                                                                                     'en.json'))
        self.translations[Language.GERMAN.value] = self._read_translation(path.join(self.base_path,
                                                                                    'de.json'))

    def _read_translation(self, file_path: str) -> dict[str, str]:
        with open(file=file_path, mode='r', encoding='utf-8') as file_handle:
            file_content = file_handle.read()
        try:
            return json.loads(file_content)
        except JSONDecodeError:
            print(f'Failed to load translation from \'{file_path}\':',
                  'Invalid JSON!')
            return {}

    def get(self, key: str) -> str:
        '''Gets a value based on given key. Fallback to english.'''
        try:
            return self.translations[self.current_language][key]
        except KeyError:
            return self.translations[Language.ENGLISH.value][key]

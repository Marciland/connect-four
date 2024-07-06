'''Prepares all resources.'''
from os import getcwd, path
from tkinter import PhotoImage

from assets import Dimension, Resolution


class Resources:  # pylint: disable=too-few-public-methods
    '''Contains all resource references.'''

    def __init__(self) -> None:
        self.base_path = path.join(getcwd(), 'res')
        self.images: dict[str, dict[str, PhotoImage]] = {}

    def prepare_images(self, dimension: Dimension) -> None:
        '''Loads all resources. This needs to be called after Tk()!'''
        self.images.clear()
        bg_image = PhotoImage(file=path.join(self.base_path,
                                             'menu_background.png'))
        match dimension:
            case Resolution.SMALL.value:
                bg_image = bg_image.zoom(5).subsample(8)
            case Resolution.MEDIUM.value:
                bg_image = bg_image.zoom(7).subsample(8)
        self.images.update({'main': {'bg': bg_image}})
        self.images.update({'cell': self._get_cell_images(dimension)})
        self.images.update({'entry': self._get_entry_images(dimension)})

    def _get_cell_images(self, dimension: Dimension) -> dict[str, PhotoImage]:
        cell_path = path.join(self.base_path, 'cell')
        empty_image = PhotoImage(file=path.join(cell_path,
                                                'empty_cell.png'))
        player1_image = PhotoImage(file=path.join(cell_path,
                                                  'purple_cell.png'))
        player2_image = PhotoImage(file=path.join(cell_path,
                                                  'yellow_cell.png'))
        if dimension == Resolution.SMALL.value:
            empty_image = empty_image.zoom(5).subsample(7)
            player1_image = player1_image.zoom(5).subsample(7)
            player2_image = player2_image.zoom(5).subsample(7)
        return {
            'empty': empty_image,
            'player1': player1_image,
            'player2': player2_image
        }

    def _get_entry_images(self, dimension: Dimension) -> dict[str, PhotoImage]:
        entry_path = path.join(self.base_path, 'entry_point')
        empty_image = PhotoImage(file=path.join(entry_path,
                                                'empty_entry.png'))
        player1_image = PhotoImage(file=path.join(entry_path,
                                                  'purple_entry.png'))
        player2_image = PhotoImage(file=path.join(entry_path,
                                                  'yellow_entry.png'))
        if dimension == Resolution.SMALL.value:
            empty_image = empty_image.zoom(5).subsample(7)
            player1_image = player1_image.zoom(5).subsample(7)
            player2_image = player2_image.zoom(5).subsample(7)
        return {
            'empty': empty_image,
            'player1': player1_image,
            'player2': player2_image
        }

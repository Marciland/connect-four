'''All dataclasses used in this project.'''
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass()
class Dimension:
    '''Screen resolution dimension.'''
    width: int
    height: int


@dataclass(frozen=True, eq=True)
class Position2D:
    '''2D position on the grid.'''
    x: int
    y: int

    def add(self, other: Position2D) -> Position2D:
        '''Returns the new Position.'''
        return Position2D(x=self.x+other.x,
                          y=self.y+other.y)


class Difficulty(Enum):
    '''Constants for the difficulties.'''
    EASY = 0
    MEDIUM = 1
    HARD = 2
    EXTREME = 3


class Resolution(Enum):
    '''Constants for the resolutions.'''
    SMALL = Dimension(width=500, height=500)
    MEDIUM = Dimension(width=700, height=700)


class Language(Enum):
    '''Constants for the languages.'''
    ENGLISH = 'en'
    GERMAN = 'de'

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

'''Position on the board.'''
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Position2D:
    '''2D position on the grid.'''
    x: int
    y: int

    def add(self, other: Position2D) -> Position2D:
        '''Returns the new Position.'''
        return Position2D(x=self.x+other.x,
                          y=self.y+other.y)

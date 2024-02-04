from collections.abc import Generator

from .piece import Piece
from ..moves import Move


class King(Piece):
    def moves(self, position: int):
        for i in (1, 9, 8, 7, -1, -9, -8, -7):
            yield Move(self, position, position + i)


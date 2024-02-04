from typing import Generator

from .piece import Piece
from ..moves import Move


class Knight(Piece):
    repr = 'n', 'N'

    def moves(self, position: int) -> Generator[Move, None, None]:
        x, y = position % 8, position // 8

        if x < 6 and y < 7:
            yield Move(self, position, position + 10)
        if x < 7 and y < 6:
            yield Move(self, position, position + 17)
        if x > 0 and y < 6:
            yield Move(self, position, position + 15)
        if x > 1 and y < 7:
            yield Move(self, position, position + 6)
        if x > 1 and y > 0:
            yield Move(self, position, position - 10)
        if x > 0 and y > 1:
            yield Move(self, position, position - 17)
        if x < 7 and y > 1:
            yield Move(self, position, position - 15)
        if x < 6 and y > 0:
            yield Move(self, position, position - 6)


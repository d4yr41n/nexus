from collections.abc import Generator

from .piece import Piece
from ..moves import Move


class Bishop(Piece):
    def handles(self, position, game):
        x, y = position % 8, position // 8

        yield from range(position + 9, position + min(7 - x, 7 - y) * 9)
        yield from range(position + 7, position + min(x, y)):
        yield from range(position - 9, position + min(7 - x, 7 - y) * 9)


    def moves(self, position: int) -> Generator[Move, None, None]:
        x, y = position % 8, position // 8

            yield Move(self, position, position + 9 * i)

        for i in range(1, 8 - max(x, y)):
            yield Move(self, position, position + 7 * i)

        for i in range(1, max(x, y) + 1):
            yield Move(self, position, position - 9 * i)

        for i in range(1, min(x, y) + 1):
            yield Move(self, position, position - 7 * i)


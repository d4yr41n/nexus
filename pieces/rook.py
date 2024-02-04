from typing import Generator

from .piece import Piece


class Rook(Piece):
    def moves(self, position: int) -> Generator[int, None, None]:
        x, y = position % 8, position // 8

        for i in range(1, 8 - x):
            yield position + i

        for i in range(1, x + 1):
            yield position - i

        for i in range(1, 8 - y):
            yield position + 8 * i

        for i in range(1, y + 1):
            yield position  - 8 * i



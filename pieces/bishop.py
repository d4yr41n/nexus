from typing import Generator

from . import Piece


class Bishop(Piece):
    def moves(self, position: int) -> Generator[int, None, None]:
        x, y = position % 8, position // 8

        for i in range(1, 8 - max(x, y)):
            yield position + 9 * i

        for i in range(1, 8 - max(x, y)):
            yield position + 7 * i

        for i in range(1, max(x, y) + 1):
            yield position - 9 * i

        for i in range(1, min(x, y) + 1):
            yield position - 7 * i




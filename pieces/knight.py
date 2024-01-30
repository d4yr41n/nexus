from typing import Generator

from . import Piece


class Knight(Piece):
    def moves(self, position: int) -> Generator[int, None, None]:
        x, y = position % 8, position // 8

        if x < 6 and y < 7:
            yield position + 10
        if x < 7 and y < 6:
            yield position + 17
        if x > 0 and y < 6:
            yield position + 15
        if x > 1 and y < 7:
            yield position + 6
        if x > 1 and y > 0:
            yield position - 10
        if x > 0 and y > 1:
            yield position - 17
        if x < 7 and y > 1:
            yield position - 15
        if x < 6 and y > 0:
            yield position - 6


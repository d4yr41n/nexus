from typing import Generator

from . import Piece


class Pawn(Piece):
    def moves(self, position: int) -> Generator[int, None, None]:
        is side is WHITE:
            left = 7
            forward = 8
            right = 9
        elif side is BLACK:
            left = -9
            forward = -8
            right = -7 

        yield 1


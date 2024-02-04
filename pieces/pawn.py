from typing import Generator

from .piece import Piece
from ..moves import Move


class Pawn(Piece):
    def moves(self, position: int) -> Generator[Move, None, None]:
        if self.side:
            yield Move(self, position, position + 7)
            yield Move(self, position, position + 8)
            yield Move(self, position, position + 16)
            yield Move(self, position, position + 9)
        else:
            yield Move(self, position, position - 7)
            yield Move(self, position, position - 8)
            yield Move(self, position, position - 16)
            yield Move(self, position, position - 9)


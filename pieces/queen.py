from typing import Generator

from .piece import Piece
from .bishop import Bishop
from .rook import Rook


class Queen(Bishop, Rook):
    def moves(self, position: int) -> Generator[int, None, None]:
        yield from super(Bishop, self).moves(position)
        yield from super(Rook, self).moves(position)


from . import Piece
from .bishop import Bishop
from .rook import Rook


class Queen(Bishop, Rook):
    @property
    def moves(self):
        yield from super(Bishop, self).moves
        yield from super(Rook, self).moves


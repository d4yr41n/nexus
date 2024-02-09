from .bishop import Bishop
from .rook import Rook


class Queen(Bishop, Rook):
    char = 'Q'
    repr = 'q', 'Q'

    def lines(self, position: int) -> tuple[range, ...]:
        return super(Bishop, self).lines(position) + super(Rook, self).lines(position)

from .bishop import Bishop
from .rook import Rook


class Queen(Bishop, Rook):
    notation = 'Q'
    repr = 'q', 'Q'
    value = 9

    def lines(self, position: int) -> tuple[range, ...]:
        return super().lines(position) + super(Bishop, self).lines(position)

    def moves(self, game, position):
        yield from super(Rook, self).moves(game, position)

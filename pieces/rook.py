from typing import TYPE_CHECKING

from .sliding_piece import SlidingPiece
from ..moves import Move

if TYPE_CHECKING:
    from ..game import Game


class Rook(SlidingPiece):
    char = 'R'
    repr = 'r', 'R'

    def lines(self, position: int) -> tuple[range, ...]:
        x, y = position % 8, position // 8
        return (
            range(position + 1, (y + 1) * 8),
            range(position + 8, 57 + x, 8),
            range(position - 1, y * 8 - 1, -1),
            range(position - 8, x, -8),
        )


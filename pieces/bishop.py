from typing import TYPE_CHECKING

from .sliding_piece import SlidingPiece
from .pinned_piece import PinnedPiece
from ..moves import Move

if TYPE_CHECKING:
    from ..game import Game


class Bishop(SlidingPiece, PinnedPiece):
    char = 'B'
    repr = 'b', 'B'

    def lines(self, position: int) -> tuple[range, ...]:
        x, y = position % 8, position // 8
        return (
            range(position + 9, position + min(7 - x, 7 - y) * 9 + 1, 9),
            range(position + 7, position + min(x, 7 - y) * 7 + 1, 7),
            range(position - 9, position - min(x, y) * 9 - 1, -9),
            range(position - 7, position - min(7 - x, y) * 7 - 1, -7)
        )


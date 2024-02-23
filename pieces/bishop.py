from typing import TYPE_CHECKING

from .sliding_piece import SlidingPiece

if TYPE_CHECKING:
    from ..game import Game


class Bishop(SlidingPiece):
    notation = 'B'
    repr = 'b', 'B'
    value = 3
    vectors = 17, 15, -17, -15


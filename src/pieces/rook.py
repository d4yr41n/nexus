from __future__ import annotations
from typing import TYPE_CHECKING

from .sliding_piece import SlidingPiece

if TYPE_CHECKING:
    from ..game import Game


class Rook(SlidingPiece):
    notation = 'R'
    repr = 'r', 'R'
    value = 5
    vectors = 1, 16, -1, -16


from ..moves.rook_move import RookMove


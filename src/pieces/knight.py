from __future__ import annotations
from typing import TYPE_CHECKING, Generator

from .piece import Piece

if TYPE_CHECKING:
    from ..game import Game


class Knight(Piece):
    notation = 'N'
    repr = 'n', 'N'
    value = 3
    index = 2
    vectors = 18, 33, 31, 14, -18, -33, -31, -14


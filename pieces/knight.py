from __future__ import annotations
from typing import TYPE_CHECKING, Generator

from .base_piece import BasePiece
from ..moves import Move

if TYPE_CHECKING:
    from ..game import Game


class Knight(BasePiece):
    notation = 'N'
    repr = 'n', 'N'

    def handles(self, game: Game, position: int) -> Generator[int, None, None]:
        x, y = position % 8, position // 8

        # TODO: implement dynamic programming
        if x < 6 and y < 7:
            yield position + 10
        if x < 7 and y < 6:
            yield position + 17
        if x > 0 and y < 6:
            yield position + 15
        if x > 1 and y < 7:
            yield position + 6
        if x > 1 and y > 0:
            yield position - 10
        if x > 0 and y > 1:
            yield position - 17
        if x < 7 and y > 1:
            yield position - 15
        if x < 6 and y > 0:
            yield position - 6

    def moves(self, game, position):
        pass

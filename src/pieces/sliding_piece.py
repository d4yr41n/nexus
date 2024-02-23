from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

from .piece import Piece

if TYPE_CHECKING:
    from ..game import Game


class SlidingPiece(Piece):
    def handles(self, game: Game, position: int) -> Generator[int, None, None]:
        for vector in self.vectors:
            square = position
            while not (square := square + vector) & 0x88:
                yield square
                if game.board[square]:
                    break


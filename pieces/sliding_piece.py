from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

from .piece import Piece

if TYPE_CHECKING:
    from ..game import Game


class SlidingPiece(Piece):
    def lines(self, position: int) -> tuple[range, ...]:
        raise NotImplementedError

    def handles(self, game: Game, position: int) -> Generator[int, None, None]:
        for line in self.lines(position):
            for i in line:
                yield i
                if game.board[i]:
                    break


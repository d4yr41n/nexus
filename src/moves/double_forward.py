from __future__ import annotations
from typing import TYPE_CHECKING

from .move import Move

if TYPE_CHECKING:
    from ..game import Game


class DoubleForward(Move):
    def __init__(self, piece, start, end, passed):
        super().__init__(piece, start, end)
        self.passed = passed
        

    def apply(self, game: Game) -> None:
        super().apply(game)
        game.en_passant = self.passed

    def cancel(self, game) -> None:
        super().cancel(game)


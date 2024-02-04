from __future__ import annotations
from typing import TYPE_CHECKING

from .move import Move

if TYPE_CHECKING:
    from ..game import Game


class DoubleForward(Move):
    def apply(self, game: Game) -> None:
        super().apply(game)
        game.en_passant = self.start + 8

    def cancel(self, game) -> None:
        super().cancel(game)


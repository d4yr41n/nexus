from __future__ import annotations
from typing import TYPE_CHECKING

from .move import Move

if TYPE_CHECKING:
    from ..game import Game
    from ..piece import Piece


class Promotion(Move):
    buffer: Piece | None = None

    def apply(self, game: Game) -> None:
        super().apply(game)
        self.buffer, game.board[self.end] = game.board[self.end], self.buffer

    def cancel(self, game: Game) -> None:
        game.board[self.end], self.buffer = self.buffer, game.board[self.end]
        super().cancel(game)


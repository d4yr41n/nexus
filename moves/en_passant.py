from __future__ import annotations
from typing import TYPE_CHECKING

from .abstract_move import AbstractMove
from .move import Move

if TYPE_CHECKING:
    from ..game import Game


class EnPassant(Move):
    def apply(self, game: Game) -> None:
        self.target = game.board[game.en_passant]
        game.board[game.en_passant] = None
        game.board[self.end] = game.board[self.start]
        game.board[self.start] = None
        super(AbstractMove, self).apply(game)

    def cancel(self, game: Game) -> None:
        super(AbstractMove, self).cancel(game)
        game.board[self.start] = game.board[self.end]
        game.board[self.end] = None
        game.board[game.en_passant] = self.target
        self.target = None


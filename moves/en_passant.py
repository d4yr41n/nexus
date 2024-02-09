from __future__ import annotations
from typing import TYPE_CHECKING

from .abstract_move import AbstractMove
from .move import Move
from ..empty import Empty

if TYPE_CHECKING:
    from ..game import Game


class EnPassant(Move):
    def apply(self, game: Game) -> None:
        self.target = game.board[game.en_passant]
        game.board[game.en_passant] = Empty()
        game.board[self.end] = game.board[self.start]
        game.board[self.start] = Empty()
        super(AbstractMove, self).apply(game)

    def cancel(self, game: Game) -> None:
        super(AbstractMove, self).cancel(game)
        game.board[self.start] = game.board[self.end]
        game.board[self.end] = Empty()
        game.board[game.en_passant] = self.target
        self.target = None


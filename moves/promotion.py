from __future__ import annotations
from typing import TYPE_CHECKING

from .move import Move

if TYPE_CHECKING:
    from ..game import Game
    from ..pieces import Piece


class Promotion(Move):
    upgrade: Piece

    def __init__(self, piece: Piece, start: int, end: int, upgrade: type):
        super().__init__(piece, start, end)
        self.upgrade = upgrade(piece.side)

    def __repr__(self) -> str:
        return super().__repr__() + self.upgrade.char

    def notation(self):
        for notation in super().notation():
            yield notation + self.upgrade.char

    def apply(self, game: Game) -> None:
        super().apply(game)
        self.upgrade, game.board[self.end] = game.board[self.end], self.upgrade

    def cancel(self, game: Game) -> None:
        game.board[self.end], self.upgrade = self.upgrade, game.board[self.end]
        super().cancel(game)



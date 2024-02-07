from __future__ import annotations
from typing import TYPE_CHECKING

from .init_move import AbstractInitMove

if TYPE_CHECKING:
    from ..game import Game


class Castling(AbstractInitMove):
    def __init__(self, king: int, rook: int) -> None:
        self.king = king
        self.rook = rook

    def __repr__(self) -> str:
        if self.king < self.rook:
            return "O-O"
        else:
            return "O-O-O"

    def castle(self, game):
        if self.king < self.rook:
            game.board[self.king], game.board[self.king + 2] = game.board[self.king + 2], game.board[self.king]
            game.board[self.rook], game.board[self.rook - 2] = game.board[self.rook - 2], game.board[self.rook]
        else:
            game.board[self.king], game.board[self.king - 2] = game.board[self.king - 2], game.board[self.king] 
            game.board[self.rook], game.board[self.rook + 3] = game.board[self.rook + 3], game.board[self.rook]

    def apply(self, game: Game):
        self.castle(game)
        super().apply(game)

    def cancel(self, game: Game): 
        self.castle(game)
        super().cancel(game)


from __future__ import annotations
from typing import TYPE_CHECKING

from .abstract_move import AbstractMove

if TYPE_CHECKING:
    from ..game import Game


class Castling(AbstractMove):
    def __init__(self, king: int, rook: int) -> None:
        self.king = king
        self.rook = rook

    def __repr__(self) -> str:
        if self.king < self.rook:
            return "O-O"
        else:
            return "O-O-O"

    def apply(self, game: Game):
        if self.king < self.rook:
            game.board[self.king + 2] = game.board[self.king]
            game.board[self.king] = None
            game.board[self.rook - 2] = game.board[self.rook]
            game.board[self.rook] = None
        else:
            game.board[self.king - 2] = game.board[self.king]
            game.board[self.king] = None
            game.board[self.rook + 3] = game.board[self.rook]
            game.board[self.rook] = None
        game.castling = game.castling.replace(("kq", "KQ")[self.side], '')
        super().apply(game)

    def cancel(self, game: Game): 
        super().cancel(game)
        if self.king < self.rook:
            game.board[self.king] = game.board[self.king + 2]
            game.board[self.king + 2] = None
            game.board[self.rook] = game.board[self.rook - 2]
            game.board[self.rook - 2] = None
        else:
            game.board[self.king] = game.board[self.king - 2]
            game.board[self.king - 2] = None
            game.board[self.rook] = game.board[self.rook + 3]
            game.board[self.rook] = None

        game.castling = sorted(game.castling + "kq", "KQ")[self.side])


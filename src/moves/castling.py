from __future__ import annotations
from collections.abc import Generator
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

    def notation(self) -> Generator[str, None, None]:
        if self.king < self.rook:
            yield "O-O"
            yield "0-0"
        else:
            yield "O-O-O"
            yield "0-0-0"

    def castle(self, game):
        side = not self.king >> 4
        king = game.kings[side]
        if self.king < self.rook:
            game.board[self.king], game.board[self.king + 2] = game.board[self.king + 2], game.board[self.king]
            game.board[self.rook], game.board[self.rook - 2] = game.board[self.rook - 2], game.board[self.rook]
            if self.king == king:
                game.kings[side] = king + 2
            else:
                game.kings[side] = self.king
        else:

            game.board[self.king], game.board[self.king - 2] = game.board[self.king - 2], game.board[self.king] 
            game.board[self.rook], game.board[self.rook + 3] = game.board[self.rook + 3], game.board[self.rook]
            if self.king == king:
                game.kings[side] = king - 2
            else:
                game.kings[side] = self.king

    def apply(self, game: Game):
        castling = ("kq", "KQ")[not self.king >> 4]
        for i in castling:
            if i in game.castling:
                self.castling += i
        self.castle(game)
        super().apply(game)

    def cancel(self, game: Game): 
        self.castle(game)
        super().cancel(game)


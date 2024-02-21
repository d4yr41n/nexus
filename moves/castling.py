from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

from .castling_state_move import CastlingStateMove

if TYPE_CHECKING:
    from ..game import Game


class Castling(CastlingStateMove):
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
        king = game.kings[game.turn]
        if self.king < self.rook:
            game.board[self.king], game.board[self.king + 2] = game.board[self.king + 2], game.board[self.king]
            game.board[self.rook], game.board[self.rook - 2] = game.board[self.rook - 2], game.board[self.rook]
            if self.king == king:
                game.kings[game.turn] = king + 2
            else:
                game.kings[game.turn] = self.king
        else:

            game.board[self.king], game.board[self.king - 2] = game.board[self.king - 2], game.board[self.king] 
            game.board[self.rook], game.board[self.rook + 3] = game.board[self.rook + 3], game.board[self.rook]
            if self.king == king:
                game.kings[game.turn] = king + 3
            else:
                game.kings[game.turn] = self.king

    def apply(self, game: Game):
        self.castling = ("kq", "KQ")[game.board[self.king].side]
        self.castle(game)
        super().apply(game)
        super(CastlingStateMove, self).apply(game)

    def cancel(self, game: Game): 
        super(CastlingStateMove, self).cancel(game)
        self.castle(game)
        super().cancel(game)


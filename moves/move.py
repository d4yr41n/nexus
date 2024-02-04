from __future__ import annotations
from typing import TYPE_CHECKING

from .abstract_move import AbstractMove

if TYPE_CHECKING:
    from ..game import Game
    from ..pieces import Piece


file = "abcdefgh"
rank = "12345678"


class Move(AbstractMove):
    target: Piece | None

    def __init__(self, piece: Piece, start: int, end: int) -> None:
        self.piece = piece
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{self.piece}{file[self.start % 8]}{rank[self.start // 8]}{file[self.end % 8]}{rank[self.end // 8]}"

    def apply(self, game: Game) -> None:
        self.target = game.board[self.end]
        game.board[self.end] = game.board[self.start]
        game.board[self.start] = None
        super().apply(game)

    def cancel(self, game: Game) -> None:
        super().cancel(game)
        game.board[self.start] = game.board[self.end]
        game.board[self.end] = self.target
        self.target = None


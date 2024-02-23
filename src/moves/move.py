from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

from .abstract_move import AbstractMove
from ..empty import Empty

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
        super().__init__()

    def __repr__(self) -> str:
        start = f"{file[self.start & 7]}{rank[self.start >> 4]}"
        end = f"{file[self.end & 7]}{rank[self.end >> 4]}"
        return f"{self.piece}{start}{end}"

    def notation(self) -> Generator[str, None, None]:
        start = f"{file[self.start & 7]}{rank[self.start >> 4]}"
        end = f"{file[self.end & 7]}{rank[self.end >> 4]}"
        yield f"{self.piece}{end}"
        yield f"{self.piece}{start}{end}"

    def apply(self, game: Game) -> None:
        self.target = game.board[self.end]
        game.board[self.end] = game.board[self.start]
        game.board[self.start] = Empty()
        if self.target and isinstance(self.target, Rook):
            castling = ("kq", "KQ")[self.target.side][not self.end & 7]
            if castling in game.castling:
                self.castling += castling
        super().apply(game)

    def cancel(self, game: Game) -> None:
        game.board[self.start] = game.board[self.end]
        game.board[self.end] = self.target
        self.target = None
        super().cancel(game)


from ..pieces.rook import Rook


from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

from .abstract_move import AbstractMove
from .castling_state_move import CastlingStateMove
from ..empty import Empty

if TYPE_CHECKING:
    from ..game import Game
    from ..pieces import Piece


file = "abcdefgh"
rank = "12345678"


class Move(CastlingStateMove):
    target: Piece | None

    def __init__(self, piece: Piece, start: int, end: int) -> None:
        self.piece = piece
        self.start = start
        self.end = end
        super().__init__()

    def __repr__(self) -> str:
        start = f"{file[self.start % 8]}{rank[self.start // 8]}"
        end = f"{file[self.end % 8]}{rank[self.end // 8]}"
        return f"{self.piece}{start}{end}"

    def notation(self) -> Generator[str, None, None]:
        start = f"{file[self.start % 8]}{rank[self.start // 8]}"
        end = f"{file[self.end % 8]}{rank[self.end // 8]}"
        yield f"{self.piece}{end}"
        yield f"{self.piece}{start}{end}"

    def apply(self, game: Game) -> None:
        self.target = game.board[self.end]
        game.board[self.end] = game.board[self.start]
        game.board[self.start] = Empty()
        super(CastlingStateMove, self).apply(game)

        if self.target:
            castling = ("kq", "KQ")[self.target.side][not self.end % 8]
            if (isinstance(self.target, Rook) and castling in game.castling):
                self.castling = str(sorted(self.castling + castling))
                super().apply(game)

    def cancel(self, game: Game) -> None:
        super(CastlingStateMove, self).cancel(game)
        game.board[self.start] = game.board[self.end]
        game.board[self.end] = self.target
        self.target = None

        if self.castling:
            super().cancel(game)


from ..pieces.rook import Rook


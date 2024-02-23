from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

from ..empty import Empty
from ..x88 import SQUARES

if TYPE_CHECKING:
    from ..game import Game
    from ..moves.abstract_move import AbstractMove


def get_vector(handler, target):
    x1, y1 = handler & 7, handler >> 4
    x2, y2 = target & 7, target >> 4
    if x1 == x2:
        if y1 > y2:
            vector = -16
        else:
            vector = 16
    elif y1 == y2:
        if x1 > x2:
            vector = -1
        else:
            vector = 1
    else:
        if x1 > x2:
            if y1 > y2:
                vector = -17
            else:
                vector = 15
        else:
            if y1 > y2:
                vector = -15
            else:
                vector = 17
    return vector


class Piece(Empty):
    notation: str
    repr: tuple[str, str]
    value: int
    vectors: tuple[int]

    def __init__(self, side: bool) -> None:
        super().__init__()
        self.side = side

    def __repr__(self) -> str:
        return self.repr[self.side]

    def __str__(self) -> str:
        return self.notation

    def __bool__(self) -> bool:
        return True

    def handles(self, game: Game, position: int) -> Generator[int, None, None]:
        allowed = self.allowed(game, position)
        for vector in self.vectors:
            if not (square := position + vector) & 0x88 and square in allowed:
                yield square

    def moves(self, game: Game, position: int) -> Generator[AbstractMove, None, None]: 
        allowed = self.allowed(game, position)
        for i in self.handles(game, position):
            if ((not (piece := game.board[i]) or piece.side is not self.side)
                and i in allowed):
                yield Move(self, position, i)

    def allowed(self, game, position) -> set:
        valid = set(SQUARES)
        pinned = False
        king = game.kings[self.side]

        for handler in self.handlers[not self.side]:
            if isinstance(game.board[handler], SlidingPiece):
                vector = get_vector(handler, position)
                square = position
                while not (square := square + vector) & 0x88:
                    if game.board[square]:
                        if square == king:
                            valid = set(range(handler, square, vector))
                            pinned = True
                        break

        handlers = game.board[king].handlers[not self.side]
        if len(handlers) == 1 and not pinned:
            handler = handlers[0]
            return set(range(handler, king, get_vector(handler, king)))
        elif not handlers:
            return valid
        else:
            return set()


from .sliding_piece import SlidingPiece
from ..moves.move import Move


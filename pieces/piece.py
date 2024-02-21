from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

from ..empty import Empty

if TYPE_CHECKING:
    from ..game import Game
    from ..moves.abstract_move import AbstractMove


def get_vector(handler, target):
    x1, y1 = handler % 8, handler // 8
    x2, y2 = target % 8, target // 8
    if x1 == x2:
        if y1 > y2:
            vector = -8
        else:
            vector = 8
    elif y1 == y2:
        if x1 > x2:
            vector = -1
        else:
            vector = 1
    else:
        if x1 > x2:
            if y1 > y2:
                vector = -9
            else:
                vector = 7
        else:
            if y1 > y2:
                vector = -7
            else:
                vector = 9
    return vector


def edge(position, vector) -> int:
    x, y = position % 8, position // 8
    if vector == -1:
        return y * 8 - 1
    elif vector == 1:
        return (y + 1) * 8
    elif vector == 8:
        return 64
    elif vector == -8:
        return -1
    elif vector == 9:
        return position + min(7 - x, 7 - y) * 9 + 1
    elif vector == -9:
        return position - min(x, y) * 9 - 1
    elif vector == 7:
        return position + min(x, 7 - y) * 7 + 1
    elif vector == -7:
        return position - min(7 - x, y) * 9 - 1
    raise ValueError


class Piece(Empty):
    notation: str
    repr: tuple[str, str]
    value: int

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
        raise NotImplementedError

    def moves(self, game: Game, position: int) -> Generator[AbstractMove, None, None]: 
        for i in self.handles(game, position):
            if ((not (piece := game.board[i]) or piece.side is not self.side)
                and i in self.allowed(game, position)):
                yield Move(self, position, i)

    def allowed(self, game, position) -> set:
        x, y = position % 8, position // 8
        valid = set(range(64))
        pinned = False
        king = game.kings[self.side]

        for handler in self.handlers[not self.side]:
            if isinstance(game.board[handler], SlidingPiece):
                vector = get_vector(handler, position)
                for i in range(position, edge(position, vector), vector):
                    if game.board[i]:
                        if i == king:
                            valid = set(range(handler, i, vector))
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


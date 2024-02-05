from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

from ..empty import Empty
from ..moves import AbstractMove, Move

if TYPE_CHECKING:
    from ..game import Game


class Piece(Empty):
    char: str
    repr: tuple[str, str]

    def __init__(self, side: bool) -> None:
        self.side = side

    def __repr__(self) -> str:
        return self.repr[self.side]

    def __bool__(self) -> bool:
        return True

    def handles(self, game: Game, position: int) -> Generator[int, None, None]: 
        raise NotImplementedError

    def moves(self, game: Game, position: int) -> Generator[AbstractMove, None, None]: 
        for i in self.handles(game, position):
            if (piece := game.board[i]) and piece.side is self.side:
                continue
            yield Move(self, position, i)


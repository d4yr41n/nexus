from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

from ..moves import AbstractMove

if TYPE_CHECKING:
    from ..game import Game


class Piece:
    repr: tuple[str, str]

    def __init__(self, side: bool) -> None:
        self.side = side

    def __repr__(self) -> str:
        return self.repr[self.side]

    def pin(self, position: int, game: Game):
        x, y = position % 8, position // 8

        right, forward, left, backward = (False,) * 4


    def moves(self, position: int, game: Game) -> Generator[AbstractMove, None, None]: 
        raise NotImplementedError


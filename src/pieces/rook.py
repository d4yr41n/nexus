from __future__ import annotations
from typing import TYPE_CHECKING, Generator

from .sliding_piece import SlidingPiece

if TYPE_CHECKING:
    from ..game import Game


class Rook(SlidingPiece):
    notation = 'R'
    repr = 'r', 'R'
    value = 5
    vectors = 1, 16, -1, -16

    def moves(self, game: Game, position: int) -> Generator[AbstractMove, None, None]: 
        allowed = self.allowed(game, position)
        for i in self.handles(game, position):
            if ((not (piece := game.board[i]) or piece.side is not self.side)
                and i in allowed):
                yield RookMove(self, position, i)



from ..moves.abstract_move import AbstractMove
from ..moves.rook_move import RookMove


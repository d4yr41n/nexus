from __future__ import annotations
from typing import TYPE_CHECKING

from .sliding_piece import SlidingPiece

if TYPE_CHECKING:
    from ..game import Game


class Rook(SlidingPiece):
    notation = 'R'
    repr = 'r', 'R'
    value = 5

    def lines(self, position: int) -> tuple[range, ...]:
        return range(position + vector, (position & 15) + 7 , vector)

    def moves(self, game: Game, position: int) -> Generator[RookMove, None, None]: 
        for i in self.handles(game, position):
            if ((not (piece := game.board[i]) or piece.side is not self.side)
                and i in self.allowed(game, position)):
                yield RookMove(self, position, i)


from ..moves.rook_move import RookMove


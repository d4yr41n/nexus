from __future__ import annotations

from collections.abc import Generator
from typing import TYPE_CHECKING

from .piece import Piece
from .knight import Knight
from .bishop import Bishop
from .rook import Rook
from .queen import Queen
from .piece import Piece

if TYPE_CHECKING:
    from ..moves.abstract_move import AbstractMove


class Pawn(Piece):
    notation = ''
    index = 1
    value = 1
    vectors = 17, 15

    def handles(self, game, position):
        for vector in self.vectors:
            if self.side:
                square = position + vector
            else:
                square = position - vector

            if not square & 0x88:
                yield square

    def moves(self, game, position: int) -> Generator[AbstractMove, None, None]:
        position_rank = position >> 4
        allowed = self.allowed(game, position)

        if self.side:
            start_rank = 1
            promotion_rank = 7
            left = position + 15
            right = position + 17
            forward = position + 16
            double = forward + 16
        else:
            start_rank = 6
            promotion_rank = 0
            left = position - 17
            right = position - 15
            forward = position - 16
            double = forward - 16

        for square in (left, right):
            if (not square & 0x88 and (piece := game.board[square])
                and piece.side is not self.side and square in allowed):
                if square >> 4 == promotion_rank:
                    yield Promotion(self, position, square, Knight)
                    yield Promotion(self, position, square, Bishop)
                    yield Promotion(self, position, square, Rook)
                    yield Promotion(self, position, square, Queen)
                else:
                    yield Move(self, position, square)

        if not game.board[forward] and forward in allowed:
            if forward >> 4 == promotion_rank:
                yield Promotion(self, position, forward, Knight)
                yield Promotion(self, position, forward, Bishop)
                yield Promotion(self, position, forward, Rook)
                yield Promotion(self, position, forward, Queen)
            elif position >> 4 == start_rank and not game.board[double] and double in allowed:
                yield Move(self, position, forward)
                yield DoubleForward(self, position, double, forward)
            else:
                yield Move(self, position, forward)


from ..moves.move import Move
from ..moves.double_forward import DoubleForward
from ..moves.promotion import Promotion


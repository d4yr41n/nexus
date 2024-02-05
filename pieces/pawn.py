from collections.abc import Generator

from .piece import Piece
from ..moves import AbstractMove, Move, DoubleForward

class Pawn(Piece):
    char = ''
    repr = 'p', 'P'

    def handles(self, game, position):
        if self.side:
            yield position + 9
            yield position + 7
        else:
            yield position + 7
            yield position + 9


    def moves(self, game, position: int) -> Generator[AbstractMove, None, None]:
        yield from super().moves(game, position)

        forward = position + 8
        if not game.board[forward]:
            yield Move(self, position, forward)
            double = forward + 8
            if not game.board[forward]:
                yield DoubleForward(self, position, double, forward)


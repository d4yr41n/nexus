from collections.abc import Generator

from .piece import Piece
from ..moves import AbstractMove, Move, DoubleForward

class Pawn(Piece):
    char = ''
    repr = 'p', 'P'

    def handles(self, game, position):
        if self.side:
            s = position + 9
            if game.board[s]:
                yield s
            s = position + 7
            if game.board[s]:
                yield s
        else:
            s = position - 7
            if game.board[s]:
                yield s
            s = position - 9
            if game.board[s]:
                yield s


    def moves(self, game, position: int) -> Generator[AbstractMove, None, None]:
        yield from super().moves(game, position)

        if self.side:
            forward = position + 8
            if not game.board[forward]:
                yield Move(self, position, forward)
                double = forward + 8
                if position // 8 == 1 and not game.board[double]:
                    yield DoubleForward(self, position, double, forward)
        else:
            forward = position - 8
            if not game.board[forward]:
                yield Move(self, position, forward)
                double = forward - 8
                if position // 8 == 6 and not game.board[double]:
                    yield DoubleForward(self, position, double, forward)



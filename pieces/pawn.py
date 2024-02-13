from collections.abc import Generator

from .piece import Piece
from .knight import Knight
from .bishop import Bishop
from .rook import Rook
from .queen import Queen
from ..moves import AbstractMove, Move, DoubleForward, Promotion

class Pawn(Piece):
    char = ''
    repr = 'p', 'P'

    def handles(self, game, position):
        x = position % 8
        if self.side:
            if x < 7:
                yield position + 9
            if x > 0:
                yield position + 7
        else:
            if x > 0:
                yield position - 9
            if x < 7:
                yield position - 7

    def moves(self, game, position: int) -> Generator[AbstractMove, None, None]:
        x, y = position % 8, position // 8

        if self.side:
            right = position + 9
            if x < 7 and (piece := game.board[right]) and piece.side is not self.side:
                if y == 6:
                    yield Promotion(self, position, right, Knight)
                    yield Promotion(self, position, right, Bishop)
                    yield Promotion(self, position, right, Rook)
                    yield Promotion(self, position, right, Queen)
                else:
                    yield Move(self, position, right)

            left = position + 7
            if x > 0 and (piece := game.board[left]) and piece.side is not self.side:
                if y == 6:
                    yield Promotion(self, position, left, Knight)
                    yield Promotion(self, position, left, Bishop)
                    yield Promotion(self, position, left, Rook)
                    yield Promotion(self, position, left, Queen)
                else:
                    yield Move(self, position, left)

            forward = position + 8
            if not game.board[forward]:
                if y == 6:
                    yield Promotion(self, position, forward, Knight)
                    yield Promotion(self, position, forward, Bishop)
                    yield Promotion(self, position, forward, Rook)
                    yield Promotion(self, position, forward, Queen)
                else:
                    yield Move(self, position, forward)
                double = forward + 8
                if y == 1 and not game.board[double]:
                    yield DoubleForward(self, position, double, forward)
        else:
            left = position - 9
            if x > 0 and (piece := game.board[left]) and piece.side is not self.side:
                if y == 1:
                    yield Promotion(self, position, left, Knight)
                    yield Promotion(self, position, left, Bishop)
                    yield Promotion(self, position, left, Rook)
                    yield Promotion(self, position, left, Queen)
                else:
                    yield Move(self, position, left)

            right = position - 7
            if x < 7 and (piece := game.board[right]) and piece.side is not self.side:
                if y == 1:
                    yield Promotion(self, position, right, Knight)
                    yield Promotion(self, position, right, Bishop)
                    yield Promotion(self, position, right, Rook)
                    yield Promotion(self, position, right, Queen)
                else:
                    yield Move(self, position, right)

            forward = position - 8
            if not game.board[forward]:
                if y == 1:
                    yield Promotion(self, position, forward, Knight)
                    yield Promotion(self, position, forward, Bishop)
                    yield Promotion(self, position, forward, Rook)
                    yield Promotion(self, position, forward, Queen)
                else:
                    yield Move(self, position, forward)
                double = forward - 8
                if y == 6 and not game.board[double]:
                    yield DoubleForward(self, position, double, forward)


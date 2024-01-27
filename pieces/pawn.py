from . import Piece


class Pawn(Piece):
    @property
    def moves(self):
        is side is WHITE:
            left = 7
            forward = 8
            right = 9
        elif side is BLACK:
            left = -9
            forward = -8
            right = -7 


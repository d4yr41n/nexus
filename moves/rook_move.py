from .init_move import InitMove
from .move import Move


class RookMove(InitMove, Move):
    def apply(self, game):
        super(Move, self).apply(game)
        castling = ("kq", "KQ")[self.piece.side][not self.start % 8]
        if castling in game.castling:
            self.castling = castling
            super().apply(game)

    def cancel(self, game):
        super().cancel(game)
        super(Move, self).cancel(game)


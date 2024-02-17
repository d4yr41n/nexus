from .castling_state_move import CastlingStateMove
from .move import Move


class RookMove(Move):
    def apply(self, game):
        castling = ("kq", "KQ")[self.piece.side][not self.start % 8]
        if castling in game.castling:
            self.castling = castling
        super().apply(game)


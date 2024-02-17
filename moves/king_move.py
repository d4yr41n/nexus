from .castling_state_move import CastlingStateMove
from .move import Move


class KingMove(Move):
    def apply(self, game):
        castling = ("kq", "KQ")[self.piece.side]
        if castling in game.castling:
            self.castling = castling
        super().apply(game)
        game.kings[self.piece.side] = self.end

    def cancel(self, game):
        super().cancel(game)
        game.kings[self.piece.side] = self.start


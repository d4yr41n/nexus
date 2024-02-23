from .move import Move


class RookMove(Move):
    def apply(self, game):
        castling = ("qk", "QK")[self.piece.side][not self.start & 7]
        if castling in game.castling:
            self.castling += castling
        super().apply(game)

    def cancel(self, game):
        super().cancel(game)


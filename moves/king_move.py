from .init_move import InitMove
from .move import Move



class KingMove(InitMove, Move):
    def apply(self, game):
        super(InitMove, self).apply(game)
        castling = ("kq", "KQ")[self.piece.side]
        if castling in game.castling:
            self.castling = castling
            super().apply(game)
        game.kings[self.piece.side] = self.end

    def cancel(self, game):
        super().cancel(game)
        super(InitMove, self).cancel(game)
        game.kings[self.piece.side] = self.start


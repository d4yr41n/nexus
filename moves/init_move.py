from .abstract_move import AbstractMove
from .move import Move


class InitMove(AbstractMove):
    castling: str | None = None

    def apply(self, game):
        super().apply(game)
        if self.castling:
            game.castling = game.castling.replace(self.castling, '')

    def cancel(self, game):
        super().cancel(game)
        if self.castling:
            game.castling = str(sorted(game.castling + self.castling))
            self.castling = None


class RookMove(InitMove, Move):
    def apply(self, game):
        super(Move, self).apply(game)
        castling = ("kq", "KQ")[self.piece.side][not self.start % 8]
        if castling in game.castling:
            self.castling = castling
            super(InitMove, self).apply(game)


class KingMove(InitMove, Move):
    def apply(self, game):
        super(Move, self).apply(game)
        castling = ("kq", "KQ")[self.piece.side]
        if castling in game.castling:
            self.castling = castling
            super(InitMove, self).apply(game)
        game.kings[self.piece.side] = self.end

    def cancel(self, game):
        super(InitMove, self).cancel(game)
        super(Move, self).cancel(game)
        game.kings[self.piece.side] = self.start



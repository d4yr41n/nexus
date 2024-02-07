from .move import AbstractMove, Move


class AbstractInitMove(AbstractMove):
    castling_side: str

    def apply(self, game):
        game.castling = game.castling.replace(self.castling_side, '')
        super().apply(game)

    def cancel(self, game):
        super().cancel(game)
        game.castling = str(sorted(game.castling + self.castling_side))


class PieceInitMove(AbstractInitMove, Move):
    def apply(self, game):
        super(Move, self).apply(game)
        super(AbstractMove, self).apply(game)

    def cancel(self, game):
        super(Move, self).cancel(game)
        super(AbstractMove, self).cancel(game)


class KingInitMove(PieceInitMove):
    def __init__(self, piece, start, end):
        super().__init__(piece, start, end)
        self.sides = ("kq", "KQ")[piece.side]


class RookInitMove(PieceInitMove):
    def __init__(self, piece, start, end):
        super().__init__(piece, start, end)
        self.sides = ("qk", "QK")[piece.side][not start % 8]
        

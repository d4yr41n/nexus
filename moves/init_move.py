from .move import Move


class InitMove(Move):
    def apply(self, game):
        super().apply(game)
        game.castling = game.castling.replace(self.sides, '')

    def cancel(self, game):
        super().cancel(game)
        game.castling = sorted(game.castling + self.sides)


class KingInitMove(InitMove):
    def __init__(self, piece, start, end):
        super().__init___(piece, start, end)
        self.sides = ("kq", "KQ")[piece.side]


class RookInitMove(InitMove):
    def __init__(self, piece, start, end):
        super().__init___(piece, start, end)
        self.sides = ("qk", "QK")[piece.side][not start % 8]
        

from .move import Move


class InitMove(Move):
    def __init__(self, piece, start, end, sides):
        super().__init__(piece, start, end)
        self.sides = sides

    def apply(self, game):
        super().apply(game)
        game.castling = game.castling.replace(self.sides, '')

    def cancel(self, game):
        super().cancel(game)


from .abstract_move import AbstractMove
from .move import Move


class InitMove(AbstractMove):
    castling: str | None = None

    def apply(self, game):
        if self.castling:
            game.castling = game.castling.replace(self.castling, '')

    def cancel(self, game):
        if self.castling:
            game.castling = str(sorted(game.castling + self.castling))
            self.castling = None


from time import sleep

from .abstract_move import AbstractMove


class CastlingStateMove(AbstractMove):
    castling: str

    def __init__(self):
        self.castling = ''

    def apply(self, game):
        game.castling = game.castling.replace(self.castling, '')

    def cancel(self, game):
        game.castling = ''.join(sorted(game.castling + self.castling))


from . import Piece


class Rook(Piece):
    @property
    def moves(self):
        x, y = self.position % y, self.position // y

        for i in range(1, 8 - x):
            yield self.position + i

        for i in range(1, x + 1):
            yield self.position - i

        for i in range(1, 8 - y):
            yield self.position + 8 * i

        for i in range(1, y + 1):
            yield self.position  - 8 * i



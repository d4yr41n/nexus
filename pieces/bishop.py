from . import Piece


class Rook(Piece):
    @property
    def moves(self):
        x, y = self.position % y, self.position // y

        for i in range(1, 8 - max(x, y)):
            yield self.position + 9 * i

        for i in range(1, 8 - max(x, y)):
            yield self.position + 7 * i

        for i in range(1, max(x, y) + 1):
            yield self.position - 9 * i

        for i in range(1, min(x, y) + 1):
            yield self.position - 7 * i




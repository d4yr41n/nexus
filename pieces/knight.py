from . import Piece


class Knight(Piece):
    @property
    def moves(self):
        x, y = self.position % 8, self.position // 8

        if x < 6 and y < 7:
            yield self.position + 10
        if x < 7 and y < 6:
            yield self.position + 17
        if x > 0 and y < 6:
            yield self.position + 15
        if x > 1 and y < 7:
            yield self.position + 6
        if x > 1 and y > 0:
            yield self.position - 10
        if x > 0 and y > 1:
            yield self.position - 17
        if x < 7 and y > 1:
            yield self.position - 15
        if x < 6 and y > 0:
            yield self.position - 6


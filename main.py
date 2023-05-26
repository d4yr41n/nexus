board = [[0 for j in range(8)] for i in range(8)]


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, coord):
        return Coord(self.x  + coord.x, self.y + coord.y)

    def __mul__(self, factor):
        return Coord(self.x * factor, self.y * factor)


class Piece:
    side: bool
    coord: Coord
    movement: tuple

    def moves(self):
        for coord in self.movement:
            yield self.coord + coord


class Knight(Piece):
    movement = (
        Coord(2, 1), Coord(1, 2), Coord(-1, 2), Coord(-2, 1),
        Coord(-2, -1), Coord(-1, -2), Coord(1, -2), Coord(2, -1)
    )


class Slide(Piece):
    def moves(self):
        for coord in self.movement:
            for i in range(8):
                yield self.coord + coord * i


class Rook(Slide):
    movement = Coord(1, 0), Coord(0, 1), Coord(-1, 0), Coord(0, -1)


class Bishop(Slide):
    movement = Coord(1, 1), Coord(-1, 1), Coord(-1, -1), Coord(1, -1)


class Queen(Slide):
    movement = (
        Coord(1, 0), Coord(1, 1), Coord(0, 1), Coord(-1, 1),
        Coord(-1, 0), Coord(-1, -1), Coord(0, -1), Coord(1, -1)
    )


class King(Piece):
    movement = (
        Coord(1, 0), Coord(1, 1), Coord(0, 1), Coord(-1, 1),
        Coord(-1, 0), Coord(-1, -1), Coord(0, -1), Coord(1, -1)
        )


from const import WHITE, BLACK, COLOR, Empty


class Piece(Empty):
    movement: tuple[int, int]

    def __init__(self, side: WHITE | BLACK, game):
        self.side = side
        self.game = game

    def __str__(self):
        return f"{COLOR[self.side]}{self.char}\033[0m"

    def __bool__(self):
        return True

    def __call__(self, x, y):
        for i, j in self.movement:
            i += x
            j += y
            if -1 < i < 8 and -1 < j < 8:
                piece = self.game.board[i][j]
                if not piece or self.side != piece.side:
                    yield i, j


class Pawn(Piece):
    char = "P"

    def __init__(self, side: WHITE | BLACK, game):
        super().__init__(side, game, coord)
        if side:
            self.movement = (0, 1),
        else:
            self.movement = (0, -1),

    def __call__(self):
        return


class Knight(Piece):
    movement = (
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    )
    char = "N"


class Slide(Piece):
    def __call__(self, x, y):
        for i, j in self.movement:
            for factor in range(8):
                i = i * factor + x
                j = j * factor + y
                if -1 < i < 8 and -1 < j < 8:
                    piece = self.game.board[i][j]
                    if not piece and self.side != piece.side:
                        yield i, j


class Rook(Slide):
    movement = (0, 1), (1, 0), (-1, 0), (0, -1)
    char = "R"


class Bishop(Slide):
    movement = (1, 1), (-1, 1), (-1, -1), (1, -1) 
    char = "B"


class Queen(Slide):
    movement = (
        (0, 1), (1, 1), (1, 0), (-1, 1),
        (-1, 0), (-1, -1), (0, -1), (1, -1)
    )
    char = "Q"


class King(Piece):
    movement = (
        (0, 1), (1, 1), (1, 0), (-1, 1),
        (-1, 0), (-1, -1), (0, -1), (1, -1)
    )
    char = "K"


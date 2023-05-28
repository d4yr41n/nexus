from const import BLACK, WHITE, Empty
from move import Move


class Game:
    board = [[Empty() for _ in range(8)] for _ in range(8)]
    moves = []

    def __init__(self, turn: WHITE | BLACK = WHITE):
        self.turn = turn

    def update(self):
        self.moves.clear()

        for x in range(8):
            for y in range(8):
                if (piece := self.board[x][y]):
                    for i, j in piece(x, y):
                        self.moves.append(
                            Move(piece.side, piece.__class__, x, y, i, j)
                        )
    
    def make(self, move: Move):
        self.board[move.to_x][move.to_y] = self.board[move.on_x][move.on_y]
        self.board[move.on_x][move.on_y] = Empty()

    def move(self, move: Move):
        moves = list(filter(lambda i: i == Move, self.moves))
        if len(moves) == 1:
            self.make(moves[0])
            self.turn = not self.turn
            self.update()


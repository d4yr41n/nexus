from const import BLACK, WHITE, Empty, Coord
from piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King, Slide
from move import Move


class Game:
    over = False
    board = tuple([Empty() for _ in range(8)] for _ in range(8))
    history = [Move()]
    moves = []
    controls = []
    coords = tuple(Coord(x, y) for x in range(8) for y in range(8))
    result: -1 | 0 | 1 = 0

    def __init__(self, turn: BLACK | WHITE = WHITE):
        self.turn = turn

    def get(self, coord: Coord):
        return self.board[coord.x][coord.y]

    def king(self):
        for coord in self.coords:
            if (piece := self.get(coord)):
                if isinstance(piece, King) and self.turn == piece.side:       
                    return coord

    def control(self):
        self.controls.clear()

        for coord in self.coords:
            if (piece := self.get(coord)):
                if self.turn != piece.side:
                    for coord in piece.controls(coord): 
                        self.controls.append(coord)
                                                   
    def update(self):                                                          
        self.moves.clear()                                                     

        for coord in self.coords:
            if (piece := self.get(coord)):
                if self.turn == piece.side:
                    for move in piece.moves(coord):   
                        self.make(move)
                        self.control()
                        if self.king() not in self.controls:
                            self.moves.append(move)
                        self.undo(move)

        if not self.moves:
            self.control()
            if self.king() in self.controls:
                self.result = -1 if self.turn else 1
            else:
                self.result = 0
            self.over = True

    def undo(self, move: None | Move = None):
        if not move and len(self.history) > 1:
            move = self.history[-1]

        if move:    
            if move.promotion:
                self.board[move.to.x][move.to.y] = Pawn(move.piece.side, self)
            elif move.extra:
                self.board[move.extra[0].x][move.extra[0].y] = self.get(
                    move.extra[1]
                )
                self.board[move.extra[1].x][move.extra[1].y] = Empty()
            elif move.empty:
                self.board[move.empty.x][move.empty.y] = move.buffer

            self.board[move.on.x][move.on.y] = self.get(move.to)
            self.board[move.to.x][move.to.y] = move.buffer

            if move.moved:
                move.piece.moved = False

    def make(self, move: Move):
        move.buffer = self.get(move.to)
        self.board[move.to.x][move.to.y] = self.get(move.on)
        self.board[move.on.x][move.on.y] = Empty()

        if move.promotion:
            self.board[move.to.x][move.to.y] = move.promotion(
                move.piece.side, self
            )
        elif move.extra:
            self.board[move.extra[1].x][move.extra[1].y] = self.get(
                move.extra[0]
            )
            self.board[move.extra[0].x][move.extra[0].y] = Empty()
        elif move.empty:
            move.buffer = self.get(move.empty)
            self.board[move.empty.x][move.empty.y] = Empty()

        if move.moved and not move.piece.moved:
            move.piece.moved = True
        else:
            move.moved = False
 
    def move(self, string: str):
        moves = list(filter(lambda move: move == string, self.moves))
        if len(moves) == 1:
            move = moves[0]
            self.make(move)
            self.history.append(move)
            self.turn = not self.turn
            self.update()
    
    def setup(self):
        self.end = False
        self.over = False
        self.board = tuple([Empty() for _ in range(8)] for _ in range(8))
        self.history = [Move()]
        self.moves = []
        self.controls = []
        self.coords = tuple(Coord(x, y) for x in range(8) for y in range(8))
        self.result = 0
        self.turn = WHITE

        for rank, side in (7, BLACK), (0, WHITE):
            self.board[0][rank] = Rook(side, self)
            self.board[1][rank] = Knight(side, self)
            self.board[2][rank] = Bishop(side, self)
            self.board[3][rank] = Queen(side, self)
            self.board[4][rank] = King(side, self)
            self.board[5][rank] = Bishop(side, self)
            self.board[6][rank] = Knight(side, self)
            self.board[7][rank] = Rook(side, self)

        for i in range(8):
            self.board[i][1] = Pawn(WHITE, self)
            self.board[i][6] = Pawn(BLACK, self)

        self.update()


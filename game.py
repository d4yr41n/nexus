from const import BLACK, WHITE, Empty, Coord
from piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King, Slide
from move import Move


PIECES = {
    Knight.notation: Knight,
    Bishop.notation: Bishop,
    Rook.notation: Rook,
    Queen.notation: Queen,
}


class Game:
    end = False
    board = tuple([Empty() for _ in range(8)] for _ in range(8))
    backup: None | tuple = None
    pep: None | Coord = None
    moves = []
    controls = []
    coords = tuple(Coord(x, y) for x in range(8) for y in range(8))
    en_passant: None | Coord = None
    result: str = ""

    def __init__(self, turn: WHITE | BLACK = WHITE):
        self.turn = turn

    def get(self, coord: Coord):
        return self.board[coord.x][coord.y]

    def king(self):
        for coord in self.coords:
            if (piece := self.get(coord)):
                if piece.__class__ == King and self.turn == piece.side:       
                    return coord

    def check(self):
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
                        self.check()
                        if self.king() not in self.controls:
                            self.moves.append(move)
                        self.undo()

        if not self.moves:
            if self.king() in self.controls:
                self.result = f"{('Black', 'White')[not self.turn]} won"
            else:
                self.result = "Draw"
            self.end = True


    def undo(self):
        if self.backup:
            self.board = self.backup
            self.en_passant = self.pep
            if self.lm.moved:
                self.lm.piece.moved = False


    def make(self, move: Move):
        self.backup = tuple(i[:] for i in self.board)
        self.pep = self.en_passant
        self.lm = move

        self.board[move.to.x][move.to.y] = self.get(move.on)
        self.board[move.on.x][move.on.y] = Empty()
        if (new := move.new):
            if isinstance(move.new, Coord):
                self.board[move.new.x][move.new.y] = self.get(move.empty)
            else:
                self.board[move.to.x][move.to.y] = move.new(
                    move.piece.side, self
                )
        if move.empty:
            self.board[move.empty.x][move.empty.y] = Empty()
        self.en_passant = move.en_passant
        if move.moved and not move.piece.moved:
            move.piece.moved = True
        else:
            move.moved = False

    
    def move(self, string: str):
        new = PIECES.get(string[-1])
        if new:
            string = string[:-1]

        moves = list(filter(lambda move: move == string, self.moves))
        if len(moves) == 1:
            move = moves[0]
            if move.new and new:
                move.new = new
            if move.new is True:
                return
            if (
                not move.new or move.new.__class__ == Coord
                or issubclass(move.new, Piece) or issubclass(move.new, Slide)
            ):
                self.make(move)
                self.turn = not self.turn
                self.update()
                    
    def setup(self):
        self.board = tuple([Empty() for _ in range(8)] for _ in range(8))
        self.end = False
        self.result = ""

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

        self.turn = WHITE

        self.update()


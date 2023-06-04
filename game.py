from const import EMPTY, BLACK, WHITE
from config import CHARS, COLORS
from piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King, Slide
from move import Move


class Game:
    squares = tuple(i + j for i in range(21, 92, 10) for j in range(1, 9))
    board: list
    turn: BLACK | WHITE
    moves = []
    history = []
    over: bool
    run: bool = False
    result: -1 | 0 | 1

    def __init__(self):
        self.reset()

    def __str__(self):
        output = "    a b c d e f g h\n\n"
        for y in range(91, 20, -10):
            output += f"{(y - 11) // 10}   "
            for x in range(1, 9):
                piece = self.board[y + x]
                char = CHARS[piece]
                if piece:
                    output += f"{COLORS[piece.side]}{char}\033[0m "
                else:
                    output += f"{char} "
            output += f"  {(y - 11) // 10}\n"
        output += "\n    a b c d e f g h\n"
        return output


    def reset(self):
        self.board = [
            EMPTY if square in self.squares else None for square in range(120)
        ]
        self.turn = WHITE
        self.moves.clear()
        self.history.clear()
        self.over = False
        self.result = 0

    def control(self):
        for square in self.squares:
            if (piece := self.board[square]):
                if self.turn != piece.side:
                    yield from piece.control(square)

    def king(self):
        for square in self.squares:
            if (piece := self.board[square]):
                if isinstance(piece, King) and self.turn == piece.side:
                    return square

    def update(self):
        self.moves.clear()

        for square in self.squares:
            if (piece := self.board[square]):
                if self.turn == piece.side:
                    for move in piece.moves(square):
                        self.make(move)
                              
                        if self.king() not in self.control():
                            self.moves.append(move)

                        self.undo(move)

        if not self.moves:
            if self.king() in self.control():
                self.result = -1 if self.turn else 1
            else:
                self.result = 0
            self.over = True

    def cancel():
        if self.history:
            self.undo(self.history[-1])
            self.update()

    def undo(self, move: Move):
        if move.promotion:
            self.board[move.target] = Pawn(move.piece.side, self)
        elif move.extra:
            self.board[move.extra[0]] = self.board[move.extra[1]]
            self.board[move.extra[1]] = EMPTY
        elif move.empty:
            self.board[move.empty] = move.buffer

        self.board[move.square] = self.board[move.target]
        self.board[move.target] = move.buffer

        if move.moved:
            move.piece.moved = False

    def make(self, move: Move):
        move.buffer = self.board[move.target]
        self.board[move.target] = self.board[move.square]
        self.board[move.square] = EMPTY

        if move.promotion:
            self.board[move.target] = move.promotion(move.piece.side, self)
        elif move.extra:
            self.board[move.extra[1]] = self.board[move.extra[0]]
            self.board[move.extra[0]] = EMPTY
        elif move.empty:
            move.buffer = self.board[move.empty]
            self.board[move.empty] = EMPTY

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
        self.reset()
        self.run = True

        for square, side in (92, BLACK), (22, WHITE):
            self.board[square] = Rook(side, self)
            self.board[square + 1] = Knight(side, self)
            self.board[square + 2] = Bishop(side, self)
            self.board[square + 3] = Queen(side, self)
            self.board[square + 4] = King(side, self)
            self.board[square + 5] = Bishop(side, self)
            self.board[square + 6] = Knight(side, self)
            self.board[square + 7] = Rook(side, self)

        for square in range(8):
            self.board[square + 32] = Pawn(WHITE, self)
            self.board[square + 82] = Pawn(BLACK, self)

        self.update()


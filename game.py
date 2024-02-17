from .pieces import Bishop, Piece, Knight, King, Rook, Queen, Pawn
from .empty import Empty
from .moves import AbstractMove


class Game:
    turn: bool
    board: list[Piece | Empty] = [Empty() for _ in range(64)]
    record = []
    en_passant: int | None = None
    castling: str = "KQkq"
    kings: list[int]
    moves: list[AbstractMove] = []

    def annotate(self):
        exclude = []
        annotated = {}
        for move in self.moves:
            for notation in move.notation():
                if notation not in exclude:
                    if notation in annotated:
                        exclude.append(notation)
                        del annotated[notation]
                    else:
                        annotated[notation] = move
        return annotated

    def setup(self) -> None:
        self.board[0] = Rook(True)
        self.board[1] = Knight(True)
        self.board[2] = Bishop(True)
        self.board[3] = Queen(True)
        self.board[4] = King(True)
        self.board[5] = Bishop(True)
        self.board[6] = Knight(True)
        self.board[7] = Rook(True)
        
        for i in range(8, 16):
            self.board[i] = Pawn(True)

        self.board[56] = Rook(False)
        self.board[57] = Knight(False)
        self.board[58] = Bishop(False)
        self.board[59] = Queen(False)
        self.board[60] = King(False)
        self.board[61] = Bishop(False)
        self.board[62] = Knight(False)
        self.board[63] = Rook(False)
 
        super().__init__()
        for i in range(48, 56):
            self.board[i] = Pawn(False)

        self.turn = True

        self.kings = [59, 4]
        self.update()

    def update(self):
        self.moves.clear()

        for i in range(64):
            self.board[i].handlers[0].clear()
            self.board[i].handlers[1].clear()

        for i in range(64):
            if (piece := self.board[i]):
                for j in piece.handles(self, i):
                    self.board[j].handlers[piece.side].append(i)

        king = self.kings[self.turn]
        if len(self.board[king].handlers[not self.turn]) == 2:
            self.moves.extend(self.board[king].moves(self, king))
        else:
            for i in range(64):
                if (piece := self.board[i]) and piece.side is self.turn:
                    self.moves.extend(piece.moves(self, i))

    def apply(self, move):
        move.apply(self)
        self.record.append(move)
        self.update()

    def input(self, notation: str):
        if (move := self.annotate().get(notation)):
            self.apply(move)


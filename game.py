from typing import Literal

from .pieces.bishop import Bishop
from .pieces.piece import Piece
from .pieces.knight import Knight
from .pieces.king import King
from .pieces.rook import Rook
from .pieces.queen import Queen
from .pieces.pawn import Pawn
from .empty import Empty
from .moves.abstract_move import AbstractMove
from .x88 import SQUARES


class Game:
    turn: bool
    board: list[Empty | None]
    record: list
    en_passant: int | None = None
    castling: str = "KQkq"
    kings: list[int]
    moves: list[AbstractMove]
    result: Literal[-1, 0, 1] | None = None

    def __init__(self):
        self.board = [Empty() if i in SQUARES else None for i in range(128)]
        self.record = []
        self.kings = []
        self.moves = []

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
        
        for i in range(16, 24):
            self.board[i] = Pawn(True)

        self.board[112] = Rook(False)
        self.board[113] = Knight(False)
        self.board[114] = Bishop(False)
        self.board[115] = Queen(False)
        self.board[116] = King(False)
        self.board[117] = Bishop(False)
        self.board[118] = Knight(False)
        self.board[119] = Rook(False)
 
        super().__init__()
        for i in range(96, 104):
            self.board[i] = Pawn(False)

        self.turn = True

        self.kings = [116, 4]
        self.update()

    def update(self):
        self.moves.clear()

        for i in SQUARES:
            self.board[i].handlers[0].clear()
            self.board[i].handlers[1].clear()

        for i in SQUARES:
            if (piece := self.board[i]):
                for j in piece.handles(self, i):
                    self.board[j].handlers[piece.side].append(i)

        king = self.kings[self.turn]
        if len(self.board[king].handlers[not self.turn]) == 2:
            self.moves.extend(self.board[king].moves(self, king))
        else:
            for i in SQUARES:
                if (piece := self.board[i]) and piece.side is self.turn:
                    self.moves.extend(piece.moves(self, i))

        if not self.moves:
            if self.board[king].handlers[not self.turn]:
                self.result = (1, -1)[self.turn]
            else:
                self.result = 0
        else:
            self.result = None
            

    def apply(self, move):
        move.apply(self)
        self.record.append(move)
        self.update()

    def cancel(self):
        self.record[-1].cancel(self)
        del self.record[-1]
        self.update()

    def input(self, notation: str):
        if (move := self.annotate().get(notation)):
            self.apply(move)


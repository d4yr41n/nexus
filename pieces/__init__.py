from __future__ import annotations

from typing import TYPE_CHECKING

from const import BLACK, WHITE
from move import Move

if TYPE_CHECKING:
    from game import Game


class Piece:
    code: int
    offsets: tuple[int]
    notation: str
    value: int

    def __index__(self):
        return self.code

    def __init__(self, side: WHITE | BLACK, game: Game):
        self.side = side
        self.game = game

    def control(self, square: int):
        for offset in self.offsets:
            offset += square
            if self.game.board[offset] != None:
                yield offset

    def moves(self, square: int):
        for target in self.control(square):
            piece = self.game.board[target]
            if not piece or self.side != piece.side:
                yield Move(self, square, target)


class Pawn(Piece):
    code = 1
    notation = ""
    value = 1

    def __init__(self, side: BLACK | WHITE, game: Game):
        super().__init__(side, game)
        if side:
            self.start = 3
            self.promotion = 9
            self.offset = 10
            self.offsets = 11, 9
        else:
            self.start = 8
            self.promotion = 2
            self.offset = -10
            self.offsets = -11, 9

    def moves(self, square: int):
        for target in self.control(square):
            piece = self.game.board[target]
            if piece and self.side != piece.side:
                if target // 10 == self.promotion:
                    for piece in (Knight, Bishop, Rook, Queen):
                        yield Move(self, square, target, promotion=piece)
                else:
                    yield Move(self, square, target)

        target = square + self.offset
        if not self.game.board[target]:
            if target // 10 == self.promotion:
                for piece in (Knight, Bishop, Rook, Queen):
                    yield Move(self, square, target, promotion=piece)
            else:
                yield Move(self, square, target)
            
            if square // 10 == self.start:
                target += self.offset
                if not self.game.board[target]:
                    yield Move(self, square, target, en_passant=target)

        if self.game.history and (
            en_passant := self.game.history[-1].en_passant
        ):
            if square - 1 <= en_passant <= square + 1:
                yield Move(
                    self, square, en_passant + self.offset,
                    empty=self.en_passant
                )


class Knight(Piece):
    code = 2
    offsets = 12, 21, 19, 8, -12, -21, -19, -8
    notation = "N"


class Slide(Piece):
    def control(self, square: int):
        for offset in self.offsets:
            for factor in range(1, 8):
                target = square + offset * factor
                if self.game.board[target] == None:
                    break
                yield target
                if self.game.board[target]:
                    break

    def moves(self, square: int):
        for target in self.control(square):
            if (piece := self.game.board[target]):
                if self.side != piece.side:
                    yield Move(self, square, target)
            else:
                yield Move(self, square, target)


class Bishop(Slide):
    code = 3
    offsets = 11, 9, -11, -9
    notation = "B"


class Rook(Slide):
    moved: bool = False
    code = 4
    offsets = 1, 10, -1, -10
    notation = "R"


class Queen(Slide):
    code = 5
    offsets = 1, 11, 10, 9, -1, -11, -10, -9
    notation = "Q"


class King(Piece):
    moved: bool = False
    code = 6
    offsets = 1, 11, 10, 9, -1, -11, -10, -9
    notation = "K"

    def moves(self, square: int):
        for target in self.control(square):
            piece = self.game.board[target]
            if not piece or self.side != piece.side:
                yield Move(self, square, target, moved=True)

        control = tuple(self.game.control())
        if not self.moved and square not in control:
            rook = square - 4
            if self.game.board[rook] and not self.game.board[rook].moved:
                for factor in range(1, 4):
                    check = square - factor
                    if self.game.board[check] or check in control:
                        break
                else:
                    yield Move(
                        self, square, square - 2, 
                        extra=(rook, rook + 3),
                        queen_castling=True, moved=True
                    )

            rook = square + 3
            if self.game.board[rook] and not self.game.board[rook].moved:
                for factor in range(1, 3):
                    check = square + factor
                    if self.game.board[check] or check in control:
                        break
                else:
                    yield Move(
                        self, square, square + 2,
                        extra=(rook, rook - 2),
                        king_castling=True, moved=True
                    )


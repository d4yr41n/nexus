from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from piece import Piece


FILES = "abcdefgh"
RANKS = "12345678"


def notation(square):
    return f"{FILES[(square - 22) % 10]}{RANKS[(square - 22) // 10]}"


class Move:
    def __init__(
        self,
        piece: None | Piece = None,
        square: None | int = None,
        target: None | int = None,
        en_passant: None | int = None,
        empty: bool | int = False,
        extra: bool | tuple[int, int] = False,
        promotion: bool | Piece = False,
        moved: bool = False,
        queen_castling: bool = False,
        king_castling: bool = False
    ):
        self.piece = piece
        self.square = square
        self.target = target
        self.en_passant = en_passant
        self.empty = empty
        self.extra = extra
        self.promotion = promotion
        self.moved = moved
        self.king_castling = king_castling
        self.queen_castling = queen_castling
        self.buffer = None

        if self.king_castling:
            self.notation = "0-0", "O-O"
        elif self.queen_castling:
            self.notation = "0-0-0", "O-O-O"
        else:
            if self.promotion:
                promotion = self.promotion.notation
            else:
                promotion = ""
            square = notation(self.square)
            target = notation(self.target)
            self.notation = (
                f"{self.piece.notation}{square}{target}{promotion}",
                f"{self.piece.notation}{target}{promotion}"
            )

    def __eq__(self, move: str):
        for notation in self.notation:
            if notation == move:
                return True


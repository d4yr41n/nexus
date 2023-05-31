from __future__ import annotations

from typing import TYPE_CHECKING

from const import BLACK, WHITE, Coord

if TYPE_CHECKING:
    from piece import Piece


class Move:
    check: bool = False

    def __init__(
        self,
        piece: None | Piece = None,
        on: None | Coord = None,
        to: None | Coord = None,
        en_passant: None | Coord = None,
        empty: bool | Coord = False,
        extra: bool | tuple[Coord, Coord] = False,
        promotion: bool | Piece = False,
        moved: bool = False,
        short_castle: bool = False,
        long_castle: bool = False
    ):
        self.piece = piece
        self.on = on
        self.to = to
        self.en_passant = en_passant
        self.empty = empty
        self.extra = extra
        self.promotion = promotion
        self.moved = moved
        self.short_castle = short_castle
        self.long_castle = long_castle
        self.buffer: None | Piece = None
        
    def __bool__(self):
        return True

    def notation(self):
        if self.short_castle:
            yield "0-0"
            yield "O-O"
        elif self.long_castle:
            yield "0-0-0"
            yield "O-O-O"
        else:
            for notation in (
                f"{self.piece.notation}{self.on}{self.to}",
                f"{self.piece.notation}{self.to}"
            ):
                if self.promotion:
                    notation += self.promotion.notation
                yield notation

    def __eq__(self, string: str):
        for notation in self.notation():
            if notation == string:
                return True



from __future__ import annotations

from typing import TYPE_CHECKING

from const import BLACK, WHITE, Coord

if TYPE_CHECKING:
    from piece import Piece


class Move:
    check: bool = False

    def __init__(
        self, piece: Piece,
        on: Coord, to: Coord,
        en_passant: None | Coord = None,
        empty: bool | Coord = False,
        new: bool | Piece = False,
        moved: bool = False,
        notation: None | str = None
    ):
        self.piece = piece
        self.on = on
        self.to = to
        self.en_passant = en_passant
        self.empty = empty
        self.new = new
        self.moved = moved
        self.notation = notation
        
    def __bool__(self):
        return True

    def __str__(self):
        return self.notation or f"{self.piece.notation}{self.on}{self.to}"

    def __eq__(self, notation: str):
        return str(self) == notation


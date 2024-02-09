from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

from .piece import Piece
from ..moves import Castling, Move

if TYPE_CHECKING:
    from ..game import Game


class King(Piece):
    char = 'K'
    repr = 'k', 'K'

    def handles(self, game: Game, position: int) -> Generator[int, None, None]:
        x, y = position % 8, position // 8
        if x < 7:
            yield position + 1
        if x > 0:
            yield position - 1
        if y < 7:
            yield position + 8
        if y > 0:
            yield position - 8
        if x < 7 and y < 7:
            yield position + 9
        if x > 0 and y < 7:
            yield position + 7
        if x < 7 and y > 0:
            yield position - 7
        if x > 0 and y > 0:
            yield position - 9

    def moves(self, game: Game, position: int) -> Generator[Move | Castling, None, None]:
        for i in self.handles(game, position):
            if (piece := game.board[i]) and piece.side is self.side:
                continue

            if not game.board[i].handlers[self.side]:
                yield Move(self, position, i)

        if ("kK"[self.side] in game.castling
            and not (f := game.board[position + 1]) and not f.handlers
            and not (g := game.board[position + 2]) and not g.handlers):
            yield Castling(position, position + 3)

        if ("qQ"[self.side] in game.castling
            and not (d := game.board[position - 1]) and not d.handlers
            and not (c := game.board[position - 2]) and not c.handlers
            and not (b := game.board[position - 3]) and not b.handlers):
            yield Castling(position, position - 4)


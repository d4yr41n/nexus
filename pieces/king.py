from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

from .piece import Piece, get_vector
from .sliding_piece import SlidingPiece
from ..x88 import SQUARES

if TYPE_CHECKING:
    from ..game import Game


class King(Piece):
    notation = 'K'
    repr = 'k', 'K'
    value = 0
    vectors = 1, 17, 16, 15, -1, -17, -16, -15

    def allowed(self, game, position) -> set:
        valid = set(SQUARES)
        for handler in self.handlers[not self.side]:
            if isinstance(game.board[handler], SlidingPiece):
                vector = get_vector(handler, position)
                edge = position
                while not (edge := edge - vector) & 0x88:
                    if game.board[edge]:
                        break
                valid -= set(range(handler + vector, edge, vector))
        return valid

    def moves(self, game: Game, position: int) -> Generator[KingMove | Castling, None, None]:
        allowed = self.allowed(game, position)
        for i in self.handles(game, position):
            if ((not (piece := game.board[i]) or piece.side is not self.side)
                and not game.board[i].handlers[not self.side]
                and i in allowed):
                yield KingMove(self, position, i)

        if ("kK"[self.side] in game.castling
            and not (f := game.board[position + 1]) and not f.handlers[not self.side]
            and not (g := game.board[position + 2]) and not g.handlers[not self.side]):
            yield Castling(position, position + 3)

        if ("qQ"[self.side] in game.castling
            and not (d := game.board[position - 1]) and not d.handlers[not self.side]
            and not (c := game.board[position - 2]) and not c.handlers[not self.side]
            and not (b := game.board[position - 3]) and not b.handlers[not self.side]):
            yield Castling(position, position - 4)


from ..moves.castling import Castling
from ..moves.king_move import KingMove


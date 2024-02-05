from .pieces import Bishop, Piece, Knight, Rook
from .empty import Empty


class Game:
    turn: bool
    board: list[Piece | Empty] = [Empty()] * 64
    record = []
    en_passant: int | None = None
    castling = "KQkq"

    def setup(self) -> None:
        self.board[1] = Bishop(True)

    @property
    def moves(self):
        for i in range(64):
            if (piece := self.board[i]):
                yield from piece.moves(self, i)

    def apply(self, move):
        move.apply(self)
        self.record.append(move)


from .pieces import Bishop, Piece, Knight, Rook
from .empty import Empty


class Game:
    turn: bool
    board: list[Piece | Empty] = [Empty()] * 64
    record = []
    en_passant: int | None = None
    castling: str = "KQkq"

    def setup(self) -> None:
        self.board[1] = Bishop(True)

    def update(self):
        for i in range(64):
            if (piece := self.board[i]):
                for j in piece.handles(self, i):
                    self.board[j].handers[piece.side].append(i)

        for i in range(64):
            if (piece := self.board[i]):
                yield from piece.moves(self, i)

    def apply(self, move):
        move.apply(self)
        self.record.append(move)


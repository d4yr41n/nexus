from .pieces import Piece, Knight


class Game:
    turn: bool
    board: list[Piece | None] = [None] * 64
    record = []
    en_passant: int | None = None
    castling = "KQkq"

    def setup(self) -> None:
        self.board[1] = Knight(True)

    @property
    def moves(self):
        for i in range(64):
            if (piece := self.board[i]):
                yield from piece.moves(i)

    def apply(self, move):
        move.apply(self)
        self.record.append(move)


from pieces import Piece


class AbstractMove:
    def apply(self, game):
        pass

    def cancel(self, game):
        pass


class Move(AbstractMove):
    capture: Piece | None = None

    def __init__(self, piece, start: int, end: int) -> None:
        self.piece = piece
        self.start = start
        self.end = end

    def apply(self, game):
        if game.board[self.end]:
            self.capture = game.board[self.end]
        game.board[self.end] = game.board[self.start]
        game.board[self.start] = None

    def cancel(self, game):
        game.board[self.start] = game.board[self.end]
        game.board[self.end] = self.capture


class Castling(AbstractMove):
    def __init__(self, king, rook):
        self.king = king
        self.rook = rook

    def apply(self, game):
        if self.king > self.rook:
            pass
        else:
            pass

    def cancel(self, game):
        pass

class EnPassant(Move):
    en_passant: int | None = None

    def apply(self, game):
        self.capture = game.board[game.en_passant]
        game.board[game.en_passant] = None
        self.en_passant = game.en_passant
        game.en_passant = None
        game.board[self.end] = game.board[self.start]
        game.board[self.start] = None

    def cancel(self, game):
        game.en_paasant = self.en_passant
        self.en_passant = None
        game.board[game.en_passant] = self.capture
        self.capture = None
        game.board[self.start] = game.board[self.end]
        game.board[self.end] = None


class Promotion(Capture):
    pass


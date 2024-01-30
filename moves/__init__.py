from pieces import Piece



class AbstractMove:
    def apply(self, game):
        pass

    def cancel(self, game):
        pass


class Move(AbstractMove):
    promotion: Piece | None

    def __init__(self, piece, start: int, end: int) -> None:
        self.piece = piece
        self.start = start
        self.end = end

    def apply(self, game):
        game.board[self.end] = game.board[self.start]
        game.board[self.start] = None

    def cancel(self, game):
        game.board[self.start] = game.board[self.end]
        game.board[self.end] = None
        
class KingsideCastling(Move):
    pass


class QueensideCastling(Move):
    pass


class EnPassant(Capture):
    pass


class Promotion(Capture):
    pass


from piece import Pawn, Knight, Bishop, Rook, Queen, King


class Move:
    pieces = {
        "N": Knight,
        "B": Bishop,
        "R": Rook,
        "Q": Queen,
        "K": King
    }
    files = dict(zip("abcdefgh", range(8)))
    ranks = dict(zip("12345678", range(8)))

    def __init__(self, side, piece, on_x, on_y, to_x, to_y):
        self.side = side
        self.piece = piece
        self.on_x = on_x
        self.on_y = on_y
        self.to_x = to_x
        self.to_y = to_y
        
    def __eq__(self, move):
        return (
            self.side == move.side
            and self.piece == move.piece
            and self.to_x == move.to_x
            and self.to_y == move.to_y
        )

    def __bool__(self):
        return True

    @classmethod
    def from_string(cls, side, string):
        cls.side = side
        if len(string) > 1:
            cls.piece = cls.pieces.get(string[0], Pawn)
            to_x, to_y = cls.files.get(string[-2]), cls.ranks.get(string[-1])
            if to_x != None and to_y != None:
                cls.to_x = to_x
                cls.to_y = to_y
                return cls


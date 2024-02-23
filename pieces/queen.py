from .sliding_piece import SlidingPiece


class Queen(SlidingPiece):
    notation = 'Q'
    repr = 'q', 'Q'
    value = 9
    vectors = 1, 17, 16, 15, -1, -17, -16, -15


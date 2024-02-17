from .piece import Piece


def get_vector(handler, target):
    x1, y1 = handler % 8, handler // 8
    x2, y2 = target % 8, target // 8
    if x1 == x2:
        if y1 > y2:
            vector = -8
        else:
            vector = 8
    elif y1 == y2:
        if x1 > x2:
            vector = -1
        else:
            vector = 1
    else:
        if x1 > x2:
            if y1 > y2:
                vector = -9
            else:
                vector = 7
        else:
            if y1 > y2:
                vector = -7
            else:
                vector = 9
    return vector


class BasePiece(Piece):
    def allowed(self, game, position):
        valid = range(64)
        pinned = False
        king = game.kings[self.side]

        for handler in self.handlers[not self.side]:
            if isinstance(game.board[handler], SlidingPiece):
                vector = get_vector(handler, position)
                for i in range(position, -1, vector):
                    if game.board[i]:
                        if i == king:
                            valid = range(handler, position, vector)
                            pinned = True
                        break

        handlers = game.board[king].handlers
        if len(handlers) == 1 and not pinned:
            handler = handlers[0]
            return range(handler, king, get_vector(handler, position))
        elif not handlers:
            return valid


from .sliding_piece import SlidingPiece


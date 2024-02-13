class PinnedPiece
    def pin(self, game):
        allowed = range(64)
        for handler in self.handlers[not self.side]:
            if isinstance(game.board[handler], SlidingPiece):
                x1, y1 = position % 8, position // 8
                x2, y2 = handler % 8, handler // 8

                if x1 == x2:
                    if y1 > y2:
                        d = 8
                    else:
                        d = -8
                elif y1 == y2:
                    if x1 > x2:
                        d = 1
                    else:
                        d = -1
                else:
                    if x1 > x2:
                        if y1 > y2:
                            d = 9
                        else:
                            d = -7
                    else:
                        if y1 > y2:
                            d = 7
                        else:
                            d = -9

                king = game.kings[self.side]
                for i in range(position, -1, d):
                    if game.board[i]:
                        if i == king:
                            allowed = range(handler, position, d)
                        break
                else:
                    continue
                break
        return allowed


class Game:
    board = [None] * 128
    moves = []
    
    def update(self):
        for piece in self.board:
            if piece is not None:
                for move in piece.moves:
                    self.moves.append(
                        Move(piece,  move)
                    )


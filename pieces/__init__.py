from typing import Generator


class Piece:
    def __init__(self, side: bool) -> None:
        self.side = side

    def moves(self, position: int) -> Generator[int, None, None]: 
        raise NotImplementedError


from __future__ import annotations


BLACK = False
WHITE = True

FILES = "abcdefgh"
RANKS = "12345678"


class Empty:
    index = 0

    def __bool__(self):
        return False

    def __index__(self):
        return self.index


class Coord:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def __str__(self):
        return f"{FILES[self.x]}{RANKS[self.y]}"

    def __eq__(self, coord: Coord):
        return self.x == coord.x and self.y == coord.y

    def __bool__(self):
        return -1 < self.x < 8 and -1 < self.y < 8

    def __add__(self, coord: Coord):
        return Coord(self.x + coord.x, self.y + coord.y)

    def __sub__(self, coord: Coord):
        return Coord(self.x - coord.x, self.y - coord.y)

    def __mul__(self, factor: int):
        return Coord(self.x * factor, self.y * factor)


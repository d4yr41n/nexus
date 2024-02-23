from __future__ import annotations

from math import inf

from ..moves.abstract_move import AbstractMove
from ..x88 import SQUARES


class Node:
    move: AbstractMove
    nodes: list[Node]
    value: float

    def __init__(self, game, move, depth):
        self.move = move
        game.apply(move)
        if depth:
            self.nodes = [Node(game, i, depth - 1) for i in game.moves]
            if self.nodes:
                self.value = (min, max)[game.turn](self.nodes, key=lambda node: node.value).value
            else:
                self.value = self.eval(game)
        else:
            self.nodes = []
            self.value = self.eval(game)
        game.cancel()

    # def __repr__(self):
    #     string = str(self.move) + ' ' + str(self.value) + '\n'
    #     for node in self.nodes:
    #         string += '\t' + str(node)
    #     return string

    def eval(self, game):
        value = 0
        if game.result == -1:
            return -inf
        elif game.result == 1:
            return inf
        for i in SQUARES:
            if (piece := game.board[i]):
                if piece.side:
                    value += piece.value
                else:
                    value -= piece.value
            if i in (51, 52, 67, 68):
                value = round(value - len(piece.handlers[0]) * .3, 1)
                value = round(value + len(piece.handlers[1]) * .3, 1)
            else:
                value = round(value - len(piece.handlers[0]) * .2, 1)
                value = round(value + len(piece.handlers[1]) * .2, 1)
        return value


class AI:
    side: bool
    depth: int

    def __init__(self, side, depth):
        self.side = side
        self.depth = depth

    def get_move(self, game):
        nodes = [Node(game, move, self.depth) for move in game.moves]
        return (min, max)[game.turn](nodes, key=lambda node: node.value).move


from __future__ import annotations

from ..moves.abstract_move import AbstractMove


class Node:
    move: AbstractMove
    nodes: list[Node]
    value: float

    def __init__(self, game, move, depth):
        self.move = move
        game.apply(move)
        if depth:
            self.nodes = [Node(game, i, depth - 1) for i in game.moves]
            self.value = (min, max)[game.turn](self.nodes, key=lambda node: node.value).value
        else:
            self.nodes = []
            self.value = self.eval(game)
        game.cancel()

    def __repr__(self):
        string = str(self.move) + ' ' + str(self.value) + '\n'
        for node in self.nodes:
            string += '\t' + str(node)
        return string

    def eval(self, game):
        value = 0
        for i in range(64):
            if (piece := game.board[i]):
                if piece.side:
                    value += piece.value
                else:
                    value -= piece.value
            if i in (27, 28, 35, 36):
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


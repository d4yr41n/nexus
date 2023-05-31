from game import BLACK, WHITE, Game
from piece import Pawn, Knight, Bishop
from const import COLOR
from move import Move


game = Game()

try:
    while True:
        print("\033[H\033[J", end="")
        print("    a b c d e f g h\n")
        for y in range(7, -1, -1):
            print(y + 1, end="   ")
            for x in range(8):
                if (piece := game.board[x][y]):
                    print(f"{COLOR[piece.side]}{piece}\033[0m", end=" ")
                else:
                    print(piece, end=" ")
            print(f"  {y + 1}")
        print("\n    a b c d e f g h\n")
        if game.end:
            print(game.result)
        for move in game.moves:
            print(str(move), end=" ")
        if (action := input("\n\n> ")):
            match action:
                case "start" | "restart":
                    game.setup()
                case "exit":
                    break
                case "undo":
                    game.undo()
                case _:
                    game.move(action)
except KeyboardInterrupt:
    print()


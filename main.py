from game import BLACK, WHITE, Game
from piece import Pawn, Knight, Bishop
from config import COLORS, CHARS
from move import Move


RESULTS = ("Draw", "White won", "Black won")

game = Game()

try:
    while True:
        print("\033[H\033[J", end="")
        print(game)
        
        if game.over:
            print(f"{RESULTS[game.result]}\n")

        match (action := input("> ")):
            case "new":
                game.setup()
            case "exit":
                break
            case "undo":
                game.undo()
            case _:
                game.move(action)

except KeyboardInterrupt:
    print()


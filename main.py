from const import RESULTS
from game import Game


game = Game()

try:
    while True:
        print("\033[H\033[J", end="")
        print(game)
        
        if game.over:
            print(f"{RESULTS[game.result]}\n")

        match (action := input("> ")):
            case "new":
                game = Game()
            case "exit":
                break
            case "cancel":
                game.cancel()
            case _:
                game.move(action)

except KeyboardInterrupt:
    print()


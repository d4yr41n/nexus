from os import system

from const import RESULTS
from game import Game


system("")

game = Game()

try:
    while True:
        print("\033[H\033[J", end="")
        print(game)
        
        if game.over:
            print(f"{RESULTS[game.result]}\n")

        action = input("> ")
        if action == "new":
            game = Game()
        elif action == "exit":
            break
        elif action == "cancel":
            game.cancel()
        else:
            game.move(action)

except KeyboardInterrupt:
    print()


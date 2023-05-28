from game import BLACK, WHITE, Game
from piece import Pawn, Knight
from move import Move


game = Game()
game.board[0][1] = Pawn(WHITE, game)
game.board[7][6] = Pawn(BLACK, game)
game.update()

while True:
    print("\033[H\033[J", end="")
    print("    a b c d e f g h\n")
    for y in range(7, -1, -1):
        print(y + 1, end="   ")
        for x in range(8):
            print(game.board[x][y], end=" ")
        print(f"  {y + 1}")
    print("\n    a b c d e f g h\n")
    move = Move.from_string(game.turn, input("> ")) 
    if move:
        game.move(move)


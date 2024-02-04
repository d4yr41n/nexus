from curses import curs_set, napms, newwin, wrapper, use_default_colors, KEY_ENTER
from curses.textpad import Textbox

from .game import Game


class Client:
    def main(self, stdscr) -> None:
        use_default_colors()
        data = ""
        game = Game()
        game.setup()
        moves = {str(move): move for move in  game.moves}
        help = False
    
        while True:
            stdscr.erase()
    
            stdscr.addstr("    a b c d e f g h\n\n")
            for i in range(8, 0, -1):
                stdscr.addstr(
                    f"{i}   {' '.join(str(i) if i else '·' for i in game.board[(i-1)*8:i*8])}   {i}\n"
                )
            stdscr.addstr("\n    a b c d e f g h")

            l = len(game.record)
            for i in range(0, len(game.record), 2):
                stdscr.addstr(i // 2, 26, f"{i // 2 + 1}. {game.record[i]}{ f' - {game.record[i+1]}' if l - 1 > i else ''}")

            stdscr.addstr(13, 0, f"> {data}")

            if help:
                stdscr.addstr(15, 0, ' '.join(str(i) for i in moves))
    
            c = stdscr.getch()
            if c == 113:
                break
            elif c == 10:
                if (move := moves.get(data)):
                    game.apply(move)
                    moves = {str(move): move for move in  game.moves}
                data = ''
            elif c == 263:
                data = data[:-1]
            elif c == 9:
                help = True
            else:
                data += chr(c)
    

if __name__ == "__main__":
    client = Client()
    wrapper(client.main)


from curses import curs_set, napms, newwin, wrapper, use_default_colors, KEY_ENTER
from curses.textpad import Textbox
from string import ascii_letters

from .game import Game


allowed = ascii_letters + "-0123456789"


class Client:
    def main(self, stdscr) -> None:
        curs_set(0)
        use_default_colors()
        data = ""
        game = Game()
        game.setup()
        moves = game.annotate()
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
                if data == "exit":
                    break
                elif (move := moves.get(data)):
                    game.apply(move)
                    moves = game.annotate()
                data = ''
            elif c == 263:
                data = data[:-1]
            elif c == 9:
                help = True
            else:
                char = chr(c)
                if char in allowed:
                    data += chr(c)
    

if __name__ == "__main__":
    client = Client()
    wrapper(client.main)


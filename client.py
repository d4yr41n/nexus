from os import system
from time import sleep
from urllib.request import Request, urlopen

from const import BLACK, WHITE, RESULTS


system("")

url = "https://nexus-ubsn.onrender.com"

urlopen(Request(url, method="POST"))

try:
    while True:
        print("\033[H\033[J", end="")
        side = input("Your side? black or white\n> ")
        if side == "black":
            side = BLACK
            move = "black"
            break
        elif side == "white":
            side = WHITE
            move = "white"
            break
    
    
    while True:
        print("\033[H\033[J", end="")
        print(urlopen(url).read().decode("utf-8"))
    
        over = int(urlopen(f"{url}/over").read().decode("utf-8"))
        if over:
            result = int(urlopen(f"{url}/result").read().decode("utf-8"))
            print(RESULTS[result])
            break
        else:
            turn = int(urlopen(f"{url}/turn").read().decode("utf-8"))
            if side == turn:
                urlopen(
                    Request(
                        f"{url}/{move}",
                        data=input("> ").encode("utf-8"),
                        method="POST"
                    )
                )
            else:
                sleep(1)
except KeyboardInterrupt:
    print()


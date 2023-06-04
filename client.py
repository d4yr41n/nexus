from time import sleep
from urllib.request import Request, urlopen

from const import BLACK, WHITE


url = "http://127.0.0.1:8000"

while True:
    side = input("Your side\n> ")
    if side == "black":
        side = BLACK
        path = "black"
        break
    elif side == "white":
        side = WHITE
        path = "white"
        break

urlopen(Request(url, method="POST"))

while True:
    print("\033[H\033[J", end="")

    print(urlopen(url).read().decode("utf-8"))

    turn = urlopen(f"{url}/turn").read().decode("utf-8")
    if turn == "False":
        turn = BLACK
    elif turn == "True":
        turn = WHITE
    if side == turn:
        urlopen(
            Request(
                f"{url}/{path}",
                data=input("> ").encode("utf-8"),
                method="POST"
            )
        )
    else:
        sleep(1)


BLACK = False
WHITE = True

COLOR = ("\033[34m", "\033[31m")


class Empty:
    char = "."

    def __bool__(self):
        return False

    def __str__(self):
        return self.char



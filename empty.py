class Empty:
    handlers: tuple[list, list] = ([], [])

    def __repr__(self) -> str:
        return '.'

    def __bool__(self) -> bool:
        return False


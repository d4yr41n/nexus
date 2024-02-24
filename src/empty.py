from .config import CHARS


class Empty:
    index: int = 0
    handlers: tuple[list, list]

    def __init__(self) -> None:
        self.handlers = [], []

    def __repr__(self) -> str:
        return CHARS[self.index]

    def __bool__(self) -> bool:
        return False


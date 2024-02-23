from __future__ import annotations
from collections.abc import Generator
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..game import Game


class AbstractMove:
    castling: str = ''
    en_passant: int | None = None

    def __repr__(self) -> str:
        raise NotImplementedError

    def notation(self) -> Generator[str, None, None]:
        raise NotImplementedError

    def apply(self, game: Game) -> None:
        self.en_passant = game.en_passant
        game.en_passant = None
        game.turn = not game.turn
        for i in self.castling:
            game.castling = game.castling.replace(i, '')

    def cancel(self, game: Game) -> None:
        game.en_passant = self.en_passant
        self.en_passant = None
        game.turn = not game.turn
        if self.castling:
            game.castling += self.castling


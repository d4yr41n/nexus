from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..game import Game


class AbstractMove:
    en_passant: int | None = None

    def __repr__(self) -> str:
        raise NotImplementedError

    def apply(self, game: Game) -> None:
        self.en_passant = game.en_passant
        game.en_passant = None

    def cancel(self, game: Game) -> None:
        game.en_passant = self.en_passant
        self.en_passant = None


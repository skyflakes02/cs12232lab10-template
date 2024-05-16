from argparse import ArgumentParser
from dataclasses import dataclass
from random import Random, getrandbits
from typing import Final

import pyxel

import pyxelgrid as pg
import pipelib as pl


TITLE: Final[str] = "Pipe Dream"
FPS: Final[int] = 25


@dataclass
class CellState:
    ... # TODO


class PipeGame(pg.PyxelGrid[CellState]):
    def __init__(self, settings: pl.DifficultySettings, seed: int) -> None:
        self.settings = settings
        self.seed = seed
        self.rand = Random(seed)

        ... # TODO

        super().__init__(settings.r, settings.c, dim=pl.DIM)

    def init(self) -> None:
        pyxel.mouse(True)
        pyxel.load(pl.PIPE_RESOURCE_PATH)
        pyxel.rseed(self.seed)

        ... # TODO

    def update(self) -> None:

        # TODO remove this debugging message
        print("The mouse is at cell", self.mouse_cell())

        ... # TODO

    def draw_cell(self, i: int, j: int, x: int, y: int) -> None:

        ... # TODO

    def pre_draw_grid(self) -> None:
        
        ... # TODO

    def post_draw_grid(self) -> None:
        
        ... # TODO


def main():
    # No need to change the code in `main`
    parser = ArgumentParser(description=f"Run the '{TITLE}' game.")

    parser.add_argument('-d', '--difficulty', default='easy',
        help=f"the game difficulty. must be one of: {', '.join(pl.DIFFICULTY_SETTINGS.keys())} (default: %(default)s)")
    parser.add_argument('-s', '--seed', type=int, default=None,
        help="the seed for the random number generator. (default: based on system time)")

    args = parser.parse_args()

    if (seed := args.seed) is None:
        seed = getrandbits(31)

    if args.difficulty not in pl.DIFFICULTY_SETTINGS:
        raise ValueError(f"Unknown difficulty: {args.difficulty}")

    PipeGame(settings=pl.DIFFICULTY_SETTINGS[args.difficulty], seed=seed).run(title=TITLE, fps=FPS)


if __name__ == '__main__':
    main()

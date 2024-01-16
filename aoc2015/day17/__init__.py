import itertools
import os
from typing import Iterable

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def combination(containers: list[int]) -> Iterable[tuple[int, ...]]:
    for n in range(1, len(containers) + 1):
        yield from itertools.combinations(containers, n)


def part1(input_path: str = INPUT_PATH, total: int = 150) -> int:
    containers = [int(line) for line in read_as_lines(input_path)]

    exact_combos = (combo for combo in combination(containers) if sum(combo) == total)

    return len(list(exact_combos))


def part2(input_path: str = INPUT_PATH, total: int = 150) -> int:
    containers = [int(line) for line in read_as_lines(input_path)]

    exact_combos = (combo for combo in combination(containers) if sum(combo) == total)

    combo_lengths = [len(combo) for combo in exact_combos]
    min_len = min(combo_lengths)

    return len([combo_len for combo_len in combo_lengths if combo_len == min_len])

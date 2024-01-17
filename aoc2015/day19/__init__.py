import os
import re
from typing import Iterable

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")

Replacement = tuple[str, str]


def parse_replacement(line: str) -> Replacement:
    old, new = line.split(" => ")
    return old, new


def mutate(string: str, replacements: Iterable[Replacement]) -> list[str]:
    mutations: set[str] = set()

    for old, new in replacements:
        for m in re.finditer(old, string):
            mutations.add(string[: m.start()] + new + string[m.end() :])

    return list(mutations)


def part1(input_path: str = INPUT_PATH) -> int:
    *lines, _, molecule = read_as_lines(input_path)
    replacements = [parse_replacement(line) for line in lines]

    return len(mutate(molecule, replacements))


def part2(input_path: str = INPUT_PATH, molecule: str | None = None) -> int:
    *lines, _, input_molecule = read_as_lines(input_path)
    replacements = [parse_replacement(line) for line in lines]

    rep_map = {out_str[::-1]: in_str[::-1] for in_str, out_str in replacements}

    def rep(m: re.Match) -> str:
        return rep_map[m.group()]

    target = "e"
    molecule = (molecule or input_molecule)[::-1]

    step = 0
    while molecule != target:
        molecule = re.sub("|".join(rep_map.keys()), rep, molecule, 1)
        step += 1

    return step

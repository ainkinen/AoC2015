import os
from collections import Counter

from aoc2015.utils.files import read_as_string

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def part1(in_str: str | None = None) -> int:
    if not in_str:
        in_str = read_as_string(INPUT_PATH)

    counts = Counter(in_str)
    return counts["("] - counts[")"]


def part2(in_str: str | None = None) -> int:
    if not in_str:
        in_str = read_as_string(INPUT_PATH)

    counter = 0
    for position, char in enumerate(in_str, start=1):
        counter += 1 if char == "(" else -1
        if counter == -1:
            return position

    return -1

import os
from collections import defaultdict

from aoc2015.utils.files import read_as_string

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def part1(input_path: str = INPUT_PATH) -> int:
    limit = int(read_as_string(input_path))

    house_presents: dict[int, int] = defaultdict(int)
    for elf in range(1, limit // 10):
        for house in range(elf, limit // 10, elf):
            house_presents[house] += elf * 10

    for house in house_presents.keys():
        if house_presents[house] >= limit:
            return house

    raise Exception("Answer not found")


def part2(input_path: str = INPUT_PATH) -> int:
    limit = int(read_as_string(input_path))

    house_presents: dict[int, int] = defaultdict(int)
    for elf in range(1, limit // 10):
        for house_idx in range(1, 51):
            idx = elf * house_idx
            house_presents[idx] += elf * 11

    for house in house_presents.keys():
        if house_presents[house] >= limit:
            return house

    raise Exception("Answer not found")

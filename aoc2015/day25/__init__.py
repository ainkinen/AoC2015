import os
import re

from aoc2015.utils.files import read_as_string

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def next_val(prev: int) -> int:
    return (prev * 252533) % 33554393


def get_num_idx(row: int, column: int) -> int:
    return sum(range(row + column - 1)) + column


def part1(input_path: str = INPUT_PATH) -> int:
    row, column = map(int, re.findall(r"\d+", read_as_string(input_path)))

    value = 20151125
    for _ in range(1, get_num_idx(row, column)):
        value = next_val(value)

    return value

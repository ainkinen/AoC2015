import os
import re
from itertools import combinations
from math import prod

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")

Box = tuple[int, int, int]  # l, w, h


def parse_box(line: str) -> Box:
    length, width, height = map(int, re.findall(r"\d+", line))
    return length, width, height


def wrapper(box: Box) -> int:
    sides = list(map(prod, combinations(box, 2)))
    return sum(2 * side for side in sides) + min(sides)


def ribbon(box: Box) -> int:
    min_sides = sorted(box)[:2]
    return 2 * sum(min_sides)


def bow(box: Box) -> int:
    return prod(box)


def part1(input_path: str = INPUT_PATH) -> int:
    boxes = [parse_box(line) for line in read_as_lines(input_path)]

    return sum(wrapper(box) for box in boxes)


def part2(input_path: str = INPUT_PATH) -> int:
    boxes = [parse_box(line) for line in read_as_lines(input_path)]

    return sum(ribbon(box) + bow(box) for box in boxes)

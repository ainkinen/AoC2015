import operator
import os
import re
from typing import Callable

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")

analysis = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

Details = dict[str, int]

ops: dict[str, Callable[[int, int], bool]] = {
    "cats": operator.gt,
    "trees": operator.gt,
    "pomeranians": operator.lt,
    "goldfish": operator.lt,
}


def parse_details(string: str) -> tuple[int, Details]:
    name_and_number, *data_pairs = re.findall(r"(\w+)\W+(\d+)", string)
    name, number = name_and_number

    return int(number), {k: int(v) for k, v in data_pairs}


def part1(input_path: str = INPUT_PATH) -> int:
    lines = read_as_lines(input_path)
    sues = {idx: details for idx, details in map(parse_details, lines)}

    for detail, number in analysis.items():
        for idx in list(sues.keys()):
            sue = sues[idx]
            if detail in sue and sue[detail] != number:
                del sues[idx]

    if len(sues) > 1:
        raise Exception("Multiple matches!")

    return list(sues.keys())[0]


def part2(input_path: str = INPUT_PATH) -> int:
    lines = read_as_lines(input_path)
    sues = {idx: details for idx, details in map(parse_details, lines)}

    for detail, number in analysis.items():
        for idx in list(sues.keys()):
            sue = sues[idx]
            op = ops.get(detail, operator.eq)
            if detail in sue and not op(sue[detail], number):
                del sues[idx]

    if len(sues) > 1:
        raise Exception("Multiple matches!")

    return list(sues.keys())[0]

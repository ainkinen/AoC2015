import os
import re
from collections import defaultdict
from typing import NamedTuple, Callable, Any, Literal

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Instruction(NamedTuple):
    rx: range
    ry: range
    op1: Callable[[bool], bool]
    op2: Callable[[int], int]


def true(_: Any) -> Literal[True]:
    return True


def false(_: Any) -> Literal[False]:
    return False


def toggle(state: bool) -> bool:
    return not state


def increase(value: int) -> int:
    return value + 1


def decrease(value: int) -> int:
    return max(value - 1, 0)


def bump(value: int) -> int:
    return value + 2


def parse_instruction(line: str) -> Instruction:
    op1: Callable
    if line.startswith("turn on"):
        op1 = true
    elif line.startswith("turn off"):
        op1 = false
    else:
        op1 = toggle

    op2: Callable
    if line.startswith("turn on"):
        op2 = increase
    elif line.startswith("turn off"):
        op2 = decrease
    else:
        op2 = bump

    numbers = list(map(int, re.findall(r"\d+", line)))
    rx = range(numbers[0], numbers[2] + 1)
    ry = range(numbers[1], numbers[3] + 1)

    return Instruction(rx, ry, op1, op2)


def part1(input_path: str = INPUT_PATH) -> int:
    instructions = [parse_instruction(line) for line in read_as_lines(input_path)]

    lights: dict[tuple[int, int], bool] = defaultdict(bool)

    for ins in instructions:
        for y in ins.ry:
            for x in ins.rx:
                key = y, x
                lights[key] = ins.op1(lights[key])

    return sum(lights.values())


def part2(input_path: str = INPUT_PATH) -> int:
    instructions = [parse_instruction(line) for line in read_as_lines(input_path)]

    lights: dict[tuple[int, int], int] = defaultdict(int)

    for ins in instructions:
        for y in ins.ry:
            for x in ins.rx:
                key = y, x
                lights[key] = ins.op2(lights[key])

    return sum(lights.values())

import os
import re

from aoc2015.utils.files import read_as_string

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def look_and_say(string: str) -> str:
    repeats: list[tuple[str, str]] = re.findall(r"((\d)\2*)", string)
    return "".join(str(len(block)) + char for block, char in repeats)


def part1(input_path: str = INPUT_PATH) -> int:
    string = read_as_string(input_path)

    for _ in range(40):
        string = look_and_say(string)

    return len(string)


def part2(input_path: str = INPUT_PATH) -> int:
    string = read_as_string(input_path)

    for _ in range(50):
        string = look_and_say(string)

    return len(string)

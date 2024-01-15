import os

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def part1(input_path: str = INPUT_PATH) -> int:
    lines = read_as_lines(input_path)
    strings = [eval(line) for line in lines]

    len_literals = sum(map(len, lines))
    len_strings = sum(map(len, strings))

    return len_literals - len_strings


def escape(string: str) -> str:
    encoded = string.translate(
        str.maketrans(
            {
                '"': r"\"",
                "\\": r"\\",
            }
        )
    )
    return f'"{encoded}"'


def part2(input_path: str = INPUT_PATH) -> int:
    lines = read_as_lines(input_path)

    encoded = [escape(line) for line in lines]

    len_encoded = sum(map(len, encoded))
    len_literals = sum(map(len, lines))

    return len_encoded - len_literals

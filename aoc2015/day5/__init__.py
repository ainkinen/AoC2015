import os
import re

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def is_nice(string: str) -> bool:
    has_three_vowels = len(re.findall(r"[aeiou]", string)) >= 3

    has_double_letter = bool(re.search(r"(.)\1", string))

    no_bad_strings = not re.search(r"ab|cd|pq|xy", string)

    return has_three_vowels and has_double_letter and no_bad_strings


def is_nicer(string: str) -> bool:
    has_repeating_pair = bool(re.search(r"(\w\w).*\1", string))

    has_repeated_with_spacer = bool(re.search(r"(\w).\1", string))

    return has_repeating_pair and has_repeated_with_spacer


def part1(input_path: str = INPUT_PATH) -> int:
    strings = read_as_lines(input_path)

    return len([s for s in strings if is_nice(s)])


def part2(input_path: str = INPUT_PATH) -> int:
    strings = read_as_lines(input_path)

    return len([s for s in strings if is_nicer(s)])

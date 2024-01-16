import os

from aoc2015.day16 import part1, parse_details, part2

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


def test_parse_details():
    assert parse_details("Sue 1: goldfish: 6, trees: 9, akitas: 0") == (
        1,
        {
            "goldfish": 6,
            "trees": 9,
            "akitas": 0,
        },
    )


def test_part1():
    assert part1(TEST_INPUT_PATH) == 3


def test_part2():
    assert part2(TEST_INPUT_PATH) == 4

import os

from aoc2015.day8 import part1, part2

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


def test_part1():
    assert part1(TEST_INPUT_PATH) == 12


def test_part2():
    assert part2(TEST_INPUT_PATH) == 19

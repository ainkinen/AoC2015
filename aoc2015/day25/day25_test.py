import os

from aoc2015.day25 import part1

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


def test_part1():
    assert part1(TEST_INPUT_PATH) == 27995004

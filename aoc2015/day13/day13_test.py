import os

from aoc2015.day13 import part1, rotate

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


def test_rotate():
    assert rotate(["bob", "alice", "jennifer", "mike"]) == [
        "alice",
        "jennifer",
        "mike",
        "bob",
    ]


def test_part1():
    assert part1(TEST_INPUT_PATH) == 330

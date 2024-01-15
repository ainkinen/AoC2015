import os

import pytest

from aoc2015.day11 import increment, rotate

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


@pytest.mark.parametrize(
    "string, expected",
    [
        # ["a", "b"],
        # ["az", "ba"],
        # ["ahz", "aja"],
        ["hepxxyzy", "hepxxyzz"],
    ],
)
def test_increment(string: str, expected: str):
    assert increment(string) == expected


@pytest.mark.parametrize(
    "password, new",
    [
        ["abcdfezz", "abcdffaa"],
        ["abcdefgh", "abcdffaa"],
        ["ghhzzzzz", "ghjaabcc"],
    ],
)
def test_rotate(password: str, new: str):
    assert rotate(password) == new

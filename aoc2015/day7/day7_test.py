import os

import pytest

from aoc2015.day7 import part1

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


@pytest.mark.parametrize(
    "output_wire, value",
    [
        ["d", 72],
        ["e", 507],
        ["f", 492],
        ["g", 114],
        ["h", 65412],
        ["i", 65079],
        ["x", 123],
        ["y", 456],
    ],
)
def test_part1(output_wire: str, value: int):
    assert part1(TEST_INPUT_PATH, output_wire) == value

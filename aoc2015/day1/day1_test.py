import os

import pytest

from aoc2015.day1 import part1, part2

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")

cases_part1 = [
    ["(())", 0],
    ["()()", 0],
    ["(((", 3],
    ["(()(()(", 3],
    ["))(((((", 3],
    ["())", -1],
    ["))(", -1],
    [")))", -3],
    [")())())", -3],
]


@pytest.mark.parametrize("in_str, expected_floor", cases_part1)
def test_part1(in_str: str, expected_floor: int):
    assert part1(in_str) == expected_floor


cases_part2 = [
    [")", 1],
    ["()())", 5],
]


@pytest.mark.parametrize("in_str, expected_position", cases_part2)
def test_part2(in_str: str, expected_position: int):
    assert part2(in_str) == expected_position

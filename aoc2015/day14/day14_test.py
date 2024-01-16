import os

import pytest

from aoc2015.day14 import part1, part2, distance, Reindeer

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


@pytest.mark.parametrize(
    "reindeer, seconds, expected_distance",
    [
        [Reindeer("Comet", 14, 10, 127), 1, 14],
        [Reindeer("Comet", 14, 10, 127), 10, 140],
        [Reindeer("Comet", 14, 10, 127), 11, 140],
        [Reindeer("Comet", 14, 10, 127), 137, 140],
        [Reindeer("Comet", 14, 10, 127), 138, 154],
        [Reindeer("Comet", 14, 10, 127), 1000, 1120],
        [Reindeer("Dancer", 16, 11, 162), 1000, 1056],
    ],
)
def test_distance(reindeer: Reindeer, seconds: int, expected_distance: int):
    assert distance(reindeer, seconds) == expected_distance


def test_part1():
    assert part1(TEST_INPUT_PATH, seconds=1000) == 1120


def test_part2():
    assert part2(TEST_INPUT_PATH, seconds=1000) == 689

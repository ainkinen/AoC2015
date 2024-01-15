import os

import pytest

from aoc2015.day4 import part1

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


@pytest.mark.skip(reason="Slow")
def test_part1():
    assert part1(TEST_INPUT_PATH) == 1048970

import os

from aoc2015.day17 import part1, part2, combination

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


def test_combination():
    assert list(combination([1, 2, 3])) == [
        (1,),
        (2,),
        (3,),
        (1, 2),
        (1, 3),
        (2, 3),
        (1, 2, 3),
    ]

    assert list(combination([3, 3, 1])) == [
        (3,),
        (3,),
        (1,),
        (3, 3),
        (3, 1),
        (3, 1),
        (3, 3, 1),
    ]


def test_part1():
    assert part1(TEST_INPUT_PATH, total=25) == 4


def test_part2():
    assert part2(TEST_INPUT_PATH, total=25) == 3

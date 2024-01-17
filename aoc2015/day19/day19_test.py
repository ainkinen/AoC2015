import os

import pytest

from aoc2015.day19 import part1, mutate, Replacement

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")

test_replacements = [
    ("H", "HO"),
    ("H", "OH"),
    ("O", "HH"),
]

test_replacements_2 = [
    ("e", "H"),
    ("e", "O"),
    ("H", "HO"),
    ("H", "OH"),
    ("O", "HH"),
]


@pytest.mark.parametrize(
    "replacements, in_str, expected",
    [
        [test_replacements, "HOH", {"HOOH", "HOHO", "OHOH", "HHHH"}],
        [
            test_replacements,
            "HOHOHO",
            {
                "HOOHOHO",
                "HOHOOHO",
                "HOHOHOO",
                "OHOHOHO",
                "HOOHOHO",
                "HOHOOHO",
                "HHHHOHO",
                "HOHHHHO",
                "HOHOHHH",
            },
        ],
    ],
)
def test_mutate(replacements: list[Replacement], in_str: str, expected: set[str]):
    assert set(mutate(in_str, replacements)) == expected


def test_part1():
    assert part1(TEST_INPUT_PATH) == 7

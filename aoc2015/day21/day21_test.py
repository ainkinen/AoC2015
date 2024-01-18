import os

from aoc2015.day21 import part1, part2, player_wins, Character

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


def test_player_wins():
    assert (
        player_wins(
            player=Character(8, 5, 5),
            boss=Character(12, 7, 2),
        )
        is True
    )


def test_part1():
    assert part1(TEST_INPUT_PATH, player_hit_points=8) == 65


def test_part2():
    assert part2(TEST_INPUT_PATH, player_hit_points=8) == 188

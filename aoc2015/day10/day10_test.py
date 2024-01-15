from aoc2015.day10 import look_and_say


def test_part1():
    string = "1"

    for _ in range(5):
        string = look_and_say(string)

    assert string == "312211"

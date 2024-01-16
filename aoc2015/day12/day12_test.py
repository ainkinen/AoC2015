import json
import os

import pytest

from aoc2015.day12 import part1, part2, sum_values

TEST_INPUT_PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


class TestSumValues:
    @pytest.mark.parametrize(
        "json_str, output",
        [
            ["[1,2,3]", 6],
            ['{"a":2,"b":4}', 6],
            ["[[[3]]]", 3],
            ['{"a":{"b":4},"c":-1}', 3],
            ['{"a":[-1,1]}', 0],
            ['[-1,{"a":1}]', 0],
            ["[]", 0],
            ["{}", 0],
            ['[1,{"c":"red","b":2},3]', 6],
            ['{"d":"red","e":[1,2,3,4],"f":5}', 15],
            ['[1,"red",5]', 6],
        ],
    )
    def test_with_reds(self, json_str: str, output: int):
        assert sum_values(json.loads(json_str)) == output

    @pytest.mark.parametrize(
        "json_str, output",
        [
            ["[1,2,3]", 6],
            ['{"a":2,"b":4}', 6],
            ["[[[3]]]", 3],
            ['{"a":{"b":4},"c":-1}', 3],
            ['{"a":[-1,1]}', 0],
            ['[-1,{"a":1}]', 0],
            ["[]", 0],
            ["{}", 0],
            ['[1,{"c":"red","b":2},3]', 4],
            ['{"d":"red","e":[1,2,3,4],"f":5}', 0],
            ['[1,"red",5]', 6],
        ],
    )
    def test_without_reds(self, json_str: str, output: int):
        assert sum_values(json.loads(json_str), ignore_reds=True) == output


def test_part1():
    assert part1(TEST_INPUT_PATH) == 18


def test_part2():
    assert part2(TEST_INPUT_PATH) == 8

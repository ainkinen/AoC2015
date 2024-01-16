import json
import os
from typing import Any

from aoc2015.utils.files import read_as_string

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def sum_values(json_obj: Any, ignore_reds: bool = False) -> int:
    match json_obj:
        case int():
            return json_obj
        case str():
            return 0
        case dict():
            if ignore_reds and "red" in json_obj.values():
                return 0
            return sum(sum_values(v, ignore_reds) for v in json_obj.values())
        case list():
            return sum(sum_values(v, ignore_reds) for v in json_obj)
        case _:
            raise Exception(f"Unknown json type {type(json_obj)}")


def part1(input_path: str = INPUT_PATH) -> int:
    json_obj = json.loads(read_as_string(input_path))
    return sum_values(json_obj)


def part2(input_path: str = INPUT_PATH) -> int:
    json_obj = json.loads(read_as_string(input_path))
    return sum_values(json_obj, ignore_reds=True)

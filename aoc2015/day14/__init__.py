import os
import re
from typing import NamedTuple

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Reindeer(NamedTuple):
    name: str
    speed: int
    sprint: int
    rest: int


def parse_reindeer(line: str) -> Reindeer:
    name, rest = line.split(" ", maxsplit=1)
    speed, sprint, rest = list(map(int, re.findall(r"\d+", rest)))

    return Reindeer(name, speed, sprint, rest)


def distance(reindeer: Reindeer, seconds: int) -> int:
    name, speed, sprint, rest = reindeer
    cycle = sprint + rest

    full_cycles, leftover_time = divmod(seconds, cycle)

    last_run_seconds = min(sprint, leftover_time)

    return full_cycles * sprint * speed + last_run_seconds * speed


def reindeer_scores(reindeer: list[Reindeer], seconds: int) -> list[int]:
    distances = [distance(r, seconds) for r in reindeer]
    max_distance = max(distances)
    return [1 if d == max_distance else 0 for d in distances]


def part1(input_path: str = INPUT_PATH, seconds: int = 2503) -> int:
    reindeer = [parse_reindeer(line) for line in read_as_lines(input_path)]
    return max(distance(r, seconds) for r in reindeer)


def part2(input_path: str = INPUT_PATH, seconds: int = 2503) -> int:
    reindeer = [parse_reindeer(line) for line in read_as_lines(input_path)]

    scores: list[int] = [0 for _ in reindeer]

    for time in range(1, seconds + 1):
        scores = [
            old_score + new_points
            for old_score, new_points in zip(scores, reindeer_scores(reindeer, time))
        ]

    return max(scores)

import itertools
import os
from collections import defaultdict

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")

DistanceMap = dict[str, dict[str, int]]  # from -> to -> dist


def parse_distance_map(lines: list[str]) -> DistanceMap:
    d_map: DistanceMap = defaultdict(dict)

    for line in lines:
        city_a, _, city_b, *_, dist = line.split(" ")

        # collect both directions for simple access
        d_map[city_a][city_b] = int(dist)
        d_map[city_b][city_a] = int(dist)

    return d_map


def total_distance(route: tuple[str, ...], d_map: DistanceMap) -> int:
    cur_city, *stops = route

    distance: int = 0
    for stop in stops:
        distance += d_map[cur_city][stop]
        cur_city = stop

    return distance


def get_min_max(input_path: str) -> tuple[int, int]:
    lines = read_as_lines(input_path)
    d_map = parse_distance_map(lines)

    cities: set[str] = set(d_map.keys())
    routes: list[tuple[str, ...]] = list(itertools.permutations(cities))

    distances = [total_distance(route, d_map) for route in routes]

    return min(distances), max(distances)


def part1(input_path: str = INPUT_PATH) -> int:
    return get_min_max(input_path)[0]


def part2(input_path: str = INPUT_PATH) -> int:
    return get_min_max(input_path)[1]

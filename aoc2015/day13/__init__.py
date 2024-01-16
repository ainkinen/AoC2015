import itertools
import os
from collections import defaultdict

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")

HappinessMap = dict[str, dict[str, int]]  # guest -> guest -> change


def parse_map(lines: list[str]) -> HappinessMap:
    h_map: HappinessMap = defaultdict(dict)

    for line in lines:
        line = line[:-1]  # without the trailing dot
        name_1, would, change, value, *_, name_2 = line.split(" ")
        sign = -1 if change == "lose" else 1
        h_map[name_1][name_2] = sign * int(value)

    return h_map


def rotate(guests: list[str]) -> list[str]:
    """Rotate the list with alphanumerically first guest at the start to catch duplicates"""
    key_guest = min(guests)
    key_idx = guests.index(key_guest)
    return guests[key_idx:] + guests[:key_idx]


def possible_orderings(guests: list[str]) -> list[list[str]]:
    keyed_orderings: dict[str, list[str]] = {
        "".join(rotate(list(permutation))): list(permutation)
        for permutation in itertools.permutations(guests)
    }

    return list(keyed_orderings.values())


def score_ordering(ordering: list[str], h_map: HappinessMap) -> int:
    total = 0

    for idx, guest in enumerate(ordering):
        left = ordering[idx - 1]
        right = ordering[(idx + 1) % len(ordering)]
        total += h_map[guest][left]
        total += h_map[guest][right]

    return total


def part1(input_path: str = INPUT_PATH) -> int:
    h_map = parse_map(read_as_lines(input_path))
    guests = list(h_map.keys())

    orderings = possible_orderings(guests)

    return max(score_ordering(ordering, h_map) for ordering in orderings)


def part2(input_path: str = INPUT_PATH) -> int:
    h_map = parse_map(read_as_lines(input_path))
    guests = list(h_map.keys())

    # add me
    for guest in guests:
        h_map["me"][guest] = 0
        h_map[guest]["me"] = 0

    guests.append("me")

    orderings = possible_orderings(guests)

    return max(score_ordering(ordering, h_map) for ordering in orderings)

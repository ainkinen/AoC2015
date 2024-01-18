import itertools
import math
import os

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def min_qe(packages: set[int], num_groups: int) -> int:
    target_weight = sum(packages) // num_groups

    num_packages = len(packages)

    for n in range(num_packages - 2):
        n_package_sets = list(
            c for c in itertools.combinations(packages, n) if sum(c) == target_weight
        )

        if n_package_sets:
            qes = [math.prod(s) for s in n_package_sets]
            return min(qes)

    raise Exception("Not found")


def part1(input_path: str = INPUT_PATH) -> int:
    packages = set(map(int, read_as_lines(input_path)))
    return min_qe(packages, 3)


def part2(input_path: str = INPUT_PATH) -> int:
    packages = set(map(int, read_as_lines(input_path)))
    return min_qe(packages, 4)

import os

from aoc2015.utils.files import read_as_string

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")

Coord = complex  # real, imag = y, x

moves = {
    ">": 1j,
    "<": -1j,
    "^": -1,
    "v": 1,
}


def visits(instructions: str) -> list[Coord]:
    at = 0
    visited: list[Coord] = [at]

    for ins in instructions:
        at += moves[ins]
        visited.append(at)

    return visited


def part1(input_path: str = INPUT_PATH) -> int:
    instructions = read_as_string(input_path)

    return len(set(visits(instructions)))


def part2(input_path: str = INPUT_PATH) -> int:
    all_instructions = read_as_string(input_path)
    santa_instructions = all_instructions[0::2]
    robo_instructions = all_instructions[1::2]

    santa_visits = visits(santa_instructions)
    robo_visits = visits(robo_instructions)

    return len(set(santa_visits) | set(robo_visits))

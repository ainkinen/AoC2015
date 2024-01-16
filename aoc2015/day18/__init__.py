import os

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")

Coord = complex  # real, imag = y, x
Direction = complex

directions: set[Direction] = {
    -1 - 1j,
    -1,
    -1 + 1j,
    -1j,
    # 0 Center
    +1j,
    1 - 1j,
    1,
    1 + 1j,
}

LitLights = set[Coord]


def initial_lights(lines: list[str]) -> LitLights:
    lit: set[Coord] = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                lit.add((y + x * 1j))

    return lit


def step_lights(lit: LitLights, max_y: int, max_x: int) -> LitLights:
    next_lit: set[Coord] = set()
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            coord = y + x * 1j
            lit_around = len(lit & {coord + d for d in directions})
            currently_lit = coord in lit
            if currently_lit:
                if 2 <= lit_around <= 3:
                    next_lit.add(coord)
            else:
                if lit_around == 3:
                    next_lit.add(coord)

    return next_lit


def part1(input_path: str = INPUT_PATH, steps: int = 100) -> int:
    lines = read_as_lines(input_path)
    lit = initial_lights(lines)
    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1

    for _ in range(steps):
        lit = step_lights(lit, max_y, max_x)

    return len(lit)


def corner_lights(max_y: int, max_x: int) -> set[Coord]:
    min_y = min_x = 0
    return {
        min_y + min_x * 1j,
        min_y + max_x * 1j,
        max_y + min_x * 1j,
        max_y + max_x * 1j,
    }


def part2(input_path: str = INPUT_PATH, steps=100) -> int:
    lines = read_as_lines(input_path)
    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1

    lit = initial_lights(lines) | corner_lights(max_y, max_x)

    for _ in range(steps):
        lit = step_lights(lit, max_y, max_x) | corner_lights(max_y, max_x)

    return len(lit)

import os

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def run(registers: dict[str, int], instructions: list[str], output: str) -> int:
    pc = 0
    while 0 <= pc < len(instructions):
        op = instructions[pc]
        reg = op[4]

        match op[:3]:
            case "hlf":
                registers[reg] = registers[reg] // 2
            case "tpl":
                registers[reg] *= 3
            case "inc":
                registers[reg] += 1
            case "jmp":
                offset = int(op[4:])
                pc += offset
                continue
            case "jie":
                offset = int(op[7:])
                if registers[reg] % 2 == 0:
                    pc += offset
                    continue
            case "jio":
                offset = int(op[7:])
                if registers[reg] == 1:
                    pc += offset
                    continue

        pc += 1

    return registers[output]


def part1(input_path: str = INPUT_PATH, output: str = "b") -> int:
    instructions = read_as_lines(input_path)

    return run({"a": 0, "b": 0}, instructions, output)


def part2(input_path: str = INPUT_PATH, output="b") -> int:
    instructions = read_as_lines(input_path)

    return run({"a": 1, "b": 0}, instructions, output)

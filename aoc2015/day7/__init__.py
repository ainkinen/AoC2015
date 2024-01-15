import os
from functools import cache
from typing import NamedTuple, assert_never

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Node(NamedTuple):
    input_a: str
    input_b: str
    op: str


def parse_connection(line: str) -> tuple[str, Node | int]:
    left, name = line.split(" -> ")
    op_parts = left.split(" ")

    match len(op_parts):
        case 1:
            if left.isdigit():
                # static input
                return name, int(left)
            else:
                return name, Node(left, "_", "IS")

        case 2:
            # NOT
            return name, Node(op_parts[1], "_", op_parts[0])

        case 3:
            # Two input nodes
            return name, Node(op_parts[0], op_parts[2], op_parts[1])

        case _:
            raise Exception(f"Unknown connection {line}")


def part1(input_path: str = INPUT_PATH, output_wire: str = "a") -> int:
    circuit: dict[str, Node | int] = dict(
        parse_connection(line) for line in read_as_lines(input_path)
    )

    @cache
    def final_value(wire: str) -> int:
        if wire.isdigit():
            return int(wire)

        node = circuit[wire]

        match node:
            case int():
                return node
            case Node():
                match node.op:
                    case "IS":
                        return final_value(node.input_a)
                    case "AND":
                        return final_value(node.input_a) & final_value(node.input_b)
                    case "OR":
                        return final_value(node.input_a) | final_value(node.input_b)
                    case "LSHIFT":
                        return (
                            final_value(node.input_a) << final_value(node.input_b)
                        ) % 65536
                    case "RSHIFT":
                        return (
                            final_value(node.input_a) >> final_value(node.input_b)
                        ) % 65536
                    case "NOT":
                        return (~final_value(node.input_a)) % 65536
                    case _:
                        raise Exception(f"Unknown op {node.op}")
            case _:
                assert_never(node)

    return final_value(output_wire)


def part2(input_path: str = INPUT_PATH, output_wire: str = "a") -> int:
    circuit: dict[str, Node | int] = dict(
        parse_connection(line) for line in read_as_lines(input_path)
    )

    @cache
    def final_value(wire: str) -> int:
        if wire.isdigit():
            return int(wire)

        node = circuit[wire]

        match node:
            case int():
                return node
            case Node():
                match node.op:
                    case "IS":
                        return final_value(node.input_a)
                    case "AND":
                        return final_value(node.input_a) & final_value(node.input_b)
                    case "OR":
                        return final_value(node.input_a) | final_value(node.input_b)
                    case "LSHIFT":
                        return (
                            final_value(node.input_a) << final_value(node.input_b)
                        ) % 65536
                    case "RSHIFT":
                        return (
                            final_value(node.input_a) >> final_value(node.input_b)
                        ) % 65536
                    case "NOT":
                        return (~final_value(node.input_a)) % 65536
                    case _:
                        raise Exception(f"Unknown op {node.op}")
            case _:
                assert_never(node)

    new_b = final_value(output_wire)
    circuit["b"] = new_b
    final_value.cache_clear()

    return final_value(output_wire)

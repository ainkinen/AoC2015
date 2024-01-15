import hashlib
import itertools
import os

from aoc2015.utils.files import read_as_string

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def find_nonce(key: str, num_zeroes: int) -> int:
    cap = 1_000_000_000
    for nonce in range(cap):
        md5_hash = hashlib.md5((key + str(nonce)).encode())

        if md5_hash.hexdigest().startswith("".join(itertools.repeat("0", num_zeroes))):
            return nonce

        nonce += 1

    raise Exception(f"No valid nonce found < {cap}")


def part1(input_path: str = INPUT_PATH) -> int:
    key = read_as_string(input_path)

    return find_nonce(key, 5)


def part2(input_path: str = INPUT_PATH) -> int:
    key = read_as_string(input_path)

    return find_nonce(key, 6)

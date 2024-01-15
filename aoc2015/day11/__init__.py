import os
import re

from aoc2015.utils.files import read_as_string

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")

a_code = ord("a")
z_code = ord("z")
i_code = ord("i")
o_code = ord("o")
l_code = ord("l")


def increment(string: str) -> str:
    char_codes = [ord(c) for c in string]

    for idx, code in reversed(list(enumerate(char_codes))):
        new_code = (code + 1) % (z_code + 1)
        new_code = max(new_code, a_code)  # wrap to a
        char_codes[idx] = new_code

        if new_code in [i_code, o_code, l_code]:
            # skip to next valid
            char_codes[idx] += 1
            # set rest to a
            for i in range(idx + 1, len(char_codes)):
                char_codes[i] = a_code
            break

        if new_code != a_code:
            # did not roll over, end
            break

    return "".join(chr(code) for code in char_codes)


def has_increasing_chain(string: str) -> bool:
    for i in range(2, len(string)):
        a = ord(string[i - 2])
        b = ord(string[i - 1])
        c = ord(string[i])

        if a == c - 2 and b == c - 1:
            return True

    return False


def has_two_pairs(string: str) -> bool:
    return bool(re.match(r".*(\w)\1.*(\w)\2.*", string))


def rotate(password: str) -> str:
    while True:
        password = increment(password)

        if has_increasing_chain(password) and has_two_pairs(password):
            return password


def part1(input_path: str = INPUT_PATH) -> str:
    password = read_as_string(input_path).strip()
    return rotate(password)


def part2(input_path: str = INPUT_PATH) -> str:
    password = read_as_string(input_path).strip()
    return rotate(rotate(password))

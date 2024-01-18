import itertools
import os
import re
from dataclasses import dataclass
from math import ceil
from typing import NamedTuple

from aoc2015.utils.files import read_as_string

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Stats(NamedTuple):
    name: str
    cost: int
    damage: int
    armor: int


@dataclass
class Character:
    hit_points: int
    damage: int
    armor: int


weapon_options = {
    Stats("Dagger", 8, 4, 0),
    Stats("Shortsword", 10, 5, 0),
    Stats("Warhammer", 25, 6, 0),
    Stats("Longsword", 40, 7, 0),
    Stats("Greataxe", 74, 8, 0),
}

armor_options = {
    Stats("Leather", 13, 0, 1),
    Stats("Chainmail", 31, 0, 2),
    Stats("Splintmail", 53, 0, 3),
    Stats("Bandedmail", 75, 0, 4),
    Stats("Platemail", 102, 0, 5),
    Stats("No armor", 0, 0, 0),
}

ring_options = {
    Stats("Damage +1", 25, 1, 0),
    Stats("Damage +2", 50, 2, 0),
    Stats("Damage +3", 100, 3, 0),
    Stats("Defense +1", 20, 0, 1),
    Stats("Defense +2", 40, 0, 2),
    Stats("Defense +3", 80, 0, 3),
    Stats("No ring 1", 0, 0, 0),
    Stats("No ring 2", 0, 0, 0),
}


def parse_input(in_str: str) -> Character:
    number = r"\d+"
    hit_points, damage, armor = map(int, re.findall(number, in_str))

    return Character(hit_points, damage, armor)


def player_wins(player: Character, boss: Character) -> bool:
    player_effect = max(1, player.damage - boss.armor)
    boss_effect = max(1, boss.damage - player.armor)

    player_rounds_for_kill = ceil(boss.hit_points / player_effect)
    boss_rounds_for_kill = ceil(player.hit_points / boss_effect)

    return player_rounds_for_kill <= boss_rounds_for_kill


def part1(input_path: str = INPUT_PATH, player_hit_points: int = 100) -> int:
    boss = parse_input(read_as_string(input_path))

    setups: list[tuple[Stats, Stats, tuple[Stats, Stats]]] = list(
        itertools.product(
            weapon_options, armor_options, itertools.combinations(ring_options, 2)
        )
    )

    players_with_setups = [
        Character(
            hit_points=player_hit_points,
            damage=weapon.damage + armor.damage + rings[0].damage + rings[1].damage,
            armor=weapon.armor + armor.armor + rings[0].armor + rings[1].armor,
        )
        for weapon, armor, rings in setups
    ]

    setup_costs = [
        weapon.cost + armor.cost + rings[0].cost + rings[1].cost
        for weapon, armor, rings in setups
    ]

    results = [player_wins(p, boss) for p in players_with_setups]

    won_costs = [cost for idx, cost in enumerate(setup_costs) if results[idx]]

    return min(won_costs)


def part2(input_path: str = INPUT_PATH, player_hit_points: int = 100) -> int:
    boss = parse_input(read_as_string(input_path))

    setups: list[tuple[Stats, Stats, tuple[Stats, Stats]]] = list(
        itertools.product(
            weapon_options, armor_options, itertools.combinations(ring_options, 2)
        )
    )

    players_with_setups = [
        Character(
            hit_points=player_hit_points,
            damage=weapon.damage + armor.damage + rings[0].damage + rings[1].damage,
            armor=weapon.armor + armor.armor + rings[0].armor + rings[1].armor,
        )
        for weapon, armor, rings in setups
    ]

    setup_costs = [
        weapon.cost + armor.cost + rings[0].cost + rings[1].cost
        for weapon, armor, rings in setups
    ]

    results = [player_wins(p, boss) for p in players_with_setups]

    lost_costs = [cost for idx, cost in enumerate(setup_costs) if not results[idx]]

    return max(lost_costs)

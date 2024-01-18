import os
import re
from typing import NamedTuple, Iterable

from aoc2015.utils.files import read_as_string

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class State(NamedTuple):
    player_hp: int
    boss_hp: int
    boss_damage: int
    player_mana: int
    mana_used: int
    shield_timer: int
    poison_timer: int
    recharge_timer: int


def player_turn(state: State, extra_drain: bool = False) -> Iterable[State]:
    """Yield new states starting from worst to keep the dfs stack optimal"""

    (
        player_hp,
        boss_hp,
        boss_damage,
        player_mana,
        mana_used,
        shield_timer,
        poison_timer,
        recharge_timer,
    ) = state

    # player turn effects
    if extra_drain:
        player_hp -= 1
    if shield_timer:
        shield_timer -= 1
    if poison_timer:
        poison_timer -= 1
        boss_hp -= 3
    if recharge_timer:
        recharge_timer -= 1
        player_mana += 101

    if player_hp <= 0 or boss_hp <= 0:
        # dead no new states
        return []

    if not recharge_timer and player_mana >= 229:
        yield State(
            player_hp,
            boss_hp,
            boss_damage,
            player_mana - 229,
            mana_used + 229,
            shield_timer,
            poison_timer,
            recharge_timer + 5,
        )

    if not poison_timer and player_mana >= 173:
        yield State(
            player_hp,
            boss_hp,
            boss_damage,
            player_mana - 173,
            mana_used + 173,
            shield_timer,
            poison_timer + 6,
            recharge_timer,
        )

    if not shield_timer and player_mana >= 113:
        yield State(
            player_hp,
            boss_hp,
            boss_damage,
            player_mana - 113,
            mana_used + 113,
            shield_timer + 6,
            poison_timer,
            recharge_timer,
        )

    if player_mana >= 73:
        yield State(
            player_hp + 2,
            boss_hp - 2,
            boss_damage,
            player_mana - 73,
            mana_used + 73,
            shield_timer,
            poison_timer,
            recharge_timer,
        )

    if player_mana >= 53:
        yield State(
            player_hp,
            boss_hp - 4,
            boss_damage,
            player_mana - 53,
            mana_used + 53,
            shield_timer,
            poison_timer,
            recharge_timer,
        )


def boss_turn(state: State) -> State:
    (
        player_hp,
        boss_hp,
        boss_damage,
        player_mana,
        mana_used,
        shield_timer,
        poison_timer,
        recharge_timer,
    ) = state

    # boss attack and effects
    player_hp -= max(1, boss_damage - (7 if shield_timer else 0))
    if shield_timer:
        shield_timer -= 1
    if poison_timer:
        poison_timer -= 1
        boss_hp -= 3
    if recharge_timer:
        recharge_timer -= 1
        player_mana += 101

    return State(
        player_hp,
        boss_hp,
        boss_damage,
        player_mana,
        mana_used,
        shield_timer,
        poison_timer,
        recharge_timer,
    )


def dfs(start_state: State, extra_drain: bool = False) -> int:
    stack: list[State] = [start_state]
    seen: set[State] = set()

    minimum_mana_seen = 1_000_000_000

    while stack:
        state = stack.pop()
        if state not in seen:
            if state.boss_hp <= 0:
                minimum_mana_seen = min(minimum_mana_seen, state.mana_used)

            seen.add(state)

            for next_s in player_turn(state, extra_drain):
                next_s = boss_turn(next_s)
                stack.append(next_s)

    return minimum_mana_seen


def part1(input_path: str = INPUT_PATH, hp: int = 50, mana: int = 500) -> int:
    boss_hp, boss_damage = map(int, re.findall(r"\d+", read_as_string(input_path)))
    return dfs(State(hp, boss_hp, boss_damage, mana, 0, 0, 0, 0))


def part2(
    input_path: str = INPUT_PATH, player_hp: int = 50, player_mana: int = 500
) -> int:
    boss_hp, boss_damage = map(int, re.findall(r"\d+", read_as_string(input_path)))
    return dfs(
        State(player_hp, boss_hp, boss_damage, player_mana, 0, 0, 0, 0),
        extra_drain=True,
    )

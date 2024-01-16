import itertools
import os
import re
from collections import Counter
from typing import NamedTuple

from aoc2015.utils.files import read_as_lines

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Ingredient(NamedTuple):
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


IngredientMap = dict[str, Ingredient]


def parse_ingredient(string: str) -> Ingredient:
    name, rest = string.split(":", maxsplit=1)
    capacity, durability, flavor, texture, calories = map(
        int, re.findall(r"-?\d+", rest)
    )

    return Ingredient(name, capacity, durability, flavor, texture, calories)


def score(recipe: Counter[Ingredient]) -> int:
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0

    for ingredient, amount in recipe.items():
        capacity += amount * ingredient.capacity
        durability += amount * ingredient.durability
        flavor += amount * ingredient.flavor
        texture += amount * ingredient.texture

    return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)


def calories(recipe: Counter[Ingredient]) -> int:
    return sum(amount * i.calories for i, amount in recipe.items())


def part1(input_path: str = INPUT_PATH) -> int:
    ingredient_map: IngredientMap = {
        i.name: i for i in map(parse_ingredient, read_as_lines(input_path))
    }

    ingredients = ingredient_map.values()

    recipes = (
        Counter(i) for i in itertools.combinations_with_replacement(ingredients, 100)
    )

    recipe_scores = map(score, recipes)

    return max(recipe_scores)


def part2(input_path: str = INPUT_PATH) -> int:
    ingredient_map: IngredientMap = {
        i.name: i for i in map(parse_ingredient, read_as_lines(input_path))
    }

    ingredients = ingredient_map.values()

    recipes = (
        Counter(i) for i in itertools.combinations_with_replacement(ingredients, 100)
    )

    meal_replacement_recipies = filter(lambda r: calories(r) == 500, recipes)

    recipe_scores = map(score, meal_replacement_recipies)

    return max(recipe_scores)

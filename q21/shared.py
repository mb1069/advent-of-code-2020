import os
import re
from functools import reduce


def get_all_ingredients(food_list):
    all_ingredients = reduce(lambda a, b: a.union(b), [i[0] for i in food_list])
    return all_ingredients


def get_all_allergens(food_list):
    all_allergens = reduce(lambda a, b: a.union(b), [i[1] for i in food_list])
    return all_allergens


def get_non_allergic_ingredients(food_list):
    all_ingredients = get_all_ingredients(food_list)
    all_allergens = get_all_allergens(food_list)

    allergen_causes = dict()
    for allergen in all_allergens:
        # Reduce from set of all ingredients to set of ingredients which occur in every recipe for which allergy noted
        candidate_ingredients = {i for i in all_ingredients}
        for ingredients, allergens in food_list:
            if allergen in allergens:
                candidate_ingredients = candidate_ingredients.intersection(ingredients)
        allergen_causes[allergen] = candidate_ingredients

    allergic_ingredients = reduce(lambda a, b: a.union(b), allergen_causes.values())

    non_allergic_ingredients = all_ingredients.difference(allergic_ingredients)

    print(f'Non allergic ingredients: {non_allergic_ingredients}')

    total_occurences = 0
    for ingredients, _ in food_list:
        total_occurences += len(ingredients.intersection(non_allergic_ingredients))

    print(f'Total non-allergic food occurences: {total_occurences}')

    return non_allergic_ingredients


def clean_input(ingredients, allergens):
    return set(ingredients.split(' ')), set(allergens.split(', '))


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        txt = [l.strip() for l in f.readlines()]

    ingredients_alergents = [clean_input(*re.findall(r'(.+) \(contains (.+)\)', l)[0]) for l in txt]

    return ingredients_alergents

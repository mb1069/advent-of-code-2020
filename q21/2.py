from q21.shared import read_file, get_non_allergic_ingredients, get_all_allergens, get_all_ingredients


class AllergenAllocator:
    def __init__(self, allergy_ingredients):
        self.allergy_ingredients = allergy_ingredients
        self.solved_ingredients = set()

    def is_solved(self):
        solved = all([len(i[1]) == 1 for i in self.allergy_ingredients.items()])
        if not solved:
            print(self.allergy_ingredients)
        return solved

    def collect_solved_ingredients(self):
        for a, i in self.allergy_ingredients.items():
            if len(i) == 1:
                self.solved_ingredients = self.solved_ingredients.union(i)

    def remove_solved_ingredients(self):
        for a in self.allergy_ingredients:
            print(len(self.allergy_ingredients[a]), (self.allergy_ingredients[a]))
            if len(self.allergy_ingredients[a]) > 1 and len(self.allergy_ingredients[a].intersection(self.solved_ingredients)) >= 1:
                print(f'Stripping {a}: {self.allergy_ingredients[a]} -> {self.allergy_ingredients[a].difference(self.solved_ingredients)}')
                self.allergy_ingredients[a] = self.allergy_ingredients[a].difference(self.solved_ingredients)

    def solve(self):
        solved_ingredients = set()
        while not self.is_solved():
            self.collect_solved_ingredients()
            self.remove_solved_ingredients()
        return self.allergy_ingredients


def main():
    food_list = read_file()
    inert_ingredients = get_non_allergic_ingredients(food_list)

    allergen_food_list = [(ing.difference(inert_ingredients), al) for ing, al in food_list]

    all_ingredients = get_all_ingredients(food_list)

    allergy_candidate_ingredients = dict()

    for a in get_all_allergens(food_list):
        candidate_ingredients = {ing for ing in all_ingredients}
        for ingredients, allergies in allergen_food_list:
            if a in allergies:
                candidate_ingredients = candidate_ingredients.intersection(ingredients)

        allergy_candidate_ingredients[a] = candidate_ingredients

    aa = AllergenAllocator(allergy_candidate_ingredients)

    solution = aa.solve().items()

    sorted_solution = sorted(solution, key=lambda r: r[0])
    ingredients = [i[1].pop() for i in sorted_solution]
    print(','.join(ingredients))



if __name__ == '__main__':
    main()

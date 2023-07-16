from collections import defaultdict, Counter
from typing import List


def findAllRecipes(recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    available = set(supplies)
    print(available)
    ans, ingredient_to_recipe, in_degree = [], defaultdict(set), Counter()
    for recipe, ingredient in zip(recipes, ingredients):
        print(recipe, ingredient)
        non_available = 0
        for ing in ingredient:
            if ing not in available:
                print(f"With recipe {recipe}: {ing} not in {available}")
                non_available += 1
                ingredient_to_recipe[ing].add(recipe)
        if non_available == 0:
            ans.append(recipe)
        else:
            in_degree[recipe] = non_available

    print(ans)
    print("in_degree", in_degree)
    print("ingredient_to_recipe", ingredient_to_recipe)
    for rcp in ans:
        for recipe in ingredient_to_recipe.pop(rcp, set()):
            print(f"recipe: {recipe}")
            in_degree[recipe] -= 1
            if in_degree[recipe] == 0:
                ans.append(recipe)
    return ans


class Solution:
    pass

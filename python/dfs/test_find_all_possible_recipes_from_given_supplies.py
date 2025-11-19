import unittest
from .find_all_possible_recipes_from_given_supplies import (
    BFS,
    DFS,
    TopologicalSortKahnAlgorithm,
)


class BaseTestFindAllRecipes:
    """Base test class containing all test cases."""

    def test_basic_recipes(self):
        # Test case with simple recipes where all ingredients are supplies
        recipes = ["bread"]
        ingredients = [["flour", "water"]]
        supplies = ["flour", "water"]
        expected = ["bread"]
        result = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(result, expected)

    def test_dependent_recipes(self):
        # Test case where one recipe depends on another recipe
        recipes = ["bread", "sandwich"]
        ingredients = [["flour", "water"], ["bread", "meat"]]
        supplies = ["flour", "water", "meat"]
        expected = ["bread", "sandwich"]
        result = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(sorted(result), sorted(expected))

    def test_impossible_recipes(self):
        # Test case where some recipes cannot be made
        recipes = ["bread", "sandwich", "burger"]
        ingredients = [["flour", "water"], ["bread", "meat"], ["bread", "lettuce"]]
        supplies = ["flour", "meat"]
        expected = []  # Can't make any recipe without water
        result = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(result, expected)

    def test_cyclic_dependency(self):
        # Test case with cyclic dependencies between recipes
        recipes = ["recipe1", "recipe2"]
        ingredients = [["recipe2"], ["recipe1"]]
        supplies = ["flour", "water"]
        expected = []  # Cyclic dependency means no recipe can be made
        result = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(result, expected)

    def test_complex_dependencies(self):
        # Test case with complex dependencies between recipes
        recipes = ["bread", "sandwich", "burger", "pizza"]
        ingredients = [
            ["flour", "water"],  # bread
            ["bread", "meat"],  # sandwich
            ["bread", "meat", "lettuce"],  # burger
            ["flour", "cheese", "tomato"],  # pizza
        ]
        supplies = ["flour", "water", "meat", "lettuce", "cheese", "tomato"]
        expected = ["bread", "sandwich", "burger", "pizza"]
        result = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(sorted(result), sorted(expected))

    def test_empty_inputs(self):
        # Test case with empty inputs
        recipes = []
        ingredients = []
        supplies = []
        expected = []
        result = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(result, expected)

    def test_no_ingredients(self):
        # Test case where a recipe requires no ingredients
        recipes = ["simple"]
        ingredients = [[]]
        supplies = ["water", "flour"]
        expected = ["simple"]
        result = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(result, expected)


class TestBFS(unittest.TestCase, BaseTestFindAllRecipes):
    def setUp(self):
        self.solution = BFS()


class TestDFS(unittest.TestCase, BaseTestFindAllRecipes):
    def setUp(self):
        self.solution = DFS()


class TestTopologicalSort(unittest.TestCase, BaseTestFindAllRecipes):
    def setUp(self):
        self.solution = TopologicalSortKahnAlgorithm()


if __name__ == "__main__":
    unittest.main()

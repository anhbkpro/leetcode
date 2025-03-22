from collections import defaultdict, deque


class BFS:
    def findAllRecipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str],
    ) -> list[str]:
        # Initialize tracking dictionaries using comprehensions
        can_make = dict.fromkeys(supplies, True)
        recipe_to_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def _check_recipe(recipe: str, visited: set) -> bool:
            # Already processed and can be made
            if can_make.get(recipe, False):
                return True

            # Not a valid recipe or cycle detected
            if recipe not in recipe_to_idx or recipe in visited:
                return False

            visited.add(recipe)

            # Check if all ingredients can be made
            can_make[recipe] = all(
                _check_recipe(ingredient, visited)
                for ingredient in ingredients[recipe_to_idx[recipe]]
            )

            return can_make[recipe]

        # Process each recipe and collect those that can be made
        return [recipe for recipe in recipes if _check_recipe(recipe, set())]


class DFS:
    def findAllRecipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str],
    ) -> list[str]:
        # Initialize tracking dictionaries using comprehensions
        can_make = dict.fromkeys(supplies, True)
        recipe_to_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def _check_recipe(recipe: str, visited: set) -> bool:
            # Already processed and can be made
            if can_make.get(recipe, False):
                return True

            # Not a valid recipe or cycle detected
            if recipe not in recipe_to_idx or recipe in visited:
                return False

            visited.add(recipe)

            # Check if all ingredients can be made
            can_make[recipe] = all(
                _check_recipe(ingredient, visited)
                for ingredient in ingredients[recipe_to_idx[recipe]]
            )

            return can_make[recipe]

        # Process each recipe and collect those that can be made
        return [recipe for recipe in recipes if _check_recipe(recipe, set())]


class TopologicalSortKahnAlgorithm:
    def findAllRecipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str],
    ) -> list[str]:
        # Store available supplies
        available_supplies = set(supplies)
        # Map recipe to its index
        recipe_to_index = {recipe: idx for idx, recipe in enumerate(recipes)}
        # Map ingredient to recipes that need it
        dependency_graph = defaultdict(list)
        # Count of non-supply ingredients needed for each recipe
        in_degree = [0] * len(recipes)

        # Build dependency graph
        for recipe_idx, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient not in available_supplies:
                    dependency_graph[ingredient].append(recipes[recipe_idx])
                    in_degree[recipe_idx] += 1

        # Start with recipes that only need supplies
        queue = deque(idx for idx, count in enumerate(in_degree) if count == 0)
        created_recipes = []

        # Process recipes in topological order
        while queue:
            recipe_idx = queue.popleft()
            recipe = recipes[recipe_idx]
            created_recipes.append(recipe)

            # Skip if no recipes depend on this one
            for dependent_recipe in dependency_graph[recipe]:
                in_degree[recipe_to_index[dependent_recipe]] -= 1
                if in_degree[recipe_to_index[dependent_recipe]] == 0:
                    queue.append(recipe_to_index[dependent_recipe])

        return created_recipes

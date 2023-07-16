from lc_2115_find_all_possible_recipes_from_given_supplies import findAllRecipes


def test_find_all_recipes():
    assert findAllRecipes(
        recipes=["bread"],
        ingredients=[["yeast", "flour"]],
        supplies=["yeast", "flour", "corn"]
    ) == ["bread"]
    assert findAllRecipes(
        recipes=["bread", "sandwich"],
        ingredients=[["yeast", "flour"], ["bread", "meat"]],
        supplies=["yeast", "flour", "meat"]
    ) == ["bread", "sandwich"]
    assert findAllRecipes(
        recipes=["bread", "sandwich", "burger"],
        ingredients=[["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
        supplies=["yeast", "flour", "meat"]
    ) == ["bread", "sandwich", "burger"]

from .method_chaining import findHeavyAnimals
import pandas as pd


def test_find_heavy_animals():
    # Input:
    # DataFrame animals:
    # +----------+---------+-----+--------+
    # | name     | species | age | weight |
    # +----------+---------+-----+--------+
    # | Tatiana  | Snake   | 98  | 464    |
    # | Khaled   | Giraffe | 50  | 41     |
    # | Alex     | Leopard | 6   | 328    |
    # | Jonathan | Monkey  | 45  | 463    |
    # | Stefan   | Bear    | 100 | 50     |
    # | Tommy    | Panda   | 26  | 349    |
    # +----------+---------+-----+--------+
    # Output:
    # +----------+
    # | name     |
    # +----------+
    # | Tatiana  |
    # | Jonathan |
    # | Tommy    |
    # | Alex     |
    # +----------+
    animals = pd.DataFrame(
        {
            "name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
            "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
            "age": [98, 50, 6, 45, 100, 26],
            "weight": [464, 41, 328, 463, 50, 349],
        }
    )
    ans = findHeavyAnimals(animals)
    expected = ["Tatiana", "Jonathan", "Tommy", "Alex"]
    assert ans["name"].tolist() == expected

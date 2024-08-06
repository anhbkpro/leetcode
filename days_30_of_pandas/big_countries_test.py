from .big_countries import big_countries
import pandas as pd


def test_big_countries():
    # Input:
    # World table:
    # +-------------+-----------+---------+------------+--------------+
    # | name        | continent | area    | population | gdp          |
    # +-------------+-----------+---------+------------+--------------+
    # | Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
    # | Albania     | Europe    | 28748   | 2831741    | 12960000000  |
    # | Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
    # | Andorra     | Europe    | 468     | 78115      | 3712000000   |
    # | Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
    # +-------------+-----------+---------+------------+--------------+
    # Output:
    # +-------------+------------+---------+
    # | name        | population | area    |
    # +-------------+------------+---------+
    # | Afghanistan | 25500100   | 652230  |
    # | Algeria     | 37100000   | 2381741 |
    # +-------------+------------+---------+
    world = {
        "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
        "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
        "area": [652230, 28748, 2381741, 468, 1246700],
        "population": [25500100, 2831741, 37100000, 78115, 20609294],
        "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000],
    }
    world = pd.DataFrame(world)
    expected = {
        "name": ["Afghanistan", "Algeria"],
        "population": [25500100, 37100000],
        "area": [652230, 2381741],
    }
    expected = pd.DataFrame(expected)
    assert big_countries(world)["name"].to_list() == expected["name"].to_list()
    assert big_countries(world)["population"].to_list() == expected["population"].to_list()
    assert big_countries(world)["area"].to_list() == expected["area"].to_list()

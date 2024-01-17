from lc_1207_unique_number_of_occurrences import Solution


def test_unique_occurrences():
    assert Solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]) is True
    assert Solution.uniqueOccurrences([1, 2]) is False

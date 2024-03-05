from lc_1750_minimum_length_of_string_after_deleting_similar_ends import Solution


def test_minimum_length():
    assert Solution.minimum_length("ca") == 2
    assert Solution.minimum_length("cabaabac") == 0
    assert Solution.minimum_length("aabccabba") == 3
    assert Solution.minimum_length("a") == 1

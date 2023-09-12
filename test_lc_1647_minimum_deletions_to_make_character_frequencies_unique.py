from lc_1647_minimum_deletions_to_make_character_frequencies_unique import Solution


def test_min_deletions():
    assert Solution.min_deletions("aab") == 0
    assert Solution.min_deletions("aaabbbcc") == 2
    assert Solution.min_deletions("ceabaacb") == 2  # frequency of 0 is ignored

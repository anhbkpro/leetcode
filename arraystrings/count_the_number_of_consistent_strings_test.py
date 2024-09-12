from .count_the_number_of_consistent_strings import Solution


def test_count_consistent_strings():
    assert Solution().countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]) == 2
    assert Solution().countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]) == 7

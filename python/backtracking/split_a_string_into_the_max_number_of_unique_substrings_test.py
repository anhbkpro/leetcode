from .split_a_string_into_the_max_number_of_unique_substrings import Solution


def test_split_a_string_into_the_max_number_of_unique_substrings():
    assert Solution().maxUniqueSplit(s="ababccc") == 5
    assert Solution().maxUniqueSplit(s="aba") == 2

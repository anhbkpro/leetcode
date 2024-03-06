from lc_340_longest_substring_with_at_most_k_distinct_characters import (
    Solution,
)


def test_length_of_longest_substring_kdistinct():
    assert Solution.length_of_longest_substring_k_distinct(s="eceba", k=2) == 3
    assert Solution.length_of_longest_substring_k_distinct(s="aa", k=1) == 2
    assert Solution.length_of_longest_substring_k_distinct(s="a", k=1) == 1

from lc_340_longest_substring_with_at_most_k_distinct_characters import lengthOfLongestSubstringKDistinct


def test_length_of_longest_substring_kdistinct():
    assert lengthOfLongestSubstringKDistinct(s="eceba", k=2) == 3
    assert lengthOfLongestSubstringKDistinct(s="aa", k=1) == 2
    assert lengthOfLongestSubstringKDistinct(s="a", k=1) == 1

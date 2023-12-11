from lc_28_find_the_index_of_the_first_occurrence_in_a_string import Solution


def test_str_str():
    assert Solution.strStr(haystack="hello", needle="ll") == 2
    assert Solution.strStr(haystack="aaaaa", needle="bba") == -1
    assert Solution.strStr(haystack="a", needle="a") == 0
    assert Solution.strStr(haystack="sadbutsad", needle="sad") == 0
    assert Solution.strStr(haystack="leetcode", needle="leeto") == -1

from lc_1662_check_if_two_string_arrays_are_equivalent import Solution


def test_array_strings_are_equal():
    assert Solution.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]) is True
    assert Solution.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]) is False

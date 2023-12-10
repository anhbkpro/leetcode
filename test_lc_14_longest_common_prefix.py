from lc_14_longest_common_prefix import Solution


def test_longest_common_prefix():
    assert Solution.longestCommonPrefix(strs=["flower", "flow", "flight"]) == "fl"
    assert Solution.longestCommonPrefix(strs=["dog", "racecar", "car"]) == ""

from .adding_spaces_to_a_string import Solution


def test_add_spaces():
    assert (
        Solution().addSpaces(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15])
        == "Leetcode Helps Me Learn"
    )

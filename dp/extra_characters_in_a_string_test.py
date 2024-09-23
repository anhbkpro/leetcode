from .extra_characters_in_a_string import Solution


def test_min_extra_char():
    assert (
        Solution().minExtraChar(s="leetscode", dictionary=["leet", "code", "leetcode"])
        == 1
    )

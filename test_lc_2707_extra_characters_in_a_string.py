from lc_2707_extra_characters_in_a_string import Solution

s = Solution()


def test_min_extra_char():
    assert s.minExtraChar(s="leetscode", dictionary=["leet", "code", "leetcode"]) == 1
    assert s.minExtraChar(s="leetcode", dictionary=["leet", "code"]) == 0
    assert s.minExtraChar(s="sayhelloworld", dictionary=["hello", "world"]) == 3

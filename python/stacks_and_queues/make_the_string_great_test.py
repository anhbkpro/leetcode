from .make_the_string_great import Solution


def test_make_good():
    s = Solution()
    assert s.makeGood("leEeetcode") == "leetcode"
    assert s.makeGood("abBAcC") == ""
    assert s.makeGood("s") == "s"

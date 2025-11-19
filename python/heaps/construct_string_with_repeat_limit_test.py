from .construct_string_with_repeat_limit import Solution


def test_repeat_limited_string():
    assert Solution().repeatLimitedString(s="cczazcc", repeatLimit=3) == "zzcccac"
    assert Solution().repeatLimitedString(s="aababab", repeatLimit=2) == "bbabaa"

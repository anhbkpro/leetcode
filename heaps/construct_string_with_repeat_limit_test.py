from .construct_string_with_repeat_limit import Solution


def test_repeat_limited_string():
    assert Solution().constructString(s="cczazcc", repeatLimit=3) == "zzcccac"
    assert Solution().constructString(s="aababab", repeatLimit=2) == "bbabaa"

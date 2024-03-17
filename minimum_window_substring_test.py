from minimum_window_substring import Solution


def test_min_window():
    assert Solution.minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert Solution.minWindow(s="a", t="a") == "a"
    assert Solution.minWindow(s="a", t="aa") == ""

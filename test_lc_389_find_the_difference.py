from lc_389_find_the_difference import Solution


def test_find_the_difference():
    assert Solution.findTheDifference(s="abcd", t="abcde") == "e"
    assert Solution.findTheDifference(s="", t="y") == "y"

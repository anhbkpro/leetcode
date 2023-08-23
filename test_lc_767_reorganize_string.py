from lc_767_reorganize_string import Solution


def test_reorganize_string():
    assert Solution.reorganize_string("aab") == "aba"
    assert Solution.reorganize_string("aaab") == ""
    assert Solution.reorganize_string("vvvlo") == "vlvov"

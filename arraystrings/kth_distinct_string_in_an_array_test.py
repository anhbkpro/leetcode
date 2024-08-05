from .kth_distinct_string_in_an_array import Solution


def test_kth_distinct():
    assert Solution().kthDistinct(["a", "b", "c", "a"], 2) == "c"
    assert Solution().kthDistinct(["a", "b", "c", "a"], 3) == ""

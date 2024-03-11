from lc_791_custom_sort_string import Solution


def test_custom_sort_string():
    assert Solution.custom_sort_string(order="cba", s="abcd") == "cbad"
    assert Solution.custom_sort_string(order="cba", s="abcd") == "cbad"

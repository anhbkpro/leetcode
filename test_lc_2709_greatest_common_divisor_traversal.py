from lc_2709_greatest_common_divisor_traversal import Solution


def test_can_traverse_all_pairs():
    assert Solution.can_traverse_all_pairs([2, 3, 6, 9]) is True
    assert Solution.can_traverse_all_pairs([7, 5, 6, 8]) is False

from lc_201_bitwise_and_of_numbers_range import Solution


def test_range_bitwise_and():
    assert Solution.range_bitwise_and(left=5, right=7) == 4
    assert Solution.range_bitwise_and(left=0, right=0) == 0
    assert Solution.range_bitwise_and(left=1, right=2147483647) == 0

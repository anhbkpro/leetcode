from lc_15_3sum import threeSum


def test_three_sum():
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum([]) == []
    assert threeSum([0, 0, 0]) == [[0, 0, 0]]

from lc_852_peak_index_in_a_mountain_array import Solution


def test_peak_index_in_mountain_array():
    assert Solution.peak_index_in_mountain_array(arr=[0, 1, 0]) == 1
    assert Solution.peak_index_in_mountain_array(arr=[0, 2, 1, 0]) == 1

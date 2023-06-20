from lc_2090_k_radius_subarray_averages import getAverages


def test_get_averages():
    assert getAverages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3) == [-1, -1, -1, 5, 4, 4, -1, -1, -1]
    assert getAverages(nums=[100000], k=0) == [100000]
    assert getAverages(nums=[8], k=100000) == [-1]

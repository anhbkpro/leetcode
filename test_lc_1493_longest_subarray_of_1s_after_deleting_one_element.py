from lc_1493_longest_subarray_of_1s_after_deleting_one_element import longestSubarray


def test_longest_subarray():
    assert longestSubarray([1, 1, 0, 1]) == 3
    assert longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
    assert longestSubarray([1, 1, 1]) == 2

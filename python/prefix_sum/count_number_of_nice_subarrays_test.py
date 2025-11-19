from .count_number_of_nice_subarrays import Solution


def test_count_number_of_nice_subarrays():
    assert Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2
    assert Solution().numberOfSubarrays([2, 4, 6], 1) == 0

from .find_k_th_smallest_pair_distance import Solution


def test_find_k_th_smallest_pair_distance():
    assert Solution().smallestDistancePair(nums=[1, 3, 1], k=1) == 0
    assert Solution().smallestDistancePair(nums=[1, 1, 1], k=2) == 0
    assert Solution().smallestDistancePair(nums=[1, 6, 1], k=3) == 5

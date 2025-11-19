from .continuous_subarrays import Solution


def test_continuous_subarrays():
    assert Solution().continuousSubarrays(nums=[5, 4, 2, 4]) == 8
    assert Solution().continuousSubarrays(nums=[1, 2, 3]) == 6

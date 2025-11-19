from .find_the_power_of_k_size_subarrays_i import Solution


def test_results_array():
    assert Solution().resultsArray(nums=[1, 2, 3, 4, 3, 2, 5], k=3) == [
        3,
        4,
        -1,
        -1,
        -1,
    ]

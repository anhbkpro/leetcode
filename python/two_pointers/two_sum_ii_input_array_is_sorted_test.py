from .two_sum_ii_input_array_is_sorted import Solution


def test_two_sum_ii():
    assert Solution().twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
    assert Solution().twoSum(numbers=[2, 3, 4], target=6) == [1, 3]
    assert Solution().twoSum(numbers=[-1, 0], target=-1) == [1, 2]

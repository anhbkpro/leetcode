from backtracking.the_number_of_beautiful_subsets import Solution


def test_number_of_beautiful_subsets():
    assert Solution().beautifulSubsets(nums = [2,4,6], k = 2) == 4
    assert Solution().beautifulSubsets(nums = [1], k = 1) == 1

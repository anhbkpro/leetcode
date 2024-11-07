from .largest_combination_with_bitwise_and_greater_than_zero import Solution, SolutionBitCount


def test_largest_combination_with_bitwise_and_greater_than_zero():
    assert Solution().largestCombination(candidates=[16, 17, 71, 62, 12, 24, 14]) == 4
    assert SolutionBitCount().largestCombination(candidates=[16, 17, 71, 62, 12, 24, 14]) == 4

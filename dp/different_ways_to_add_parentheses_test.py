from .different_ways_to_add_parentheses import Solution


def test_different_ways_to_add_parentheses():
    assert sorted(Solution().diffWaysToCompute("2-1-1")) == [0, 2]
    assert sorted(Solution().diffWaysToCompute("2*3-4*5")) == [-34, -14, -10, -10, 10]

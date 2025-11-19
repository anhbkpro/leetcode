from backtracking.subsets import Solution


def test_subsets():
    assert Solution().subsets([1, 2]) == [[], [1], [2], [1, 2]]
    assert Solution().subsets([0]) == [[], [0]]
